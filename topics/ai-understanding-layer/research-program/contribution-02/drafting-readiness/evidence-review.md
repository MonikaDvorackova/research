---
id: note-contribution-02-drafting-evidence-review
title: "Contribution 2 Drafting Readiness — Experimental Evidence Review"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, drafting-readiness, evidence-review]
refs: [../experiment/RESULT.md, ../experiment/analysis/experiment-report.md, ../experiment/followup-case10/RESULT.md, ../experiment/followup-case10/analysis/experiment-report.md]
---

## Experimental Evidence Review

A non-advocacy summary of both completed experiments. No results are
restated with any spin beyond what their own raw data supports; both
"strongest support" and "strongest counterevidence" are given equal
prominence for each experiment, per the review's own requirement.

---

## Primary Experiment

**Research question** (`../experiment/experiment-design/research-question.md`):
given complete, independent version histories for policy, evidence,
authority, model, and context, does versioning alone suffice for
temporally correct reconstruction, or does explicit decision-time binding
materially improve it — specifically comparing Regime B (versioned,
unbound) against Regime C (versioned, bound), with Regime A (bare) as a
floor condition.

**Cases:** 10 structural cases, 11 decisions (`../experiment/results/`):
1 control, 5 forward-drift (isolated policy/authority/evidence/context/
model changes, non-retroactive), 1 isolated retroactive-drift, 2
combined-drift, 1 concurrency (which, as implemented, did not induce
genuine ambiguity — see the follow-up).

**B vs. C:**

| Category | B: TC / FHC | C: TC / FHC |
|---|---|---|
| control | 1.00 / 0.00 | 1.00 / 0.00 |
| forward-drift | 1.00 / 0.00 | 1.00 / 0.00 |
| retroactive-drift | 0.00 / 0.50 | 1.00 / 0.00 |
| combined-drift | 0.00 / 0.63 (avg) | 1.00 / 0.00 |
| concurrency | 1.00 / 0.00 | 1.00 / 0.00 |

**Where B succeeded:** every case without retroactive correction (control,
all five forward-drift cases, and — as implemented — the concurrency
case). B ≈ C exactly on all of these; a fully bitemporal, fully
event-sourced Regime B was not weakened to manufacture a gap.

**Where B failed:** the three cases involving retroactive correction
(Cases 3, 8, 9). In every one, B's temporally-correct-per-construction
bitemporal query returned a version other than the one ground truth says
the decision actually relied on.

**False Historical Confidence:** the primary experiment's sharpest single
result. On Cases 3, 8, and 9, B did not fail by abstaining — it failed by
confidently naming a concrete, wrong policy and/or authority version (FHC
0.50–1.00 on these cases; 0.00 everywhere else). C's FHC was 0.00 in
every case, no exception.

**Strongest support:** the categorical TC flip (1.00→0.00) on Cases 3, 8,
9, concentrated exactly where the theorized retroactive-correction
mechanism predicts and nowhere else — the cleanest possible confirmation
pattern the design's own pre-registered interpretation table anticipated
(row 1).

**Strongest counterevidence:** Case 10, as implemented, showed B and C
performing identically (both succeeding) on the one case built to test
concurrency ambiguity — because the implementation used exact,
non-fault-injected timestamps 60 seconds from the relevant boundary. This
was disclosed as a limitation before the follow-up, not discovered after.
Also notable: on Cases 3, 8, 9, B's *Authorization Correctness* (the
bottom-line GRANT/DENY outcome) was 1.00 despite TC being 0.00 — the
wrong policy version happened to produce the same authorization outcome
as the correct one. This is real counterevidence to any claim that the
mechanism has *practical* consequences for authorization outcomes in this
specific testbed, even though it has clear consequences for *historical
accuracy* (TC/FHC).

**Overall classification:** PARTIAL SUPPORT
(`../experiment/RESULT.md`).

---

## Case 10 Follow-up

**Research question** (`../experiment/followup-case10/research-question.md`):
under genuine, observationally-caused timestamp-precision ambiguity — not
retroactive correction — can complete version history alone recover the
actual decision context, or does something more (explicit binding, or any
other causal signal) provide information that cannot be inferred from
the available temporal record.

**Cases:** 6 cases (`../experiment/followup-case10/results/`): 1
no-ambiguity control, 3 isolated-dimension ambiguity (policy, authority,
model), 1 combined-dimension ambiguity, 1 negative control (F10-6: the
same ambiguity as the policy case, plus a non-binding causal consumption
event given to B only).

**B vs. C:**

