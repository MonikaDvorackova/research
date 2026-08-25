---
id: note-oreilly-article-citation-review
title: "O'Reilly Article draft-v1 — Citation Traceability"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [oreilly, article, review, citations]
refs: [../draft-v1.md]
---

## Cited sources (four)

| # | Sentence/section | Source | Status | Notes |
|---|---|---|---|---|
| [1] | Section 6: "W3C's own provenance data model (PROV-DM) already distinguishes an entity's own attributes from the `used` relation..." | W3C PROV-DM, 2013 | **PASS** | Accurate, matches PROV-DM's actual `used` relation; reused verbatim from Article 2's already-verified reference list. |
| [2] | Section 6: "Distributed tracing systems capture parent-span relationships..." | OpenTelemetry Traces docs | **PASS** | Accurate description of span parent-child relationships; reused from Article 2. |
| [3] | Section 6: "Event-sourcing architectures already have the option to record which prior event a later one consumed..." | Fowler, "Event Sourcing," 2005 | **PASS** | Correctly attributes only the pattern's existence, not the "values vs. identifiers" finding (which is this programme's own, not Fowler's) — same discipline Article 2's own citation audit already confirmed. |
| [4] | Section 6: "dynamic and continuous assurance cases... applied specifically to frontier AI systems..." | Carlan et al., "Dynamic Safety Cases for Frontier AI," arXiv:2412.17618, 2024 | **PASS, with a flagged gap** | Title and lead author verified this session (per `editorial-notes.md`); full co-author list not independently confirmed, citation correctly uses "et al." rather than inventing names. **NEEDS CITATION completion** before external publication — re-fetch the primary source directly to confirm the full author list. |

## Uncited factual prior-art claims

| Claim | Location | Currently cited? | O'Reilly-style requirement | Verdict |
|---|---|---|---|---|
| "Admission controllers in Kubernetes block a pod from starting until policy checks pass" | Section 3, line 47 | No | O'Reilly practitioner pieces do not require academic-style citations for widely-known platform behavior, but a link improves reader trust and costs nothing | **NEEDS CITATION** (link to Kubernetes admission-controller docs) |
| "Policy decision points and policy enforcement points (the PDP/PEP pattern from access-control systems)" | Section 3, line 47; Section 6, line 79 | No | PDP/PEP is a named, decades-old access-control pattern (e.g., XACML); a reader unfamiliar with the term benefits from a link | **NEEDS CITATION** (a general XACML/PDP-PEP reference) |
| "Software supply-chain frameworks like in-toto and SLSA gate a build's promotion on signed, checkable attestations" | Section 3, line 47 | No | Both are named, specific, citable projects with authoritative documentation | **NEEDS CITATION** (in-toto and SLSA project sites) |
| "Workflow-provenance systems in scientific computing have modeled activity-to-entity dependency graphs since before most current ML tooling existed" | Section 6, line 79 | No | A historical/factual claim about a named field; this programme's own `contribution-03/provenance-review.md` already has a stronger, more precise citation available (Buneman et al., ICDT 2001, why/where-provenance) that was never carried into this article | **NEEDS CITATION** — the Buneman citation is already verified elsewhere in this programme and should be added here rather than left as an uncited assertion |
| "CI/CD deployment gates block a release until required checks pass" | Section 3, line 47 | No | Generic enough that O'Reilly style likely does not require a citation (this is common practitioner knowledge, not a specific claim about one system) | PASS, no citation needed |

## Citation plan for v2

1. **Complete citation [4]** — re-fetch `arxiv.org/abs/2412.17618` directly
   (not via search summary) to confirm the full author list before any
   external submission.
2. **Add a citation for PDP/PEP / XACML** — a general, authoritative
   reference (e.g., the OASIS XACML specification), used once, at first
   mention in Section 3.
3. **Add a citation for Kubernetes admission controllers** — official
   Kubernetes documentation, used once.
4. **Add citations for in-toto and SLSA** — each project's own
   authoritative site/spec, used once, at first mention.
5. **Add the Buneman et al. why/where-provenance citation** (ICDT 2001)
   to Section 6's workflow-provenance sentence — already independently
   verified elsewhere in this programme
   (`contribution-03/source-ledger.md`, S16; identified as a required
   addition in the research note's own adversarial review and never
   carried forward into this article, a gap worth closing here).

None of these five additions require new research — all are either
already-verified citations sitting unused elsewhere in this programme
(Buneman) or standard, easily-verifiable references to named,
well-known projects (Kubernetes, XACML, in-toto, SLSA) that a narrowly
necessary verification pass (not a new research pass) can confirm before
v2.

## Overall

**PASS on accuracy for all four currently-used citations. NEEDS CITATION
on five uncited factual claims, all addressable without reopening
research.**
