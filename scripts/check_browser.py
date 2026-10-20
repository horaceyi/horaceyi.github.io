#!/usr/bin/env python3
"""Exercise the real static site in Chromium and capture review artifacts."""
import argparse
from functools import partial
from http.server import ThreadingHTTPServer
import json
from pathlib import Path
import shutil
from threading import Thread

from check_site import ROOT, QuietHandler


def check_rendering(page, name):
    """Reject unstyled HTML and decoded-image failures, including HTTP 200 fallbacks."""
    state = page.evaluate('''() => ({
      heading: document.querySelector('h1').textContent.trim(),
      chineseName: document.querySelector('.alternate-name').textContent.trim(),
      heroDisplay: getComputedStyle(document.querySelector('.hero')).display,
      navDisplay: getComputedStyle(document.querySelector('nav')).display,
      stylesheets: [...document.styleSheets].map(s => ({
        href: s.href,
        rules: (() => { try { return s.cssRules.length; } catch { return 0; } })()
      })),
      fonts: [...document.fonts].map(f => ({family: f.family, status: f.status})),
      images: [...document.images].map(i => ({
        src: i.currentSrc, complete: i.complete, naturalWidth: i.naturalWidth
      }))
    })''')
    assert state['heading'] == 'Hongrui (Horace) Yi', f'{name}: incorrect hero name'
    assert state['chineseName'] == '易弘睿', f'{name}: Chinese name is not separate'
    assert any(s['href'] and s['href'].endswith('/red.css') and s['rules'] > 0 for s in state['stylesheets']), f'{name}: stylesheet not applied'
    assert state['heroDisplay'] == 'grid' and state['navDisplay'] == 'flex', f'{name}: layout styles missing'
    assert all(any(f['family'] == family and f['status'] == 'loaded' for f in state['fonts']) for family in ['Manrope', 'Newsreader']), f'{name}: web fonts not loaded'
    assert all(i['complete'] and i['naturalWidth'] > 0 for i in state['images']), f'{name}: image not decoded'
    content = page.locator('.hero-content').bounding_box()
    portrait = page.locator('.portrait').bounding_box()
    if page.viewport_size['width'] > 600:
        assert portrait['x'] >= content['x'] + content['width'], f'{name}: desktop/tablet portrait overlaps text'
    else:
        assert portrait['y'] >= content['y'] + content['height'], f'{name}: mobile portrait overlaps text'
    links = [link.bounding_box() for link in page.locator('nav a').all()]
    assert all(a['x'] + a['width'] < b['x'] for a, b in zip(links, links[1:])), f'{name}: navigation links crowded/overlapping'
    return state


