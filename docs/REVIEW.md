# Redesign review — October 2026

Prepared on the local branch `redesign/academic-portfolio`, based on `c055261`. No remote push, pull request, merge, production-branch change, domain change, or deployment has been performed. This document is excluded from the default GitHub Pages build by `_config.yml`.

## What changed

- Replaced the table-based layout with semantic, responsive HTML and a restrained navy/light-neutral design. Self-hosted Manrope and Newsreader fonts provide a consistent typographic hierarchy without third-party font requests.
- Updated the identity, biography, research focus, Ph.D. start date, advisor, and laboratory using the owner's supplied October 2026 information.
- Organized the page into an introduction, biography, three current research directions, journal/conference publications, education, earlier experience, and contact. Research descriptions disclose methods and scope, not unpublished outcomes.
- Preserved the two original citations and author order with the owner's explicit permission. They remain **pending independent bibliographic verification**, not represented as newly verified additions.
- Preserved the original portrait, publication figures, and legacy assets. The page uses optimized derivatives and does not invent OCT figures or a new portrait.
- Removed the missing CV download, obsolete scrolling news, decorative institution-logo tables, personal friend links, icon-based contact clutter, and the third-party ClustrMaps tracking script. Legacy files remain in Git, and earlier research and teaching remain accessible through native disclosures.
- Added responsive images, explicit image sizes, lazy-loaded publication figures, keyboard-visible focus, a skip link, accessible disclosures, reduced-motion support, print styles, a custom 404 document, metadata, JSON-LD, robots.txt, and a sitemap.
- Preserved `CNAME` byte-for-byte as `horaceyi.com`; no hosting or DNS setting was changed. Added only file exclusions to the default GitHub Pages configuration. There is no application build or client-side JavaScript dependency.

## Audit of the original site

| Finding | Resolution |
| --- | --- |
| Identity still described an M.S. student; news stopped at 2023 | Replaced with the owner-provided Ph.D. status and August 2025 start |
| No viewport metadata; wide layout tables and fixed-width logos | Replaced with responsive grid/flex layouts and semantic landmarks |
| Homepage portrait loaded 17,479,884 bytes | Added 480px / 800px WebP derivatives of 29,632 / 69,872 bytes; original untouched; derivative EXIF removed |
| Original publication figures totaled 810,241 bytes | Display derivatives total 71,708 bytes; originals untouched |
| Original favicon was 270,398 bytes | Added a 2,962-byte 32px PNG derived from the existing icon |
| Missing `assets/pdf/CV.pdf` | Removed all download references; owner explicitly requested omission |
| `hanwu.website/` interpreted as a local path | Removed the non-research friends section, including this broken reference |
| Malformed markup, obsolete tags, and layout-only tables | Rebuilt the HTML and validated both public HTML documents |
| Heading styles, no skip link, missing image descriptions, hover-only cues | Added semantic hierarchy, alt text, focus states, and keyboard-operable controls |
| Third-party visitor widget and no social/canonical metadata | Removed the widget; added canonical, OG/Twitter and Person/ProfilePage data |
| No dependency manifests, lockfiles, CI, or site build instructions | Kept static hosting and documented local development/checks; no deployment automation added |
| Python 2 `jemdoc.py`, no `.jemdoc` inputs, unused `jemdoc.css` | Retained for history and excluded from the published output |

## Content provenance and open editorial items

| Material | Source and decision |
| --- | --- |
| Hongrui / Horace / 易弘睿, current JHU Ph.D. position, August 2025 start, advisor, laboratory | Owner's supplied request; used as authorized biographical information, not claimed as independently checked |
| OCT/DALK, Kalman/deep-learning tracking, corneal scattering/attenuation, MCML, inverse estimation, U-Net/sweat imaging, high-resolution/3D/4D imaging | Owner's supplied research scope; presented without numeric results, acceptance claims, or undisclosed manuscript details |
| M.S. at JHU; undergraduate institutions and mechanical engineering degrees | Owner's request and original website; degree names retained, exact completion dates omitted because the legacy page contains inconsistent date information |
| University of Alberta / SJTU experience and teaching | Original website; retained in compact form with years, no new role or award added |
| Existing portrait and publication diagrams | Original tracked assets; only resizing, format conversion, and metadata removal were applied |
| `hyi13@jhu.edu`, GitHub, LinkedIn | Original website; retained. Please confirm the email and professional profile destinations remain current. No Google Scholar, ORCID, project code, or lab URL was invented. |
| GPA, honors, scholarships, and fellowship language on the old page | Not newly asserted. Legacy text remains in Git history at the base commit; confirm which items and supporting dates should return to the visible profile. |
| New conference contributions, manuscripts, and research figures | Held out of the public page until official records and permission to disclose are provided. No confidential manuscript title, venue/status, result, or unreleased figure is embedded in the HTML or metadata. |

### Retained citations — verification pending

The owner chose to retain these existing entries and flag them here. Source: the original `index.html` at `c055261`. Their title, author order, venue and year were transcribed, not embellished. A DOI has **not** been guessed for the IEEE paper.

