---
id: note-contribution-02-novelty-verdict
title: "Contribution 2 — Novelty Decomposition and Surviving Thesis Verdict"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, novelty-verdict, thesis]
refs: [prior-art-audit.md, collision-tests.md, temporal-semantics.md, minimal-decision-record.md]
---

## Contribution 2 — Novelty Decomposition and Surviving Thesis Verdict

Scope: Tasks 9, 10, and 11. This document does the actual adversarial work
the brief demands: it does not choose the flattering verdict, and it applies
the same disqualifying standard already used against Contribution 1 in
`article-01-decision-level-control/novelty-audit.md` (Position B: new
synthesis, not new mechanism).

---

## Task 9 — Does Contribution 2 need the word "knowledge"?

**No.** Tested against the candidate meanings in the brief:

- *Sufficient information for historical reconstruction* — this is what
  Contribution 2 actually needs, and it is expressible without the word
  "knowledge" at all: as the binding, developed in
  `minimal-decision-record.md`, between a decision and the temporally valid
  versions of the evidence, policy, and authority that applied to it.
- *Explanatory context* — subsumed by the binding above; not a separate
  requirement.
- *Provenance* — a real, existing technical term (W3C PROV) that Contribution
  2 uses precisely, in its narrow sense (lineage relations), not loosely.
- *Justification / decision rationale* — this is sub-problem G specifically,
  already named without needing "knowledge" as an umbrella term.
- *Temporal context* — this is `temporal-semantics.md`'s subject matter,
  again nameable without "knowledge."

"Knowledge" is not required by any of Contribution 2's actual claims. It
introduces exactly the epistemological baggage the brief warns about, and it
collides — unnecessarily — with Contribution 3's reserved territory
(capability vs. understanding, the nature of "understanding" as a systems
property). **Recommendation: retire "knowledge" from Contribution 2's
technical vocabulary entirely.** It may remain in practitioner-register
framing exactly where it already lives (Source A's prose, the O'Reilly
drafts) without being promoted to a formal thesis term — consistent with
`claim-graph.md`'s own C6 precision concern, now resolved rather than merely
flagged.

---

## Task 10 — Novelty decomposition

| Dimension | Rating | Reasoning |
|---|---|---|
| **Historical decision reconstruction as a problem (general, not AI-specific)** | None | Already well-addressed piecemeal by bitemporal databases (D/E), event sourcing (A/B), and PROV (lineage) for non-AI systems. The general problem of "was this decision valid under the rules in force then" is old — it is the subject matter of financial audit, legal discovery, and compliance engineering long before AI. Claiming novelty at this level would not survive scrutiny. |
| **AI-specific decision reconstruction** | Moderate | The specific set of transient dependencies (prompts, live retrieval corpora, policy-as-config, agent delegation) is a genuinely AI/LLM-era pattern not addressed by name in any surveyed source. The underlying mechanisms needed are all pre-existing (per the collision tests), but their *combination*, applied to *this* dependency set, is not found packaged elsewhere. |
| **Decision-context preservation (the binding concept itself)** | Moderate-strong | The distinction between "artifacts are versioned elsewhere" and "a decision is bound, at t0, to specific versions of those artifacts" (Objection 8) is the most defensible, checkable finding in this audit — genuinely not found stated this way in the surveyed prior art, though it is a modest, assemblable idea once stated, not a deep theoretical discovery. |
| **Temporal evidence continuity** | Weak | Bitemporal database theory already fully solves the *representational* problem (Objection 4). What remains novel is narrowly the *application* to AI-specific objects, not the temporal theory itself. |
| **Policy/authority continuity** | Weak, for the same reason as temporal evidence continuity | Structurally identical to bitemporal modeling of role/delegation validity — a solved database problem, unapplied by default in AI tooling. |
| **Minimal decision record (as a named artifact)** | Moderate | No existing schema (PROV, in-toto Predicate, SLSA provenance, EU AI Act Art. 12 minimum) matches the field set derived in `minimal-decision-record.md`, but every field individually maps onto an existing schema's concept — this is assembly novelty, not conceptual novelty. |
| **Reconstruction completeness criteria (replay vs. reconstruction)** | Moderate-strong | Confirmed, in `collision-tests.md` Task 6, as not found formalized this way in the prior art surveyed (the ACM reproducibility taxonomy covers only the replay half). This is the single cleanest, most citable novel distinction to emerge from the audit. |
| **Reconstruction failure experiments** | None yet — this is a method, not a finding | No claim to novelty is being made here; `empirical-next-step.md` treats this as future design work, refined from `empirical-program.md`'s existing sketch, not as an already-novel contribution. |

