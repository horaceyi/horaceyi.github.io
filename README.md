# Hongrui Yi — academic website

A responsive, static academic portfolio for **Hongrui (Horace) Yi**, hosted with GitHub Pages at **https://horaceyi.com/**. No package manager, JavaScript runtime, or build step is required to edit or serve the website.

## Local development

Use the existing checkout; cloud tasks are already isolated. Do not create a Git worktree unless explicitly requested.

```sh
cd /workspace/horaceyi.github.io
python3 -m http.server 8000 --bind 127.0.0.1
```

Use local HTTP requests or a browser in your development environment to inspect the site. The server must be started again in a new task; running processes do not survive snapshots.

Open the HTTP-served site for visual review. A Codex file preview labeled “Index” may render the HTML without its sibling stylesheet, fonts, or images; that is not the same as serving this directory. Keep `index.html`, `red.css`, and `assets/` together. Relative URLs intentionally support both the site root and a containing directory. Do not rewrite working asset paths just to accommodate an isolated file preview.

## Files and editing

| File | Purpose |
| --- | --- |
| `index.html` | All visible content, navigation, SEO metadata, and JSON-LD |
| `red.css` | Design tokens, reusable layouts, responsive and print styles; filename retained from the original site |
| `assets/img/portrait-*.webp` | Optimized versions of the original `bio.JPG`, with metadata removed |
| `assets/img/dkcsl.webp`, `assets/img/iap.webp` | Optimized versions of the existing publication figures |
| `assets/fonts/` | Locally hosted Manrope and Newsreader variable fonts and OFL licenses |
| `404.html` | Custom GitHub Pages error page |
| `CNAME` | Custom domain, `horaceyi.com`; preserve this file |
| `robots.txt`, `sitemap.xml` | Search-engine discovery |
| `_config.yml` | Excludes development/review files from the default GitHub Pages Jekyll output |
| `scripts/` | Optional local quality checks; not website dependencies |
| `docs/REVIEW.md` | Audit, content provenance, and outstanding editorial review |

Edit the clearly marked sections in `index.html`. Research projects are grouped under `#research`; papers under `#publications`; education and earlier experience under `#background`. Keep section IDs stable because navigation and external bookmarks use them. Native `<details>` elements provide keyboard-operable technical notes without JavaScript.

When changing the biography, also update the title, description, Open Graph/Twitter metadata, JSON-LD, and footer update date. Keep canonical, Open Graph URL, sitemap, and CNAME consistent with the production domain. Do not put private editorial notes in HTML comments or structured data.

### Research and publications

- Publish only owner-authorized research descriptions; do not infer experimental results, performance metrics, or manuscript status.
- For each new paper, verify the complete title, author order, venue, year, publication status, and DOI or official record. Highlight Hongrui Yi in the author list.
- Separate journal articles, conference papers, accepted presentations, and explicitly authorized preprints/manuscripts. Acceptance of an abstract is not publication of a paper.
- The two existing citations are retained with the owner's permission; independent metadata verification remains pending. See `docs/REVIEW.md` before adding new entries.
- There is intentionally no CV link. Add one only if an actual, public, current PDF is provided and checked.
- Do not relabel earlier publication figures as OCT research images. Retain provenance and meaningful alt text for every image.

### Images and fonts

The original portrait and figures remain untouched. The website loads only the optimized WebP derivatives. Keep explicit image dimensions, responsive `srcset` for the portrait, and lazy loading for below-the-fold figures. The portrait is not lazy-loaded. Use photographs/figures with appropriate rights and public-disclosure permission; never synthesize a portrait or experimental figure.

Manrope and Newsreader are from the corresponding **Fontsource Variable 5.3.0** npm packages; only the Latin normal variable WOFF2 subsets are served. Each font's OFL license is retained beside it. There are no third-party font requests, analytics, or application scripts. Decorative arrows use inline SVG so they do not depend on a font's glyph coverage. The old unused icons, `jemdoc.css`, and Python 2 `jemdoc.py` remain for historical preservation; they are not part of the current workflow.

## Checks

The standard-library check starts and stops its own local HTTP server and validates every page's local references, fragments, responsive image candidates, CSS resources, metadata, structured data, and served resource bytes:

```sh
python3 scripts/check_site.py
```

Optional browser verification (requires `playwright` for Python and Chromium, already present in this cloud environment):

```sh
python3 scripts/check_browser.py --output /tmp/horace-site-review
```

It verifies applied stylesheet rules, decoded images, loaded fonts, resource MIME types, console/network errors, layout from 320px to 1440px, keyboard behavior, navigation destinations, a 200% zoom-equivalent viewport, reduced motion, and print rendering. The exact English hero name and separate Chinese name are checked as rendered DOM text. It saves screenshots plus network/rendering evidence outside the checkout. To include an axe accessibility scan, supply a locally installed `axe-core/axe.min.js` with `--axe /path/to/axe.min.js`. Development-only tools can be installed outside the repository:

```sh
npm install --prefix /tmp/horace-tools --no-audit --no-fund axe-core@4.14.0 html-validate@11.16.4
/tmp/horace-tools/node_modules/.bin/html-validate index.html 404.html
python3 scripts/check_browser.py --output /tmp/horace-site-review --axe /tmp/horace-tools/node_modules/axe-core/axe.min.js
```

The exact tool versions used for the delivered review are recorded in `docs/REVIEW.md`. Automated accessibility checks do not replace a screen-reader review. External scholarly/profile URLs require live network access and are distinct from the deterministic local checks.

## GitHub Pages and review

Keep the current Pages publishing source and custom-domain settings. No new deployment workflow is introduced. The default GitHub Pages Jekyll build reads `_config.yml`; if switching to a different uploader or disabling Jekyll, preserve the exclusions so maintenance documents and scripts are not published. Python's local server serves files directly and does not apply these publication exclusions or route unknown URLs to `404.html`.

Work is prepared on a local review branch. **Do not push to the production branch, merge, or deploy without the owner's approval.** A local preview or commit does not update the live website. Review the diff, editorial checklist, and validation evidence before authorizing publication.
