#!/usr/bin/env python3
"""Check the static site's links and HTTP responses without external packages."""
from collections import Counter
from functools import partial
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import re
import sys
from threading import Thread
from urllib.parse import unquote, urlsplit
from urllib.request import urlopen
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids, self.refs, self.images, self.labels = [], [], [], []
        self.headings = Counter()
        self.meta, self.links, self.structured = {}, {}, []
        self._json = None
        self.lang = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html':
            self.lang = a.get('lang')
        if 'id' in a:
            self.ids.append(a['id'])
        if tag in ['h1', 'main', 'title']:
            self.headings[tag] += 1
        if tag == 'img':
            self.images.append(a)
        for key in ['href', 'src']:
            if key in a:
                self.refs.append(a[key])
        if 'srcset' in a:
            self.refs.extend(candidate.strip().split()[0] for candidate in a['srcset'].split(','))
        for key in ['aria-labelledby', 'aria-describedby']:
            self.labels.extend(a.get(key, '').split())
        if tag == 'meta':
            self.meta[a.get('name', a.get('property'))] = a.get('content')
        if tag == 'link':
            self.links[a.get('rel')] = a.get('href')
        if tag == 'script':
            assert a.get('type') == 'application/ld+json', 'Unexpected executable script'
            self._json = ''

    def handle_data(self, data):
        if self._json is not None:
            self._json += data

    def handle_endtag(self, tag):
        if tag == 'script' and self._json is not None:
            self.structured.append(json.loads(self._json))
            self._json = None


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


def main():
    pages = {p.relative_to(ROOT).as_posix(): Page(p.read_text()) for p in ROOT.glob('*.html')}
    resources = set(pages)
    external = set()
    fragments = 0

    def resolve(ref, source):
        nonlocal fragments
        assert ref and ref == ref.strip(), f'{source}: empty/whitespace URL: {ref!r}'
        u = urlsplit(ref)
        if u.scheme or u.netloc:
            assert u.scheme in ['https', 'mailto'], f'{source}: insecure/unsupported URL: {ref}'
            assert u.netloc or (u.scheme == 'mailto' and '@' in u.path), ref
            external.add(ref)
            return
        # Paths beginning with / resolve from the custom-domain site root.
        path = ((ROOT / unquote(u.path).lstrip('/')) if u.path.startswith('/')
                else (ROOT / source).parent / unquote(u.path)) if u.path else ROOT / source
        path = path.resolve()
        assert path.is_relative_to(ROOT), f'{source}: path escapes site: {ref}'
        if path.is_dir():
            path /= 'index.html'
        assert path.is_file(), f'{source}: missing file: {ref}'
        rel = path.relative_to(ROOT).as_posix()
        resources.add(rel)
        if u.fragment:
            assert rel in pages and unquote(u.fragment) in pages[rel].ids, f'{source}: missing fragment: {ref}'
            fragments += 1

    for filename, page in pages.items():
        assert page.lang == 'en', f'{filename}: missing document language'
        assert all(page.headings[h] == 1 for h in ['h1', 'main', 'title']), f'{filename}: invalid landmarks/title'
        assert len(page.ids) == len(set(page.ids)), f'{filename}: duplicate IDs'
        assert all(label in page.ids for label in page.labels), f'{filename}: missing accessible label target'
        assert page.meta.get('viewport') and page.meta.get('description'), f'{filename}: missing metadata'
        for img in page.images:
            assert img.get('alt') and int(img.get('width', '0')) > 0 and int(img.get('height', '0')) > 0, f'{filename}: image lacks text/dimensions'
        for ref in page.refs:
            resolve(ref, filename)

    home = pages['index.html']
    assert (ROOT / 'CNAME').read_text().strip() == 'horaceyi.com', 'Custom domain changed'
    assert home.links['canonical'] == home.meta['og:url'] == 'https://horaceyi.com/'
    assert home.meta['og:image'].startswith('https://horaceyi.com/')
    resolve(urlsplit(home.meta['og:image']).path, 'index.html')
    data = home.structured[0]
    assert data['@type'] == 'ProfilePage' and data['mainEntity']['@type'] == 'Person'
    assert data['mainEntity']['url'] == home.links['canonical']
    for ref in re.findall(r'url\([\'"]?([^\)\'\"]+)[\'"]?\)', (ROOT / 'red.css').read_text()):
        resolve(ref, 'red.css')
    sitemap = ET.parse(ROOT / 'sitemap.xml')
    assert [node.text for node in sitemap.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')] == [home.links['canonical']]
    assert 'Sitemap: https://horaceyi.com/sitemap.xml' in (ROOT / 'robots.txt').read_text()
    assert pages['404.html'].meta['robots'] == 'noindex'
    resources.update(['robots.txt', 'sitemap.xml', 'CNAME'])

    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(ROOT)))
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        origin = f'http://127.0.0.1:{server.server_port}'
        for ref in sorted(resources):
            with urlopen(origin + '/' + ref, timeout=5) as response:
                assert response.status == 200 and response.read() == (ROOT / ref).read_bytes(), f'HTTP content mismatch: {ref}'
        with urlopen(origin + '/', timeout=5) as response:
            assert b'Hongrui (Horace) Yi' in response.read(), 'Wrong homepage served'
    finally:
        server.shutdown()
        server.server_close()
        thread.join()
    print(f'PASS: {len(pages)} HTML pages; {fragments} fragment links; {len(resources)} local resources served byte-for-byte.')
    print('PASS: image/srcset and CSS references, metadata, JSON-LD, sitemap, custom domain, and custom error page.')
    print(f'NOT CHECKED: live reachability/bibliographic accuracy of {len(external)} distinct external URLs (including metadata URLs).')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (AssertionError, OSError, ValueError, KeyError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        sys.exit(1)
