---
id: note-oreilly-submission-references
title: "O'Reilly Submission — References Review"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [oreilly, submission, references]
refs: [article-submission.md, ../article/review/citation-review.md]
---

Nine sources, all carried from `draft-v2.md` and re-checked here for
publication readiness. No claim was changed; only presentation format
was adjusted (numbered `[n]` markers converted to inline hyperlinks or
short inline attributions, per the link-review recommendation below).

## Per-source check

| Source | Supports which article claim | Primary/authoritative? | Publication-ready format |
|---|---|---|---|
| Kubernetes, "Admission Controllers Reference" | Kubernetes admission control as existing prior art for the gate pattern | Yes — official project documentation | Inline hyperlink on first mention |
| OASIS, XACML 3.0 | PDP/PEP pattern as existing prior art | Yes — official standard | Inline hyperlink on first mention |
| in-toto | Supply-chain attestation as existing prior art | Yes — official project site | Inline hyperlink on first mention |
| SLSA | Supply-chain attestation as existing prior art | Yes — official project site | Inline hyperlink on first mention |
| Buneman, Khanna, Tan, "Why and Where," ICDT 2001 | Database-provenance theory predates general-purpose provenance standards | Yes — primary academic source (previously verified elsewhere in this research programme, `contribution-03/source-ledger.md` S16) | Short inline attribution + end-list entry (no stable public URL confirmed this session; not required for a practitioner piece) |
| W3C, PROV-DM | The consumption-relation concept already exists in provenance standards | Yes — W3C Recommendation | Inline hyperlink on first mention |
| OpenTelemetry, "Traces" | Distributed tracing's parent-span pattern as existing prior art | Yes — official project documentation | Inline hyperlink on first mention |
| Fowler, "Event Sourcing" | Event-sourcing's optional consumption-recording pattern | Yes — standard, widely-cited reference for this pattern | Short inline attribution + end-list entry |
| Carlan et al., "Dynamic Safety Cases for Frontier AI," arXiv:2412.17618 | Dynamic/continuous assurance cases as the closest prior-art collision | Yes — primary source, verified via direct arXiv fetch in the prior review round | Short inline attribution + end-list entry (arXiv link available, included) |

## Accuracy check

All nine sources support exactly the claim attached to them in the
article text — none is over-extended beyond what it actually
establishes (matching the discipline already applied in Article 2's own
citation practice: e.g., Fowler's source supports the *existence* of the
event-sourcing pattern, not this programme's own "values vs.
identifiers" finding, which the article correctly does not attribute to
Fowler).

## Format recommendation implemented

O'Reilly practitioner articles typically favor inline hyperlinks on
first mention over academic-style bracketed numbered citations, which
read as research-note formatting rather than a readable technical
essay. `article-submission.md` implements this: web-linkable sources
(Kubernetes, XACML, in-toto, SLSA, PROV-DM, OpenTelemetry) are inline
hyperlinks at first mention, with a short "Further reading" list at the
end for anyone who wants the full citation; the three sources without a
convenient single canonical URL (Buneman et al., Fowler, Carlan et al.)
use a short inline attribution (author, year) plus the same end-list
entry. No numbered bracket markers (`[1]`, `[2]`...) remain in the
submission copy.

## Not recommended

Adding a full academic bibliography, DOIs, or a formal citation format
(APA/MLA/etc.) — this would work against O'Reilly's practitioner
register and isn't required by anything found in `oreilly/submission/
CURRENT-OREILLY-ROUTE.md`. The current "Further reading" list format is
recommended as final unless an editor requests otherwise.

## Link check

All hyperlinked URLs are the same ones already used, unmodified, in
`draft-v2.md`'s References section — no new URLs were introduced beyond
what was already reviewed and accepted in that document. Live-link
verification (confirming each URL currently resolves) was not performed
in this session and should be done once, close to actual submission —
flagged in `PUBLICATION-QA.md`, not treated as blocking here since the
URLs are unchanged from the already-accepted draft-v2.
