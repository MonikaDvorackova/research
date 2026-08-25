---
id: note-contribution-03-article-claim-review
title: "Contribution 3 Article draft-v1 — Claim Ledger"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [contribution-03, article, review, claims]
refs: [../draft-v1.md, reviewer-report.md]
---

Classification: SUPPORTED / SUPPORTED WITH QUALIFICATION / SYNTHESIS /
OBVIOUS-PRIOR-ART / OVERSTATED / UNSUPPORTED.

| Claim (as stated or implied in draft-v1) | Location | Classification | Basis |
|---|---|---|---|
| "does not necessarily compose" | line 107 (and title/thesis throughout) | **SUPPORTED WITH QUALIFICATION** | True and correctly hedged, but the underlying mechanism is close to guaranteed by `DecisionRecordT1`'s schema (Objection 6) — supported as stated, but the article does not disclose how much of the "necessarily" is doing the qualifying work. |
| "trajectory" (as the object of reconstruction) | throughout | **SYNTHESIS** | A reasonable practitioner-facing term for what diagnosability theory would call a "path" or "history" over a discrete-event system (`../../diagnosability-review.md`) — legitimate as vocabulary, not a new formal object. |
| "system" (title: "...Unreconstructable System") | title | **OVERSTATED** | The experiment measures trajectory-level (multi-decision) dependency-edge identifiability, explicitly not full system-state reconstruction (G4 in `../../generalization-from-c2.md` is out of scope). "System" claims a broader unit of analysis than was tested. See `title-review.md`. |
| "unreconstructable" (title) | title | **OVERSTATED** | Even in the four failing cases, the record is not uninformative — it narrows to exactly the tied candidates (e.g., D1 or D2), never to "nothing." "Unreconstructable" reads as a stronger, more absolute failure than AMBIGUOUS-with-named-candidates actually is. |
| "causal structure" / "causal execution order" | lines 21, 85 | **SUPPORTED** | Standard systems/distributed-computing usage (execution/dependency ordering), not a statistical-causal-inference claim; consistent with the field's own vocabulary and with Article 2's prior careful usage. No issue. |
| "dependency" (edges, relation) | throughout | **SUPPORTED / DEFINITIONAL** | Defined at first use, used consistently; the specific operationalization (value-match or recency) is disclosed as domain-specific in Limitations. |
| "guarantees" ("does not give you the second... for free") | line 13 | **SUPPORTED** | Informal, not overclaimed as a formal guarantee; consistent with the qualified tone elsewhere. |
| "globally" / "locally" | throughout | **SUPPORTED / DEFINITIONAL** | Cleanly and consistently used; this pairing is one of the article's genuine strengths. |
| "locally auditable and globally ambiguous" | line 97 | **SYNTHESIS** | A fair, well-supported characterization of the T1 failure cases specifically — but see the construct-validity caveat in `reviewer-report.md` §5 (only dependent decisions are scored; "globally ambiguous" is not tested against false-edge invention on independent decisions). |
| "reconstructability" | throughout, inherited from Contribution 2 | **OBVIOUS / PRIOR-ART-ADJACENT** | Per `../../diagnosability-review.md`, near-identical in structure to established diagnosability theory (Sampath et al. 1995, cited as [4]). Legitimate as consistent programme terminology; not a new technical property, and the article does not claim it is one — correctly cautious here. |
| "missing relation" (the negative-control finding) | lines 71–77 | **SUPPORTED** | Directly matches the raw data: C3-6/T1 resolves CORRECT_UNIQUE once `causal_trace_event` is added, C3-2/T1 (structurally identical otherwise) does not (`experiment/results/edge_level_results.csv`). |
| "not a new provenance mechanism, and does not claim to be one" | line 87 | **SUPPORTED** | Verified consistent throughout; the article never claims a new mechanism anywhere else either. |
| "existence... not... prevalence" | line 101 | **SUPPORTED** | Consistently maintained; no p-value, sample-size, or prevalence language found anywhere in the article (grep-verified, see `empirical-traceability.md`). |
| "the same composition question applies to any system built from dependent, individually-auditable steps" | line 109 | **SUPPORTED** | Confirmed directly by the AI-specificity removal test (`reviewer-report.md` §7) — the claim is accurate, and unusually honest for a piece that could have overclaimed AI-uniqueness. |
| "∀i identifiable(C(di)) ⇏ identifiable(E)" | line 31–37 | **OVERSTATED (as rigor), OBVIOUS (as content)** | Presented with the trappings of a formal result; substantively close to tautological given the schema (`reviewer-report.md` §17). Recommend cut or explicit relabeling. |
| "an investigator was built for each regime. Neither is a strawman" | line 53 | **SUPPORTED** | Verified against `src/reconstruction.py`: T1's investigator infers wherever local evidence uniquely determines an edge (value match, unique-latest timestamp) before returning AMBIGUOUS; not a weak baseline. |

## Summary

No claim in draft-v1 is factually **UNSUPPORTED**. The two claims with
the most serious classification issues are the title's "system" and
"unreconstructable" (**OVERSTATED**, both correctable by retitling — see
`title-review.md`) and the formalization (**OVERSTATED as rigor**,
correctable by cutting or relabeling). The composition claim itself is
**SUPPORTED WITH QUALIFICATION** — true, correctly hedged in the
article's prose, but resting on a mechanism closer to guaranteed than
discovered, which the article does not disclose anywhere (this is
Objection 6's core finding, not a separate issue).