**Overall pattern:** identical in shape to Contribution 1's own audit
(`article-01-decision-level-control/novelty-audit.md`): every mechanism is
old (bitemporal databases, PROV, in-toto/Sigstore, event sourcing); what is
new, where anything is, is the specific synthesis and the specific
application to AI's transient-context problem — never a new primitive.

---

## Task 11 — Surviving thesis verdict

**Verdict: B — Narrowed survival.**

Reasoning, tested against the four options honestly:

- **Not A (strong survival).** Existing mechanisms are not absent — they are
  abundant and, in the case of bitemporal databases specifically,
  completely sufficient in theory for two of the four sub-problems this
  contribution cares about (D, E). Claiming that "existing mechanisms do
  not adequately represent the reconstruction problem" would be false; they
  represent most of it perfectly well, on paper.
- **Not C (framing only).** This was seriously considered: if bitemporal
  modeling + PROV + in-toto attestation can be composed straightforwardly,
  is the "synthesis" trivial enough that Contribution 2 is just relabeling
  existing engineering? Tested directly against `minimal-decision-record.md`
  and `collision-tests.md` Objection 8: no — because the **binding**
  property (a decision explicitly pinned, at t0, to specific valid-time
  slices of policy/evidence/authority) is not automatically produced by
  composing these mechanisms; it requires a deliberate architectural
  decision to record it, one that is not standard practice in any of the
  surveyed tooling (MLflow, vector databases, prompt stores, policy-config
  services). If this were purely a framing exercise, an example of an
  existing system already doing this by accident would be expected to turn
  up in the audit; none did.
- **Not D (falsified).** The distinctions found (replay vs. reconstruction;
  versioning-existing vs. binding-recorded; integrity vs. completeness in
  audit logs; execution-preservation vs. justification-preservation even in
  aviation safety practice) are checkable, survived nine adversarial
  objections, and are not merely restatements of things already solved.
- **B fits:** most of the individual primitives required (bitemporal
  validity, structured signed evidence, provenance graphs) already exist in
  mature, separate literatures. What Contribution 2 actually contributes is
  a **synthesis**: the recognition that AI-mediated decisions require these
  three primitives combined and bound per-decision, applied specifically to
  a dependency set (prompts, live retrieval, policy-as-config, delegated
  agent authority) that current AI/ML tooling does not, by default, treat
  this way.

**This is the same verdict shape Contribution 1 reached (Position B: new
synthesis, not new mechanism).** That consistency is a point in favor of the
audit's honesty, not evidence of a rubber-stamped process — the two
contributions were audited independently, against different prior-art
fields, and landed on the same modest, defensible claim shape.

---

## Recommended precise thesis (replacing "State Is Not Knowledge")

> **Retained system state — including logs, traces, and provenance
> records — does not, by default, bind a decision to the temporally valid
> versions of the evidence, policy, and authority that made it valid when
> it occurred. That binding, not any of the individual artifacts it would
> reference, is the missing engineering artifact, and closing the gap
> requires applying existing bitemporal and attestation primitives — not
> inventing new ones — to a set of AI-specific transient dependencies
> (prompts, live retrieval corpora, policy-as-config, delegated agent
> authority) that current tooling does not treat this way by default.**

