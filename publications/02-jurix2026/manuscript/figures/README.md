---
id: pub-02-jurix2026-figures
title: "Figures — Publication 02"
type: publication
status: draft
created: 2026-07-29
updated: 2026-07-30
tags: [jurix, figures, publication-02]
source: ../planning/jurix-specification.md
---

## Publication figures (final set)

Four essential figures (approved specification: B–E). Research-workflow figure omitted as optional.

| Pub. order | Spec ID | File stem | Placement (manuscript) |
|---|---|---|---|
| Figure 1 | B | `fig1-fragmented-preservations` | §2 (end) |
| Figure 2 | C | `fig2-decision-knowledge-structure` | §4.2–4.3 |
| Figure 3 | D | `fig3-knowledge-continuity-model` | §5.2–5.5 |
| Figure 4 | E | `fig4-reconstruction-process` | §5.6 |

Each figure is provided as:

- `.svg` — editable vector source (grayscale-safe)
- `.pdf` — LNCS-oriented export via `rsvg-convert`

### Suggested captions (for later manuscript insert)

1. **Fig. 1.** Fragmented preservations in contemporary AI deployments: operational artefacts remain available as mutable system state, while structured, decision-bound Decision Knowledge is not assembled. Ordinary change between decision time (*t0*) and review time (*t1*) widens the gap.
2. **Fig. 2.** Structure of Decision Knowledge for one AI-assisted decision: components from the working inventory are bound to a decision object.
3. **Fig. 3.** Conceptual model for engineering Knowledge Continuity: capture points on an existing decision path form a bound Decision Knowledge artifact; continuity services retain it for later use; the change plane must not silently rewrite past Decision Knowledge. Not an implementation architecture.
4. **Fig. 4.** Conceptual reconstruction process and reconstruction probe (method only; no empirical results).

### Visual grammar

- Solid stroke = retained / bound path
- Dashed stroke = live system state or broken / failure path
- Double border = Decision Knowledge artifact
- Hatch fill = mutable live state or change plane
- No colour-dependent meaning
