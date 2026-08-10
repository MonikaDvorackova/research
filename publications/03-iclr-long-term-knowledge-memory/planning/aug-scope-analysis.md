---
id: pub-03-aug-instance-and-scope
title: "AUG instance qualification and scope analysis"
type: research-notes
status: audit
created: 2026-08-01
updated: 2026-08-01
---

# Prior-project qualification (do not force into AUG)

Adequacy = unique entailment \(f_T(x,I)=y^*\) (see `aug-formal-definition.md`).

## CR-Gap

**What was measured:** Retrospective reconstruction under overwrite / keep-all / revision-aware stores; retrieval success vs reader failure decomposition (`experiments/cr-gap-pilot/outputs/findings.md`).

**Was \(I\) formally sufficient to identify the historical answer?**  
Often **no**. Overwrite **deletes** evidence — adequacy fails by construction. Keep-all retains records but conflicts and retrieval ranking mean the *presented* top-\(m\) view is frequently **not** a unique entailment of the historical state (reader failures given retrieval = 257 for keep-all). The scientific tension was whether the **trace retained enough structured, selectable history**, not whether a uniquely adequate \(I\) was mis-used.

| Classification | **partial AUG instance** (only the subset: retrieval succeeds *and* \(f_T\) uniquely fixes \(y^*\) on the presented view *and* reader errs). Overall project: **not primarily an AUG study**. |

## Archive Pareto

**What was measured:** Retention policy vs completeness/historical utility; go/no-go NO-GO with universal dominance (`go_nogo.md`).

**AUG?** **No.** This is a **capacity-allocation** experiment. It never established a fixed \((T,x)\) with programmatic unique adequacy of archived \(I\) and then measured \(M(x,I)\neq y^*\). The pilot failed before adequacy–utilization was on the table.

| Classification | **not an AUG instance** |

## P-Bind

**What was measured:** Gold triple present in fixed top-\(k\), length/position matched; deterministic JSON attribute lookup; binding-error taxonomy.

**Uniquely determined by gold-present context?** **Yes** under programmatic \(f_T\): the gold record alone determines \(y^*\); competitors do not change the unique correct lookup (they are distractors, not alternate entailments).

**Model fail to use adequate evidence?** **Yes** when it outputs a competitor value (entity swap).

| Classification | **direct AUG instance** |

## F1×F4

**What was measured:** Same task family as P-Bind; isolated conjunction of same-attribute + lexically similar entity.

**Direct AUG or disambiguation error?** Both: it is an AUG event *and* a specific **disambiguation / binding** error under competitive cues. It does **not** expand task-family coverage beyond P-Bind.

| Classification | **direct AUG instance** (same experimental family as P-Bind) |

## Breadth check

Qualifying direct instances: **P-Bind and F1×F4 only** — **one family**.  
CR-Gap at best partial; Archive Pareto none.  
⇒ Claiming AUG “breadth from four projects” is **unsupported**.

---

# Scope analysis

Scores 1–5 (higher = better for Pub-03 viability). Saturation risk: higher = worse.

| Scope | Coherence | Novelty | Falsifiability | Feasibility | ICLR depth | Saturation risk | Notes |
|---|---:|---:|---:|---:|---:|---:|---|
| **Universal AUG** | 2 | 1 | 2 | 3 | 2 | 5 | Occupied by Sufficient Context (ICLR 2025) |
| **Agent-memory AUG** | 3 | 2 | 3 | 3 | 2 | 4 | Still “utilization under memory context”; RECON/MINTEval neighborhood |
| **Post-retrieval AUG** | 3 | 1 | 3 | 4 | 2 | 5 | Explicitly studied (RECON; utilization gap papers) |
| **Binding-specific adequacy failure** | 4 | 2 | 4 | 5 | 2 | 3 | Feasible; already judged **too narrow** for ICLR core (F1×F4 AC verdict C) |

## Recommended narrowest viable scope

**None for Pub-03 continuation under the AUG banner.**

If forced to pick the least incoherent remnant: **binding-specific adequacy failure** — but that is the closed F1×F4 line, not an ICLR-depth object.

**Narrowest viable scientific scope that is still a research object:** *not AUG*; the occupation audit kills the umbrella.
