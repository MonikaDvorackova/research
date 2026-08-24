---
id: note-contribution-03-article-03-options
title: "Contribution 3 — Article 3 Thesis Candidates"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-03, article-options]
refs: [generalization-from-c2.md, composition-review.md, assurance-integration-review.md]
---

## Three thesis candidates, ranked

No prose drafted. Ranked by how well each survives this review's own
adversarial findings, per the authorizing task's Section 24 decision
rule.

### Rank 1 — The composition question (research agenda)

**Thesis:** Contribution 2 earned that a single decision's consumed
context can fail to be uniquely reconstructable even from complete
retained history. It is currently unknown whether that guarantee — once
achieved per-decision — composes into a guarantee at the trajectory
level (multiple, possibly interdependent decisions within one agent
execution), or whether it fails to compose the way local component
verifiability is already known to fail to guarantee global emergent-
behavior predictability in systems-of-systems research.

- **Contribution type:** C — research agenda article.
- **Prior-art collision:** Compositional verification / emergent-behavior
  literature (direct, current, strong — `composition-review.md`);
  diagnosability theory (for precisely framing the base, per-decision
  property being composed, `diagnosability-review.md`); bisimulation/
  observational equivalence (for formalizing what "compose" would even
  mean).
- **Empirical requirement:** Eventually yes — an experiment structurally
  extending Contribution 2's own methodology to a multi-decision
  trajectory, testing whether Regime B/C's per-decision results
  aggregate as expected or reveal a new, trajectory-level failure mode.
  Not designed in this pass, per the authorizing task's explicit
  instruction.
- **Why Articles 1 and 2 matter:** Contribution 1 supplies the decision/
  enforcement vocabulary a trajectory is built from; Contribution 2
  supplies both the G1 result being extended and the exact experimental
  methodology (three-regime design, deterministic investigator, honest-
  ambiguity discipline) this candidate would reuse rather than reinvent.
- **Strongest objection:** This may be no more than "run Contribution 2's
  experiment again, at a larger scale" — a scaling exercise dressed as a
  new question. The counter-argument, and the reason this is still
  ranked first: compositional-verification research shows scaling is
  *not* safe to assume trivial for adjacent properties (predictability),
  so the question of whether it is trivial for reconstructability
  specifically is genuinely open, not merely unasked.

### Rank 2 — The taxonomy/synthesis piece

**Thesis:** System-level "understanding" of an AI-mediated decision
system is not one property but a vector of already-named, already-
formalized properties (diagnosability-shaped reconstructability,
observability, interpretability, system-identification-shaped
predictability, verifiability) that no source in this review's search
connects explicitly to each other, or to Contribution 2's own results,
for this specific object class — and dynamic assurance cases, not a new
architectural layer, are the correct existing coordination mechanism,
not yet explicitly composed with a decision-context-reconstructability
claim of Contribution 2's specific kind.

- **Contribution type:** B — systems synthesis article, weakened by the
  dynamic-assurance-case finding relative to how it would have looked
  before this pass.
- **Prior-art collision:** All of `operationalization-review.md`'s
  vector table; `assurance-integration-review.md`'s dynamic-assurance-
  case finding is the most damaging single collision against this
  candidate's ambition.
- **Empirical requirement:** None — a synthesis/taxonomy piece, matching
  Contribution 1's own evidentiary shape.
- **Why Articles 1 and 2 matter:** Both are the concrete illustrations
  the taxonomy organizes around (decision-level control; decision-level
  reconstruction).
- **Strongest objection:** Risks being a literature map with a citation
  list, not a contribution — the specific, defensible claim (the
  diagnosability↔Contribution-2 connection; the "DACs coordinate but
  don't yet specify this claim type" finding) is real but narrow, and a
  full article built around it risks reading as padded survey rather
  than argument.

### Rank 3 — No article; closing research note only

**Thesis:** The historical/comparative review and this narrow pass
together already constitute the honest, complete output of this line of
inquiry. Recommend explicitly retiring the capability-vs-understanding
framing and the "Understanding Layer" architectural claim, publishing
(if anything) only a short closing note pointing future researchers at
the G2→G3 composition boundary this review isolated, without attempting
a full Article 3.

- **Contribution type:** E — no independent article, by explicit choice
  rather than default.
- **Prior-art collision:** N/A — this option concedes the field, it does
  not compete in it.
- **Empirical requirement:** None.
- **Why Articles 1 and 2 matter:** They remain complete, independently
  valid contributions on their own; this option's only claim is that
  they do not need a third, weaker capstone to be worth having done.
- **Strongest objection:** This may be premature — Rank 1's research
  question is genuinely novel and well-scoped; abandoning the programme
  here could waste real, earned groundwork (`diagnosability-review.md`,
  `composition-review.md`) that a future, better-resourced pass could
  use productively.

## Recommendation

**Rank 1, conditional on the empirical requirement being satisfied
first — not Rank 2, and not Rank 3 outright.** This is not a
recommendation to draft Article 3 now (see `FINAL-RESEARCH-VERDICT.md`'s
"ready to draft" answer); it is a recommendation about which of the
three candidates deserves the next unit of research effort, if any is
authorized.
