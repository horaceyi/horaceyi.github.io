# IEEE TBME 2026 publication update

Added the owner-supplied journal paper to Selected Publications using the existing featured-paper styling. The 2026 journal article appears first, followed by the prominently featured first-author SPIE 2025 paper. Hongrui Yi is labeled **Fourth author** on the TBME article and **First author** on the featured SPIE paper. The second SPIE paper and both earlier publications are preserved.

## Citation and provenance

**Title:** Autonomous OCT-Guided Robotic System for Vertical Needle Insertion and Big-Bubble Dissection in Corneal Transplantation

**Authors in supplied order:** Yaning Wang; Justin D. Opfermann; Jinglun Yu; Hongrui Yi; James Kaluna; Rishi Biswas; Ruizhi Zuo; William Gensheimer; Axel Krieger; Jin U. Kang.

**Journal/year:** IEEE Transactions on Biomedical Engineering (2026).

- DOI: https://doi.org/10.1109/TBME.2026.3681869
- Official JHU record: https://pure.johnshopkins.edu/en/publications/autonomous-oct-guided-robotic-system-for-vertical-needle-insertio/
- PubMed: https://pubmed.ncbi.nlm.nih.gov/41945802/

All three links are included in the public entry. The citation uses the owner's complete supplied metadata. Each destination was tried once and returned a proxy tunnel `403 Forbidden`, so independent retrieval is not claimed. No volume, issue, page range, precise publication date, or individual technical contribution was inferred. Paper-specific author spellings remain distinct across the TBME and SPIE entries.

## Scope and validation

- Reused the approved typography, palette, and featured-paper styles; no stylesheet, portrait, research image, font, responsive breakpoint, domain setting, or GitHub Pages configuration was changed.
- Added a related-paper anchor from the OCT-guided microsurgery research direction to the TBME entry, alongside its existing SPIE link.
- Retained all four previous publication entries byte-for-byte, including their author lists, links, and figures.
- Standard-library site check passed: 2 HTML pages, 11 fragment references, and 13 local resources served byte-for-byte. HTML validation and `git diff --check` passed.
- Actual Chromium rendering passed at 1440, 1024, 768, 720, 390, and 320px, including CSS/fonts/images, network/console checks, layout, keyboard navigation, reduced motion, and JavaScript-disabled operation. Automated axe checks returned zero violations and 38 passing rules per homepage viewport.
- A focused browser check compared the new title, all ten authors, fourth-author label and emphasis, journal/year, DOI, JHU URL, and PubMed URL to the supplied citation. Five papers are present and the two requested entries use the featured style.
- Screenshots and browser reports are saved under `/workspace/horace-tbme-review/preview/`; the self-contained review file is `/workspace/horace-tbme-review/screenshot-review.html`.

The pre-existing GitHub API restriction also blocked checking remote PR status. The review branch can still be updated through native Git; no PR existence or API update is inferred from a branch push. No merge or deployment is authorized or performed.