1. **Hongrui Yi**, Quanchang Li, Hao Wang, Jian Tang, Rui Liu, Wenbin Huang, Xiaoxi Ding. “Dual-kernel driven convolutional sparse learning for bearing transient feature enhancement.” *Measurement*, 2023. Existing DOI: https://doi.org/10.1016/j.measurement.2023.112643.
2. Haoyu Wang, **Hongrui Yi**, Jie Liu, Lixu Gu. “Integrated Treatment Planning in Percutaneous Microwave Ablation of Lung Tumors.” *International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)*, 2022. Existing IEEE record: https://ieeexplore.ieee.org/document/9871915.

Attempts to retrieve the DOI resolver, Crossref work/search endpoints, IEEE Xplore, SPIE Digital Library, JHU faculty page, and the previous Alberta profile all received proxy `403 Forbidden` responses. This is a network access limitation, not proof that a link is dead or a citation is correct. No TLS or verification checks were disabled. Live source checks need to be repeated after the relevant environment network change is applied.

Seven domains were added to the environment configuration **draft**, preserving its existing package-manager preset and other settings: `api.crossref.org`, `doi.org`, `www.spiedigitallibrary.org`, `spie.org`, `ieeexplore.ieee.org`, `engineering.jhu.edu`, `www.ncbl.ualberta.ca`. Saving the draft does not apply runtime networking or publish anything. External GitHub/LinkedIn/JHU profile reachability and production DNS/TLS have not been claimed as validated.

Before adding the 2025 SPIE contribution, obtain the official record confirming title, full author order, presentation format, date, and DOI if assigned. Before adding either 2027 contribution, confirm its official title, authorship, format, acceptance evidence, and permission to disclose. No new accepted-contribution or manuscript section is shown merely to fill space. A new CV and publicly approved research visuals can be added later; neither is needed to publish the current layout after approval.

## Validation evidence

Run the commands from the repository root. Generated screenshots/reports are outside the checkout at `/workspace/horace-site-review/`.

| Check | Result |
| --- | --- |
| `python3 scripts/check_site.py` | Passed: 2 HTML documents, 9 fragment references, 13 local resources returned byte-for-byte; local links, srcset, CSS fonts, metadata, JSON-LD, sitemap, robots, and CNAME checked |
| `html-validate index.html 404.html` | Passed with the recommended configuration; no errors or warnings |
| Chromium through Python Playwright | Passed at 1440, 1024, 768, 720, 390, and 320 CSS pixels; no horizontal overflow, missing image, page error, failed asset response, or external page request |
| Keyboard and local navigation | Passed: skip link focuses main, each navigation anchor remains visible below the sticky header, all four disclosures open/close with Space |
| JavaScript-disabled context | Navigation and research disclosures passed without JavaScript |
| axe-core automated accessibility | 0 violations for WCAG 2 A/AA, WCAG 2.1 AA, and best-practice tags across 6 viewport runs; 37 passing rules each. Expanded disclosures also passed at desktop/mobile; 404 document passed 27 rules. This does not imply full manual WCAG certification. |
| Reduced motion | Verified computed smooth scrolling is disabled when requested |
| Reflow/zoom-equivalent layout | 720px viewport covers the layout equivalent of 200% zoom on a 1440px-wide desktop; 320px reflow checked separately. Actual browser text-only zoom and screen-reader use were not tested. |
| Print | Print PDF generated and preview checked; it is a site printout, not a replacement CV |
| GitHub Pages/custom domain | CNAME unchanged and static output compatible by inspection; no production deployment, new-task snapshot restoration, DNS/TLS check, or hosted Jekyll build was run |
| External scholarly links and new publication metadata | Blocked by network policy; distinct from local site validation. Existing entries retained with owner's consent. |

Tools used: Python 3.12.14, Chromium 154.0.8037.57, axe-core 4.14.0, html-validate 11.16.4. See the browser report for the exact Chromium version of the delivered run; the website itself has no tool dependencies.

Review artifacts: `desktop-hero.png`, `desktop.png`, `mobile-hero.png`, `mobile.png`, tablet/small-screen images, `print.pdf`, `browser-report.json`, and per-run `*-axe.json` files. Lazy-loaded figures were explicitly loaded before screenshots.

## Changed files

- Rewritten: `index.html`, `red.css`.
- Added site support: `404.html`, `robots.txt`, `sitemap.xml`, `_config.yml`.
- Added documentation/tooling: `README.md`, `docs/REVIEW.md`, `scripts/check_site.py`, `scripts/check_browser.py`, `.gitignore`.
- Added optimized assets: `assets/img/portrait-480.webp`, `assets/img/portrait-800.webp`, `assets/img/dkcsl.webp`, `assets/img/iap.webp`, `assets/img/favicon-32.png`.
- Added self-hosted typography: `assets/fonts/manrope-latin-wght-normal.woff2`, `assets/fonts/newsreader-latin-wght-normal.woff2`, and the two `*-OFL.txt` license files from Fontsource Variable 5.3.0.
- Unchanged: `CNAME`, original photos/figures/logos, original `jemdoc.py`, `jemdoc.css`, and the existing PDF directory.

## Review and release

Inspect `git diff c055261...redesign/academic-portfolio` and the local preview artifacts. The current design/content can be reviewed independently of the pending new scholarly entries. Confirm contact details, retained citations, and any desired legacy honors; provide public records/assets for future additions. **Pushing, merging, and deployment require owner approval.** No remote PR is claimed; the review branch and commit are local.