Shorthand for practitioner framing (not a technical claim in itself):
**"Versioned is not bound."** This deliberately replaces "State Is Not
Knowledge" — the earlier phrase survives only as historical/practitioner
color in Source A's own prose, not as this contribution's operative thesis.

---

## Is Contribution 2 still independently publishable?

**Yes**, under the narrowed thesis above, for the same reasons
`contribution-boundaries.md` already established structurally (independent
truth conditions from Contribution 1, independent evidence type, now
independently audited prior art) — with one required correction to that
earlier document: the thesis statement it anticipated ("current state is
insufficient... because AI-specific context... was never treated as a
persistent engineering artifact") should be updated to the binding-centric
formulation above, which is more precise and, per this audit, more
defensible against the strongest available objections (4, 7, 8) than the
original formulation would have been.

---

## Post-experiment update (2026-08-23)

The reconstruction experiment designed in `experiment-design/` (design
verdict: READY FOR IMPLEMENTATION) was implemented and executed on
2026-08-23. Full report: `experiment/analysis/experiment-report.md`; short
verdict: `experiment/RESULT.md`; raw data: `experiment/results/`. This
section records the empirical consequence for the thesis above. It does
not replace or erase the pre-experiment verdict recorded above this line.

**Result, in one line:** the retroactive-correction half of the binding
mechanism (`../temporal-semantics.md`'s transaction-time/valid-time
confound) was confirmed with a clean, categorical, non-marginal empirical
result (Regime C's Temporal Correctness = 1.00 and False Historical
Confidence = 0.00 vs. Regime B's 0.00 and 0.50–1.00, on Cases 3, 8, and 9,
with B ≈ C exactly on every non-retroactive case). The concurrency-
ambiguity half of the mechanism (Case 10) was **not tested** by this run —
a disclosed implementation choice (exact, non-fault-injected timestamp
semantics) meant Case 10 never exercised genuine ambiguity, so B and C
tied there. Overall classification against the pre-registered
interpretation table (`experiment-design/preregistered-interpretation.md`):
**PARTIAL SUPPORT** — closest to row 1 (strong support) restricted to the
retroactive-correction mechanism, combined with row 8's shape for the
untested concurrency mechanism.

**Consequence for the surviving thesis:** this result **narrows and
empirically grounds** the thesis; it does not broaden, weaken, or falsify
it. Specifically:

- The thesis's central claim — "retained system state does not, by
  default, bind a decision to the temporally valid versions... that made
  it valid when it occurred" — now has direct empirical support for the
  retroactive-correction mechanism in a controlled, synthetic setting, not
  merely a design-level argument for why it should be true.
- The thesis should be read as **empirically demonstrated for one of its
  two named mechanisms** (retroactive correction) and **still open, not
  yet tested, for the other** (concurrency/attribution ambiguity under
  timestamp imprecision). Prior to this experiment, both mechanisms had
  equal (design-level, untested) standing; after it, they do not.
- Nothing in this result licenses claims beyond a synthetic, ten-case,
  controlled diagnostic study: not prevalence, not severity, not
  generalization to production AI systems, not compliance or
  trustworthiness claims (`experiment-design/validity-and-confounders.md`'s
  external-validity limitations remain fully in force and are unaddressed
  by this run).
- The event-sourcing collision question (`preservation-regimes.md`) also
  received direct empirical confirmation of its own narrow prediction:
  Regime B's event trace, which captures raw *values* rather than version
  *identifiers*, fully protected the evidence-supersession case (5) without
  binding, but did not protect policy/authority identification under
  retroactive correction — the exact, narrow distinction the design
  predicted, now measured rather than only argued.

**Contribution 2 remains independently publishable** under the thesis as
stated, with the scope of its empirical support now precisely bounded:
strong, controlled, synthetic evidence for the retroactive-correction
mechanism; no evidence yet, either direction, for the concurrency-
ambiguity mechanism. **Next step, not performed here and requiring a new
authorization:** a follow-up run of Case 10 with genuine clock/timestamp-
precision fault injection, to actually test the mechanism that run's clean
implementation left untested.

---

## Follow-up Case 10 update (2026-08-23)

A narrowly scoped follow-up experiment, explicitly authorized separately
from the primary experiment above, was implemented and executed to
resolve the one gap the primary run's post-experiment update named as its
required next step. Full report:
`experiment/followup-case10/analysis/experiment-report.md`; short verdict:
`experiment/followup-case10/RESULT.md`; raw data:
`experiment/followup-case10/results/`. **The primary experiment above is
unmodified: its commit (`31c58ddc6e95b5f66153b4c2dd35d91f4ae8e725`), raw
results, and reported metrics are unchanged.** This section only adds to
the record; it does not revise anything above this line.

**Mechanism tested:** timestamp precision loss (a decision's true moment
is truncated to whole-second observable precision before being
persisted), distinct from the primary experiment's retroactive-correction
mechanism. Six cases (F10-1 through F10-6); Regime B vs. Regime C only.

**Result, in one line:** where no causal signal connects a decision to
the specific version it consumed, complete version history genuinely
cannot resolve which version applied when a boundary falls inside the
decision's observable timestamp window (Regime C: Correct-Unique on
every such case; Regime B: honestly `AMBIGUOUS`, never confidently wrong
— False Historical Confidence = 0.00 throughout this run) — **but** a
disclosed negative control (F10-6) showed that an ordinary, non-binding
causal consumption event resolves the same ambiguity exactly as well as
Regime C's explicit binding does.

