# Research and publication refinement

This round refines the approved design on `redesign/academic-portfolio`, based on `05ebbf4`. It preserves the portrait, fonts, palette, responsive breakpoints, asset paths, earlier publications, `CNAME`, and GitHub Pages configuration. No push, merge, or deployment was performed.

## Featured 2025 SPIE paper

The following citation is now the first entry under Selected Publications. The owner supplied every bibliographic field below and explicitly instructed us to use these details if external access remained blocked. It is **owner-confirmed, not independently verified in this environment**.

- **Title:** Kalman filter/deep-learning hybrid automatic boundary tracking of optical coherence tomography data for deep anterior lamellar keratoplasty (DALK)
- **Authors, in the supplied order:** Hongrui Yi; Jinglun Yu; Yaning Wang; Justin Opfermann; Bill G. Gensheimer; Axel Kriger; Jin U. Kang.
- **Publication:** Proceedings of SPIE, Volume 13310, Article 133100A (2025).
- **DOI:** https://doi.org/10.1117/12.3042689
- **arXiv:** https://arxiv.org/abs/2501.15311

The public entry highlights first authorship, includes both supplied links, and connects the OCT-guided microsurgery direction to the paper. No author spelling was silently normalized or inferred. Only the supplied year is shown; an exact publication date was not invented. The paper and its arXiv version are one research output, not two publications.

The 2023 Measurement article and 2022 EMBC paper retain their original titles, author order, links, and authentic figures. Their independent bibliographic checks remain pending under the owner's earlier instruction to retain them.

## Verification limits and pending confirmations

- Crossref title/author/date searches, DOI and IEEE records, and the previously specified JHU faculty destination returned proxy `403 Forbidden` responses. The newly supplied arXiv, laboratory, and Google Scholar URLs were each tried once and also blocked. No repeated retries were made after the owner instructed us to use the supplied information.
- The saved environment policy already lists the previously requested scholarly domains; it does not establish that the running proxy permits those requests. No duplicate network change or credential request was added.
- Other 2025–2026 papers or contributions could not be checked against public records. None were guessed or added. This is an access limitation, not a finding that no other work exists.
- A separate presentations section is deferred: the supplied proceedings citation does not establish an oral/poster format, exact presentation date, or program identifier. Supply those official program details to add a distinct presentation entry without conflating it with a published paper.
- Submitted or under-review manuscripts remain absent. No new acceptance, numerical outcome, award, or confidential manuscript information was added.

Future independent review should compare the complete supplied author spellings/order, title, proceedings volume/article, DOI, and year against the publisher record. Additional recent items need a complete official citation or explicit owner-confirmed metadata before inclusion. No further decision is needed for the supplied 2025 entry in this review branch.

## Profile and biography

- Ph.D. student in Electrical and Computer Engineering at Johns Hopkins University; start August 2025; advisor Professor Jin U. Kang; Intelligent Optical Imaging and Vision Laboratory (iOIV / Kang Lab): retained from the owner's confirmed information.
- The M.S. and undergraduate institutions/degrees remain unchanged. Unsupported exact completion dates were not introduced.
- **Google Scholar:** https://scholar.google.com/citations?user=PC4IGhUAAAAJ — supplied by the owner; added to Contact and JSON-LD. Reachability remains unverified due to the access block.
- **Laboratory publications:** https://ioiv.ece.jhu.edu/publications/ — supplied by the owner; linked from the biography. Its contents could not be inspected here.
- **GitHub:** https://github.com/HoraceYi returned HTTP 200. The profile links to `horaceyi.com`, supporting the existing identity match. Its public bio still says “MS in ECE @ Johns Hopkins University”; the owner may wish to update that separately. No external account was edited.
- **LinkedIn:** the existing URL was retained; access was blocked. No other profile URL was invented.

## Research storytelling and visuals

The homepage now identifies OCT, biomedical imaging, and surgical robotics immediately. The three research directions describe the technical question and approach more directly, with compact textual method sequences. These sequences summarize research methods; they are not fabricated experimental figures or claims of measured performance.

No suitable OCT, light-transport, or sweat-imaging figures exist in the checkout. The existing diagrams belong to the earlier signal-processing and lung-ablation papers and remain with those papers. To add authentic visuals, provide the following with a caption, source, and permission for public display:

1. **OCT-guided microsurgery:** a publicly approved corneal OCT B-scan with a boundary overlay, or paired frames illustrating the tracking task; preferably a figure from the 2025 paper that is cleared for reuse.
2. **Computational OCT:** a corneal light-transport/model schematic or an approved synthetic OCT example with the relevant labels and explanation. Do not supply unreleased numerical results for public use.
3. **AI image analysis:** a representative sweat-gland or droplet image paired with its segmentation mask, with any identifying information removed and public-use permission established.

The portrait and all original/optimized research images are unchanged. No placeholder scientific imagery was added.

## Validation and review artifacts

- `python3 scripts/check_site.py`: 2 HTML pages, 10 fragment links, 13 byte-verified local resources; passed.
- `html-validate index.html 404.html`: passed.
- Chromium checks at 1440, 1024, 768, 720, 390, and 320px: applied CSS, loaded fonts, decoded images, resource MIME types, layout, keyboard operation, navigation, and reduced motion passed. No console errors, failed asset requests, or external page requests.
- axe-core: 38 passing rules and zero violations in each of the six homepage viewport runs; expanded disclosures and the custom error page passed as well.
- A separate browser check compared the new title, all seven authors in order, year, volume/article text, DOI, arXiv URL, and Scholar URL exactly against the owner's supplied strings. It also confirmed that all three papers remain and that the SPIE entry is first.
- Existing CSS/asset serving, `CNAME`, `_config.yml`, portrait, fonts, and earlier figures were preserved; no deployment validation is claimed.

Fresh screenshots, network/rendering reports, and a print preview are under `/workspace/horace-refinement/preview/`. `/workspace/horace-refinement/screenshot-review.html` embeds the desktop/mobile captures and the updated publication section in one self-contained review file, avoiding the prior missing-sibling-assets problem in file previews.
