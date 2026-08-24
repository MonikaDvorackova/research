---
id: note-contribution-03-ai-systems-review
title: "Contribution 3 — AI/ML Systems, XAI, Verification, and Assurance Review (Claims C, E, F)"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-03, ml-systems, agents, xai, formal-methods, assurance]
refs: [pre-research-claim-ledger.md, source-ledger.md]
---

## Testing Claims C (comparative "losing the race"), E (AI-specific difference), and F (fragmentation)

Per the authorizing task's explicit sequencing, this review only reaches
AI-specific literature after the software-engineering baseline
(`historical-literature-review.md`, `program-comprehension-review.md`,
`observability-review.md`, `provenance-review.md`) is established.

## What genuinely changed with learned components (Claim E)

Sculley et al., "Hidden Technical Debt in Machine Learning Systems"
(NeurIPS 2015) [S21] is the foundational, already-cited (internally,
`../conceptual-inversions.md` Inversion F) source for this question. It
identifies ML-specific risk factors with no direct analogue in ordinary
software: **entanglement** (changing anything changes everything, since
components are not independently tunable), **hidden feedback loops**,
**undeclared consumers**, and **data dependencies** that "cost more than
code dependencies" [S21]. These are not restatements of general software
complexity — they are specific to systems whose behavior is learned from
data rather than explicitly authored, which is the clearest,
literature-supported candidate for what is genuinely different about
AI-mediated systems as objects of understanding. **This is the strongest
source-supported answer to Claim E found in this review.**

## Foundation models and agents: current state, honestly reported

Mechanistic interpretability has moved from niche research toward "an
emerging AI debugging, auditing, and safety discipline" [S22], with a
January 2025 cross-institutional paper ("Open Problems in Mechanistic
Interpretability," 29 researchers, 18 organizations) formalizing the
field's open problems, including the explicit finding that **"many
interpretability queries are intractable"** [S22]. This is a direct,
current, source-supported data point bearing on Section 14's
operationalization question: if the field's own leading researchers
report intractability as an open problem, "understanding" cannot
currently be treated as a routinely measurable quantity at the model
level, regardless of what a future architectural layer might do at the
system level.

For agents specifically, a layered observability architecture (the
"Agentic Trajectory & Layered Interpretability Stack," extending
OpenTelemetry to agent workloads) has emerged as a convergent industry
pattern by 2026 [S23]. The same 2026 source states directly: **"the AI
observability landscape... is characterized by impressive depth at
individual layers but limited integration across them"** [S23] — the
single most directly relevant, current, technical confirmation found in
this review of a *scoped* version of Source A's fragmentation claim (F):
real, current, but specific to integration *across layers of AI agent
observability tooling*, not (yet) evidenced as a claim about
explainability/governance/provenance as separate research *disciplines*
failing to coordinate.

## Explainability (XAI), tested on its own terms

XAI is not one method; the field itself distinguishes interpretability,
post-hoc explanation, feature attribution, counterfactual explanation,
and (increasingly) mechanistic interpretability as different objects
with different audiences and different guarantees [S22][S24]. Recent
work explicitly frames the goal as "bridging the gap between the
intricacies of advanced AI algorithms and the imperative for human
comprehension" [S24] — again, close to Source A's own language, already
established as this field's own self-description, not evidence that the
field is unaware of the problem.

**What system-level "understanding" would need to contain that
model-level explainability does not, per this review:** XAI's object is
almost universally *a single model's output on a single input*
[S20][S22][S24] — none of the sources reviewed extend XAI's guarantees to
a *multi-component decision path* (model + retrieval + policy +
authority, Contribution 2's own object) or to *why a past decision was
authorized* in the normative sense `provenance-review.md` isolates. XAI
does not, by any source found here, aggregate into system-level decision
justification by default — this is a genuine, if narrow, gap XAI's own
literature does not claim to close.

## Formal methods and runtime verification, tested against the gap

Runtime verification checks whether "a system's behaviour conforms to
requirements," using monitors that compare observed traces against a
formal specification [S25]. This is a load-bearing, precise distinction:
runtime verification answers **"does property P hold"**, not **"why did
the system behave as it did"** or **"can we reconstruct what happened"**
— a fundamentally different question from reconstruction, confirmed
directly by the field's own definition, not merely inferred. Runtime
monitors can be applied to black-box neural components, using formalized
safety properties [S25] — but this closes the *verification* gap, not
the *reconstruction* or *explanation* gap this programme's earlier
contributions target.

## Assurance cases as a candidate existing "umbrella" (testing Claim F directly)

Assurance/safety cases (Claim-Argument-Evidence, Goal Structuring
Notation) are a mature, standards-adjacent discipline for **structuring
justified confidence in a system property**, already applied to AI and
autonomous systems specifically [S26][S27][S28]. This is the strongest
candidate found in this review for an *already-existing* umbrella that
could, in principle, coordinate evidence from explainability,
observability, provenance, and governance into one structured argument
— directly testing whether Source A's fragmentation diagnosis is simply
wrong because systems/safety engineering already solved the
coordination problem.

**Verdict on this specific test:** assurance cases are a **structuring
methodology for evidence**, not a **source of evidence** — they organize
claims and arguments; they do not themselves produce observability,
provenance, or explainability data. This mirrors `../notes/intellectual-progression.md`
Task 7's own finding about Contribution 1's enforcement gate ("a
downstream consumer of preserved evidence... not the preservation
mechanism itself"). Assurance cases could coordinate the fragmented
fields Source A names, but adopting an assurance-case framework does not,
by itself, generate the underlying reconstruction/observability/
explanation content those fields would need to supply — so assurance
cases **narrow** the fragmentation claim (a coordination mechanism
exists and is mature) without fully **refuting** it (the fields still
need to actually produce compatible, composable evidence, which is a
separate, unresolved question this review did not find addressed).

## Verdict on Claims C, E, F

- **Claim E (AI-specific difference):** partially survives, narrowly.
  Sculley et al.'s entanglement/feedback-loop/undeclared-consumer
  findings are genuine, source-supported, AI/ML-specific complications
  with no direct software-engineering analogue found in this review.
- **Claim C (AI is currently losing the capability/understanding race):**
  does **not** survive as an empirical claim. No source found in this
  review measures capability and understanding as comparable quantities
  over time for any system, AI or otherwise. The closest available
  evidence (mechanistic interpretability's own "many queries are
  intractable" finding [S22]) is a snapshot, not a trend, and does not
  establish direction of change, let alone relative rate.
- **Claim F (fragmentation):** survives narrowed and scoped. Real,
  current, technical evidence exists for fragmentation *within* AI
  agent-observability tooling specifically [S23]. No evidence found for
  fragmentation *across* explainability/provenance/governance/auditability
  as research communities. Assurance cases are a real, mature candidate
  coordination mechanism this review found, which Source A's own
  framing does not acknowledge.