**Consequence for the surviving thesis: narrowed, not weakened or
broadened.** The concurrency/precision-ambiguity mechanism — the one
half of the original two-mechanism thesis the primary experiment left
untested — is now empirically demonstrated. At the same time, the
specific formulation "explicit decision-time binding is required" does
not survive as the narrowest account: the negative control shows the
operative requirement is **a preserved causal relation between a
decision and the specific version it consumed**, of which Regime C's
`DecisionBindingRecord` is one general, systematic, buildable
implementation — not the only one, and not shown here to be uniquely
necessary.

**Updated thesis statement**, superseding the "binding-centric"
formulation earlier in this document for the purpose of any future
drafting, without erasing it (it remains the correct description of what
was tested and found *before* this follow-up):

> Retained system state — including logs, traces, and provenance
> records — does not, by default, preserve a causal relation between a
> decision and the temporally valid versions of the evidence, policy, and
> authority that made it valid when it occurred. That causal relation,
> not any of the individual artifacts it would reference, is the missing
> engineering property; explicit decision-time binding is one general,
> systematic way to guarantee it exists for every decision, but this
> research programme has not shown it to be the only sufficient
> mechanism.

Working shorthand, updated: **"Versioned is not bound — and what's
missing is a causal link, not necessarily a specific binding schema."**

**Integrated Contribution 2 empirical verdict: NARROWED SUPPORT.** Both
named failure mechanisms (retroactive correction — primary experiment;
timestamp-precision ambiguity — this follow-up) are now empirically
demonstrated in a controlled, synthetic setting. The thesis is
simultaneously strengthened (a second, previously untested mechanism is
now confirmed) and narrowed (the necessary property is causal linkage in
general, not the specific binding schema this contribution names).

**Contribution 2 remains independently publishable**, under the updated
thesis statement above. **Contribution 2's empirical phase is CLOSED**:
no further pre-drafting empirical question is currently known to be a
must-have (a study combining both mechanisms, testing clock skew across
independent components, or testing unreliable/contested causal signals
would be legitimate future work, not a blocker to drafting — per the
explicit instruction governing this follow-up not to generate additional
experiments merely because more are possible). Drafting Contribution 2
should use the updated (causal-relation) thesis statement above, not the
binding-centric formulation that preceded this follow-up.