| Case | B | C |
|---|---|---|
| F10-1 (control) | TC=1, FHC=0.00 | TC=1, FHC=0.00 |
| F10-2/3/4/5 (ambiguity, no causal signal) | TC=0 (or unscored dimension for F10-4), URR 0.33–0.67, **FHC=0.00** | TC=1, URR=1.00, FHC=0.00 |
| F10-6 (ambiguity + causal event on B) | TC=1, URR=1.00, FHC=0.00 | TC=1, URR=1.00, FHC=0.00 |

**Ambiguity behavior:** B's Ambiguity Detection Rate is 1.00 on every case
with a genuinely ambiguous dimension. Unlike the primary experiment, B
never produces a confidently wrong answer under this mechanism (FHC =
0.00 throughout this entire follow-up, for both regimes, on every case)
— a structurally different, and more honest, failure profile than the
primary experiment's retroactive-correction result.

**F10-6 negative control:** the single most consequential result across
both experiments for how the thesis must be stated. An ordinary,
non-binding causal consumption event — never framed, named, or
structured as a "decision binding" — resolves the same ambiguity Regime
C's binding resolves, with identical scores on every metric.

**Strongest support:** F10-2/3/5 show, cleanly, that with *no* causal
signal at all, complete version history genuinely cannot uniquely resolve
which version a decision consumed when a boundary falls inside the
observable timestamp window — and it fails by honestly saying so, not by
guessing.

**Strongest counterevidence** (against the *original*, binding-specific
formulation of the thesis — this is evidence *for* the narrowed
formulation, not against Contribution 2 as a whole): F10-6 directly
contradicts "explicit decision-time binding is uniquely necessary." Any
preserved causal relation resolves the ambiguity; binding is not special.

**Overall classification:** the follow-up's own six-case pattern does not
map onto a single primary-experiment-style label; its consequence,
combined with the primary experiment, is captured by the integrated
verdict below.

---

## What the combined experiments establish

1. In this synthetic, controlled testbed, complete version history
   (bitemporal, event-sourced, deliberately built stronger than typical
   real tooling) is **not sufficient** for temporally correct
   reconstruction under **two independent, named mechanisms**:
   retroactive correction (primary experiment) and observational
   timestamp-precision ambiguity (follow-up).
2. Under the first mechanism, the failure mode is **confidently wrong**
   answers (measurable False Historical Confidence). Under the second, the
   failure mode is (in this implementation) **honestly ambiguous**
   answers — these are different, independently worth reporting, failure
   profiles, not one undifferentiated "B fails" result.
3. Whatever closes both gaps must supply a **preserved causal relation**
   between the decision and the specific version it consumed. Regime C's
   explicit binding is one sufficient way to do this, demonstrated across
   both experiments without exception (FHC = 0.00 for C on every one of
   16 case-regime rows across both experiments). It is **not shown to be
   the only** sufficient way — F10-6 demonstrates an alternative that
   also works.
4. Versioning "some but not all" the right dependencies, or versioning
   without any causal signal, is not a strawman condition — Regime B in
   both experiments was deliberately built at or above the strength of
   real-world best practice, and still failed under the two tested
   mechanisms.

## What the combined experiments do not establish

1. **Prevalence or severity in real production systems.** Both testbeds
   are synthetic, small, and purpose-built. No claim about how often
   either mechanism occurs in practice, or how costly its consequences
   are there, follows from this evidence.
2. **That any specific schema (the minimal decision record as drafted) is
   optimal, minimal, or cost-effective to implement.** Both experiments
   test whether *a* binding closes the gap in principle, not whether this
   particular field set is the right one to standardize.
3. **Generalization across mechanisms not tested.** Clock skew across
   independent components, general multi-timeline concurrent ordering
   ambiguity, and unreliable or contested causal signals were all
   explicitly out of scope for the follow-up
   (`../experiment/followup-case10/research-question.md`).
4. **Anything about compliance, governance risk, or trustworthiness.**
   Neither experiment measured any outcome in this category; any such
   claim in a future draft would be unsupported by this evidence (see
   `claim-ledger.md`, claim 13).
5. **That the concurrency-ambiguity mechanism, as originally conceived by
   the primary experiment's Case 10, is real.** The follow-up tested a
   *related but distinct* mechanism (timestamp precision loss) with its
   own case design; it does not retroactively validate the primary
   experiment's original Case 10 construction, which remains, as
   originally reported, a case that did not test what it was built to
   test.

External-validity limitations are otherwise unchanged from
`../experiment/experiment-design/validity-and-confounders.md` and are not
restated here in full; they apply to both experiments without exception.
