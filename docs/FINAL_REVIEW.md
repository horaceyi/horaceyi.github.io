# Final publication refinement and release review

This final round preserves the approved visual design and adds the owner-supplied second-author SPIE 2025 paper. Both SPIE papers precede the 2023 Measurement article and the 2022 EMBC paper. The first-author work remains visually featured; the second uses a restrained text entry. No portrait, research figure, font, responsive breakpoint, domain setting, or publishing workflow was changed.

## Added citation

**Title:** Topology-based deep-learning segmentation method for deep anterior lamellar keratoplasty (DALK) surgical guidance using M-mode OCT data.

**Authors, supplied order:** Jinglun Yu; Hongrui Yi; Yaning Wang; Justin D. Opfermann; William G. Gensheimer; Axel Krieger; Jin U. Kang.

**Venue:** Proceedings of SPIE, Vol. 13310, Article 1331003 (2025).

**DOI:** https://doi.org/10.1117/12.3042615

**Owner-supplied institutional reference:** https://pure.johnshopkins.edu/en/publications/topology-based-deep-learning-segmentation-method-for-deep-anterio/

The title, author order, volume/article, year, and links were transcribed from the owner's request. Source access is blocked in this environment; the entry is not represented as independently verified here.

## First-paper author spelling — owner confirmed against the JHU record

The owner supplied the official institutional record for DOI `10.1117/12.3042689` and confirmed its author order: **Hongrui Yi, Jinglun Yu, Yaning Wang, Justin Opfermann, Bill G. Gensheimer, Axel Kriger, Jin U. Kang**.

Official record: https://pure.johnshopkins.edu/en/publications/kalman-filterdeep-learning-hybrid-automatic-boundary-tracking-of-/

The confirmed first-paper spellings **Justin Opfermann**, **Bill G. Gensheimer**, and **Axel Kriger** are preserved exactly. The second paper keeps its different spellings **Justin D. Opfermann**, **William G. Gensheimer**, and **Axel Krieger**. The first paper's supplied volume, article, year, and DOI also match the owner's confirmation. Both entries link to their respective institutional records. The discrepancy is resolved by the owner's record confirmation; access from this environment remains blocked, so independent retrieval is not claimed.

## Figures

No suitable, publicly reusable OCT research figure is available in the checkout. Existing figures are specific to the earlier publications and remain with those papers. The two SPIE entries preserve the current text-based presentation; no scientific image was fabricated or borrowed without reuse permission.

## Final validation

- Local static-site check passed: 2 HTML documents, 10 fragment references, and 13 local resources served byte-for-byte, including CSS/font/image references, metadata, canonical URL, sitemap, and CNAME.
- HTML validation passed for both public HTML documents; `git diff --check` passed.
- Chromium rendering passed at 1440, 1024, 768, 720, 390, and 320px. Checks cover applied CSS, loaded fonts, decoded images, asset MIME types, navigation spacing, no horizontal overflow, keyboard behavior, reduced motion, and no console/network failures.
- axe-core returned zero violations and 38 passing rules per homepage viewport; expanded content and the custom error document passed as well.
- A separate browser check confirmed four papers remain, the first and second entries are the two SPIE 2025 papers, and the new title, all seven authors in order, volume/article/year, DOI, and emphasized second author match the supplied citation.
- The current publication section was captured from the actual HTTP-served page for visual review. Fresh screenshots and browser/network reports are under `/workspace/horace-final-review/preview/`; an embedded screenshot review is saved alongside them.

## External links and hosting

External web destinations were checked, with the first paper's institutional URL added after the owner supplied it. GitHub returned HTTP 200. DOI links, arXiv, the lab, Google Scholar, LinkedIn, JHU, the institutional host, IEEE, and the production domain returned proxy tunnel `403 Forbidden` errors. These are access restrictions, not evidence that those destinations are broken. No credential values were printed and no TLS verification was disabled. Results and access limitations are saved in `/workspace/horace-final-review/external-links.json`.

`CNAME` remains byte-identical as `horaceyi.com`; canonical and sitemap URLs agree. `_config.yml` is unchanged, and maintenance/review files remain excluded from the default GitHub Pages Jekyll output. There are no repository deployment workflows. Remote GitHub Pages source settings and live DNS/TLS could not be verified through the blocked GitHub API/domain access; no hosted build or deployment has been claimed.

## PR preparation and remaining prerequisites

Native Git read access to the origin succeeds, and a `GH_TOKEN` binding is already present. GitHub CLI API requests and an unauthenticated public API check both fail at the proxy tunnel for `api.github.com`, before an API response can establish token scope. A missing or invalid token has not been inferred; no duplicate credential was requested.

The environment draft preserves its existing domain rules and adds the GitHub API and remaining review destinations: `api.github.com`, `arxiv.org`, `ioiv.ece.jhu.edu`, `pure.johnshopkins.edu`, `scholar.google.com`, `www.linkedin.com`, `www.jhu.edu`, `horaceyi.com`. Saving this draft does not apply runtime networking or publish the website. Review/save these settings and publish the **environment** to activate them, then retry API and source verification; this is separate from approving website deployment.

The PR title and full description are prepared outside the checkout at `/workspace/horace-final-review/PR_BODY.md`. Branch publication and remote PR status are reported separately in the task's final response; this file does not claim that a PR exists.

The local website is technically validated, and both SPIE author lines are confirmed by the owner against their records. External link/hosting checks remain restricted by environment access, so an unconditional production verification claim is not made. Merge and deployment require the owner's approval.
