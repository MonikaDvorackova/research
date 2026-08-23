---
id: note-contribution-02-drafting-terminology
title: "Contribution 2 Drafting Readiness — Terminology"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, drafting-readiness, terminology]
refs: [thesis-and-titles.md, ../minimal-decision-record.md]
---

## Terminology

Stable terms, decided before drafting. "Ours" means coined or
repurposed specifically for this contribution; "established" means used
in the same sense elsewhere in prior art.

| Term | Definition | Established prior-art term? | Ours? | Collision risk | Recommended use |
|---|---|---|---|---|---|
| **Decision-time binding** | The specific mechanism tested as Regime C: an explicit record, authored at t0, pinning a decision to specific version identifiers of policy/authority/model/evidence. | No exact match (closest: in-toto Predicate, PROV Usage relation) — `../collision-tests.md` Objection 7/1 | Ours, narrowly | Now narrower than the article's own thesis (F10-6 shows binding is *one implementation*, not the required property itself) — using it as the headline term risks implying uniqueness. | Use only to name the *specific experimental condition* (Regime C), never as the name of the general required property. |
| **Causal linkage / causal relation** | The general, empirically supported required property: any preserved relation connecting a decision to the specific version(s) it consumed. | Loosely related to W3C PROV's "Usage" relation, but PROV does not require version-identification or valid-time containment | Ours, as the operative term for the narrowed thesis | Risk of confusion with "causality" in the statistical/philosophical sense (cause-and-effect) — this is not what's meant; it is closer to "reference" or "pointer" than to causal inference. | **Primary term for the general property** (per `../novelty-verdict.md`'s follow-up update). Define explicitly on first use to head off the statistical-causality misreading. |
| **Consumed context** | The specific set of versions (of policy, evidence, authority, model, relevant config) a decision actually used, as opposed to what merely existed at the time. | Not standard; closest informal usage in observability discourse | Ours | Low, if defined early — clear once "retained vs. consumed" (the title's own distinction) is established | Use for the C(d) set in any formalization; pair consistently with "retained" as its contrast term. |
| **Decision context** | Looser, unscoped term for "whatever surrounded a decision." | Common informally, no fixed technical meaning | N/A — too vague to be "ours" either | High — this is exactly the term `../problem-formalization.md` warns risks becoming unbounded (sub-problem F) | **Avoid** as a load-bearing term; use "consumed context" (scoped, C/D/E-specific) instead. |
| **Historical context** | Same looseness as "decision context," with an added temporal-distance connotation. | Common informally | No | Same as "decision context," plus vagueness about whose history (the artifact's, or the decision's) | **Avoid**; if temporal distance needs naming, say "at t1" or "later" explicitly rather than reaching for this phrase. |
| **Decision provenance** | The lineage graph (PROV-shaped) connecting a decision to the entities/agents involved. | Yes — direct extension of W3C PROV's established sense of "provenance" | Extension, not coinage | Low — PROV's meaning transfers cleanly | Use when specifically invoking the PROV-graph framing (`prior-art-matrix.md`'s PROV row), not as a general synonym for the thesis. |
| **Decision-context provenance** | Redundant compound of "decision provenance" and "consumed context." | No | No — should not be coined | High — adds a word without adding meaning; likely to be read as a third, distinct concept by a careful reader | **Do not use.** Prefer "decision provenance" (when invoking PROV specifically) or "consumed context" (when naming the C(d) set), never both compounded. |
| **Historical reconstructability** | The general property of being able to answer, at t1, why D was valid at t0 — i.e., sub-problem G from `../problem-formalization.md`. | Loosely related to digital-preservation literature's "interpretability over time" (OAIS), not a fixed term there either | Ours, as used within this programme | Low, if scoped explicitly to decisions (not generalized to "historical reconstructability of AI behavior," which drifts toward Contribution 3) | Use as the article's name for the overall target property (G); always pair with "of a decision," never left general. |
| **Temporal correctness** | The primary metric name from both experiments: whether the reconstructed version is the one whose valid-time interval actually contained t0, per ground truth. | Ours, as a metric name (not a general term in bitemporal-database literature, which speaks of valid-time queries but not a named "correctness" metric) | Ours | Low — scoped explicitly to the experiments' own metric definitions | Use only when referring to the measured metric (`../experiment/experiment-design/metrics-and-scoring.md`), not as a loose synonym for "accurate." |
| **Decision-context identifiability** | The candidate formal property evaluated in `formalization.md`: whether a sufficient preserved relation exists to uniquely determine each element of a decision's consumed context from later-available state. | No | Ours, if adopted (see `formalization.md`'s decision) | Low, given its narrow, defined scope | Use only if the minimal formalization is included in the article; do not use informally as a synonym for "reconstructability" (which is broader, covering G's normative-synthesis half too). |
