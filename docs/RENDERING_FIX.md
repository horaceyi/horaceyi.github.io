# File-preview diagnosis and hero correction

The reported “Index” preview showed unstyled HTML, a broken portrait, and a joined English/Chinese heading. The user identified this as a Codex file preview rather than the HTTP-served site.

## Findings before changing the website

- No HTTP preview server was running on port 8000 in the current instance. Started Python's static server with its directory explicitly set to `/workspace/horaceyi.github.io`.
- Both the root page and `/index.html` loaded the existing stylesheet, both WOFF2 fonts, and the existing optimized portrait successfully. The browser computed a grid hero and flex navigation; no asset request failed.
- A controlled reproduction served the same HTML alone at `/review/index.html`, without sibling resources at that path. The browser requested `/review/red.css` and `/review/assets/...`; these returned 404. This reproduced the unstyled layout and broken portrait. The internal Codex preview URL was not available for direct inspection, so these are reproduction logs, not a claim to have inspected Codex's own Network panel.
- The original heading's actual DOM text was `Hongrui YiHorace / 易弘睿`: the nickname and Chinese text were nested immediately after the name and depended on CSS to look separate. This was an independent markup defect.

The asset files, filename capitalization, relative paths, and CSS font URLs were correct when the directory was served together. No production asset paths were rewritten, and no portrait was replaced or fabricated.

## Minimal changes

- `index.html`: the English `<h1>` now reads exactly **Hongrui (Horace) Yi**, including whitespace. The Chinese name is a separate paragraph with a Chinese language attribute.
- `red.css`: small name-specific rules keep the longer name legible and prevent the ending from breaking awkwardly; the mobile heading size accommodates the full name.
- `scripts/check_browser.py`: checks actual stylesheet rules, computed grid/flex layout, separate name text, decoded image dimensions, loaded fonts, navigation spacing, CSS/image/font MIME types, console errors, and transport failures. Network records and rendering state are saved alongside screenshots.
- `README.md`: distinguishes an isolated file preview from HTTP serving. The stylesheet, font, image paths, portrait assets, `CNAME`, and GitHub Pages configuration are otherwise unchanged.

## Verification

Actual Chromium rendering passed at **1440px, 768px, and 390px**, plus the existing 1024px, 720px, and 320px checks. Screenshots were taken after font loading and after every lazy image had decoded. There were no overlapping navigation links, horizontal overflow, missing images, console errors, failed asset responses, or external page requests.

The running port-8000 server was also inspected separately: document, CSS, two fonts, portrait, favicon, and both publication figures all returned HTTP 200 with the expected MIME types. Fonts were loaded and image decoding succeeded. There is no application JavaScript dependency; native navigation and disclosures passed with JavaScript disabled.

Two negative controls deliberately blocked the stylesheet and portrait. The new rendering checks rejected each failure, showing that unstyled HTML or alt text alone cannot pass the visual-readiness checks.

- `python3 scripts/check_site.py`: passed, including 2 pages, 9 fragment references, and 13 local resources served byte-for-byte.
- `html-validate index.html 404.html`: passed.
- Browser/axe run: all six widths passed; each homepage run had 37 passing axe rules and zero violations. Expanded details and the custom error page also passed.
- `git diff --check`: passed. `CNAME` and the original/optimized photo assets are unchanged.

## Fresh review artifacts

The latest artifacts are outside the checkout under `/workspace/horace-render-fix/`:

- `fresh/desktop-hero.png`, `fresh/desktop.png`
- `fresh/mobile-hero.png`, `fresh/mobile.png`
- `fresh/tablet.png` and the additional viewport captures
- `fresh/browser-report.json`, per-view accessibility reports, and `fresh/print.pdf`
- `http-server-after.json`: actual port-8000 response and rendering evidence
- `site-root-before.json`, `index-file-before.json`, `isolated-file-preview-before.json`: baseline and controlled reproduction evidence
- `screenshot-review.html`: actual fresh screenshots embedded in one review document. It was tested in an isolated preview path and loads all five images without sibling CSS/font/image requests. This is a screenshot gallery, not a production page or deployment.

No push, merge, deployment, DNS change, or GitHub Pages publishing change was performed. Review remains on the local `redesign/academic-portfolio` branch.