def main():
    from playwright.sync_api import sync_playwright

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('/tmp/horace-site-review'))
    parser.add_argument('--axe', type=Path, help='Optional path to axe-core/axe.min.js')
    parser.add_argument('--chromium', default=shutil.which('chromium') or shutil.which('google-chrome'))
    args = parser.parse_args()
    output = args.output.resolve()
    assert not output.is_relative_to(ROOT), 'Save generated review artifacts outside the checkout.'
    output.mkdir(parents=True, exist_ok=True)
    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(ROOT)))
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    origin = f'http://127.0.0.1:{server.server_port}'
    report = {'viewports': [], 'accessibility': 'NOT RUN' if not args.axe else 'axe-core', 'base_url': 'local test server'}

    def audit(page, name):
        if not args.axe:
            return
        page.add_script_tag(path=str(args.axe.resolve()))
        result = page.evaluate('''async () => {
          const result = await axe.run(document, {runOnly: {type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21aa', 'best-practice']}});
          return {passes: result.passes.length, violations: result.violations.map(v => ({id: v.id, impact: v.impact, targets: v.nodes.map(n => n.target)}))};
        }''')
        (output / f'{name}-axe.json').write_text(json.dumps(result, indent=2) + '\n')
        assert not result['violations'], f'{name}: accessibility violations: {result["violations"]}'
        return result['passes']

    try:
        with sync_playwright() as p:
            launch = {'headless': True, 'args': ['--no-sandbox']}
            if args.chromium:
                launch['executable_path'] = args.chromium
            browser = p.chromium.launch(**launch)
            report['chromium'] = browser.version
            cases = [('desktop', 1440, 1000), ('small-desktop', 1024, 900), ('tablet', 768, 1024), ('zoom-equivalent', 720, 900), ('mobile', 390, 844), ('small-mobile', 320, 700)]
            for name, width, height in cases:
                page = browser.new_page(viewport={'width': width, 'height': height}, reduced_motion='reduce')
                errors, failed, external, network, console_errors, request_failures = [], [], [], [], [], []
                page.on('pageerror', lambda e: errors.append(str(e)))
                page.on('response', lambda r: failed.append(f'{r.status} {r.url}') if r.status >= 400 else None)
                page.on('response', lambda r: network.append({'url': r.url, 'type': r.request.resource_type, 'status': r.status, 'content_type': r.headers.get('content-type', '')}))
                page.on('console', lambda m: console_errors.append(m.text) if m.type == 'error' else None)
                page.on('requestfailed', lambda r: request_failures.append({'url': r.url, 'error': r.failure}))
                page.on('request', lambda r: external.append(r.url) if not r.url.startswith(origin) else None)
                response = page.goto(origin, wait_until='networkidle')
                assert response.status == 200
                page.evaluate('document.fonts.ready')
                assert page.title().startswith('Hongrui (Horace) Yi')
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), f'{name}: horizontal overflow'
                assert page.evaluate('getComputedStyle(document.documentElement).scrollBehavior') == 'auto'
                page.keyboard.press('Tab')
                assert page.locator('.skip-link').evaluate('(e) => e === document.activeElement'), f'{name}: skip link not first'
                page.keyboard.press('Enter')
                assert page.evaluate('document.activeElement.id') == 'main', f'{name}: skip link did not focus main'
                for link in page.locator('nav a').all():
                    target = link.get_attribute('href')
                    link.click()
                    rect = page.locator(target).bounding_box()
                    header = page.locator('.site-header').bounding_box()
                    assert rect['y'] >= header['height'] - 1 and rect['y'] < height, f'{name}: {target} obscured/offscreen'
                for detail in page.locator('details').all():
                    summary = detail.locator('summary')
                    summary.focus()
                    page.keyboard.press('Space')
                    assert detail.get_attribute('open') is not None, f'{name}: details cannot open by keyboard'
                    page.keyboard.press('Space')
                    assert detail.get_attribute('open') is None, f'{name}: details cannot close by keyboard'
                for img in page.locator('img').all():
                    img.scroll_into_view_if_needed()
                page.wait_for_function('Array.from(document.images).every(i => i.complete && i.naturalWidth > 0)')
                rendered = check_rendering(page, name)
                for resource in network:
                    kind = resource['type']
                    if kind in ['stylesheet', 'image', 'font']:
                        assert resource['status'] == 200, f'{name}: asset failed: {resource}'
                        expected = {'stylesheet': ['text/css'], 'image': ['image/'], 'font': ['font/', 'application/font', 'application/x-font', 'application/octet-stream']}[kind]
                        assert any(resource['content_type'].startswith(t) for t in expected), f'{name}: wrong asset MIME type: {resource}'
                page.evaluate('window.scrollTo({top:0, behavior:"instant"})')
                # Remove focus for editorial screenshots without changing page behavior.
                page.evaluate('document.activeElement.blur()')
                page.mouse.move(0, 0)
                page.screenshot(path=str(output / f'{name}.png'), full_page=True)
                if name in ['desktop', 'mobile']:
                    page.screenshot(path=str(output / f'{name}-hero.png'))
                passed = audit(page, name)
                if name in ['desktop', 'mobile']:
                    page.locator('details').evaluate_all('(items) => items.forEach(e => e.open = true)')
                    audit(page, name + '-expanded')
                    page.locator('details').evaluate_all('(items) => items.forEach(e => e.open = false)')
                if name == 'desktop':
                    page.emulate_media(media='print')
                    page.pdf(path=str(output / 'print.pdf'), format='A4', print_background=True, margin={'top': '12mm', 'right': '12mm', 'bottom': '12mm', 'left': '12mm'})
                assert not errors and not failed and not external and not console_errors and not request_failures, f'{name}: errors={errors}, failed={failed}, external={external}, console={console_errors}, request_failures={request_failures}'
                report['viewports'].append({'name': name, 'width': width, 'height': height, 'axe_passes': passed, 'errors': errors, 'failed_requests': failed, 'external_requests': external, 'console_errors': console_errors, 'request_failures': request_failures, 'network': network, 'rendered': rendered})
                print(f'PASS: {name} ({width}px): applied CSS/fonts, decoded images, layout, keyboard, anchors, reduced motion' + (f', {passed} axe checks / 0 violations' if passed else ''), flush=True)
                page.close()
            page = browser.new_page(viewport={'width': 390, 'height': 844}, java_script_enabled=False, reduced_motion='reduce')
            page.goto(origin, wait_until='networkidle')
            page.locator('nav a[href="#research"]').click()
            assert page.url.endswith('#research')
            page.locator('.research-detail summary').first.click()
            assert page.locator('.research-detail').first.get_attribute('open') is not None
            report['no_javascript'] = 'PASS: navigation and native details'
            print('PASS: navigation and research disclosures with JavaScript disabled')
            page.close()
            page = browser.new_page(viewport={'width': 390, 'height': 844})
            page.goto(origin + '/404.html', wait_until='networkidle')
            assert page.locator('h1').inner_text() == 'A different direction.'
            audit(page, '404')
            page.get_by_role('link', name='Return to the homepage').click()
            assert page.title().startswith('Hongrui (Horace) Yi')
            report['404'] = 'PASS: document, return link (production routing not tested)'
            page.close()
            browser.close()
        (output / 'browser-report.json').write_text(json.dumps(report, indent=2) + '\n')
        print('PASS: custom 404 page and home link; print PDF generated.')
        print(f'Artifacts: {output}')
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


if __name__ == '__main__':
    main()
