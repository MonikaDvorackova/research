---
id: pub-03-aug-cross-phenomenon-hypotheses
title: "AUG candidate laws and cross-phenomenon prediction"
type: research-notes
status: audit
created: 2026-08-01
updated: 2026-08-01
---

# Candidate general laws (max three) — then kill

AUG as a **definition** is not a paper. Below are candidate laws. Platitudes are rejected.

## Rejected non-laws (explicit)

- “More interference ⇒ more errors”
- “Information presence does not guarantee accuracy” ← **Sufficient Context / oracle-RAG already**
- “Harder tasks reduce utilization”

## Candidate Law A — Conjunctive cue necessity under unique adequacy

- **IV:** Presence of cue pair (attribute-match ∧ lexical-neighborhood) vs either cue alone, holding \(f_T(x,I)=y^*\).
- **DV:** Binding-swap rate (entity swap).
- **Prediction:** Swap rate rises only under the conjunction; singles ≈ null.
- **Falsification:** Either single cue alone yields ≥ half the conjunction effect, or conjunction effect disappears under length/position controls.
- **Task families required:** (1) entity–attribute lookup; (2) **a second non-binding family** with analogous cue factors (e.g. historical state selection with “same slot ∧ similar label”).

**Status:** Supported **only** in family (1) by F1×F4. Family (2) **not instantiated**.  
⇒ **Not adoptable as AUG law** for Pub 03.

## Candidate Law B — Adequacy margin / uniqueness erosion

- **IV:** Number of alternate values in \(I\) that share the queried attribute (competitors with same role), holding gold present and \(Y_T=\{y^*\}\).
- **DV:** Error rate / swap rate.
- **Prediction:** Errors increase with count of same-role competitors even when uniqueness of \(y^*\) is preserved.
- **Falsification:** Flat curve after length match; or errors are mostly malformed/unsupported rather than competitor-sourced.
- **Task families:** attribute lookup; multi-hop slot filling with unique gold path.

**Status:** Partially echoed by P-Bind ρ packing, but factor decomp showed **same-role alone (F1) is null** without lexical neighborhood.  
⇒ **Rejected** as stated (wrong IV).

## Candidate Law C — Invariance under information-preserving transforms

- **IV:** Transforms of \(I\) that leave \(f_T(x,I)=y^*\) unchanged (paraphrase, record order among non-gold, table vs list).
- **DV:** AUG event rate.
- **Prediction:** Rate invariant under pure information-preserving transforms; varies only when transform changes competitive cue structure.
- **Falsification:** Large rate changes under paraphrase-only transforms that preserve \(f_T\).
- **Task families:** lookup; conflict resolution with unique gold.

**Status:** **Not tested** in repo. Cannot be claimed. Not used to rescue AUG.

---

# Cross-phenomenon prediction (exactly one attempt)

**Attempted link:** entity–attribute binding (P-Bind) ↔ historical state selection (CR-Gap retrospective).

| Field | Specification |
|---|---|
| Task families | (A) gold-present attribute lookup; (B) retrospective fact selection from a multi-revision store view |
| Adequacy guarantee | (A) gold triple in \(I\), programmatic lookup; (B) **requires** presented \(I\) to uniquely entail historical \(y^*\) (revision-aware oracle view) |
| Controlled variable | Presence of a “same-slot competitor” with a lexically similar surface (name/key) |
| Predicted common relationship | Under unique adequacy, same-slot + similar-surface competitors raise **competitor-sourced substitution errors** in both families |
| Supporting outcome | Parallel Δ in swap/substitution rates on both families under matched length |
| Outcome proving **no shared law** | CR-Gap errors remain dominated by **non-adequate** views (missing/conflicted retrieval) while binding errors require adequate gold-present \(I\) — i.e. different causal regimes |

### Evaluation of the attempt

A precise shared prediction **cannot be honestly affirmed** from existing evidence:

1. CR-Gap’s primary failures are often **adequacy failures of \(I\)** (overwrite; conflicted keep-all retrieval), not AUG events.  
2. Binding failures are AUG events under programmatic adequacy.  
3. No experiment manipulated “same-slot ∧ similar-surface” in historical selection.

**Conclusion:** No cross-phenomenon law is available.  
Therefore AUG functions as an **umbrella label**, not a unifying scientific object for this repository’s results.
