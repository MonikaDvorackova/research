---
id: note-contribution-02-empirical-next-step
title: "Contribution 2 — Empirical Next Step (Design Only, Not Run)"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, empirical-design, falsifiability]
refs: [novelty-verdict.md, minimal-decision-record.md, ../empirical-program.md]
---

## Contribution 2 — Empirical Next Step

Scope: Tasks 12–14. Per the brief, this document formulates the empirical
question and critiques two candidate methods (repository audit; controlled
failure experiment). **No experiment is run here.** This refines, rather
than replaces, `../empirical-program.md`'s Programme 1 and Programme 2,
using the sharper distinctions this audit produced — most importantly, the
binding-vs-versioning distinction from `collision-tests.md` Objection 8,
which the earlier design did not yet have available.

---

## Task 12 — The empirical question, improved

**Original candidate (from the brief):**

> Given the artifacts normally preserved by a production ML system, can an
> independent investigator reconstruct whether a historical decision
> satisfied the policy and evidence requirements applicable at decision
> time?

**Improvement required by this audit:** the original candidate treats
preservation as roughly binary ("normally preserved" vs. not). The audit's
central finding — that versioning existing elsewhere is not the same as a
decision-time binding being recorded — means the experiment must distinguish
at least **three** preservation regimes, not two, or it will not be able to
tell whether any observed reconstruction failure is due to missing
artifacts (the naive hypothesis) or missing bindings (this audit's sharper
hypothesis). A two-condition design confounds these.

**Improved formulation:**

> Given a decision D, evidenced and authorized at t0 under one of three
> preservation regimes — (i) no dependency versioning beyond the bare
> decision outcome, (ii) dependencies (policy, retrieval corpus, model,
> authority) independently versioned elsewhere but not bound to D at t0,
> or (iii) dependencies versioned **and** explicitly bound to D at t0 via a
> minimal decision record — does realistic drift between t0 and t1 (policy
> revision, retrieval-corpus update, model rotation, authority
> reassignment) prevent a blinded investigator at t1 from correctly
> answering the justification question G, and does the size of that failure
> differ between regimes (ii) and (iii) specifically, not just between (i)
> and (iii)?

The (ii)-vs-(iii) comparison is the experiment's most important addition
relative to `../empirical-program.md`'s original two-condition sketch: it
isolates the binding property itself, rather than conflating "some
preservation" with "sufficient preservation."

---

## Definitions

- **Unit of analysis:** A single decision D, evidenced and authorized in a
  minimal synthetic testbed (reusing Contribution 1's own running example —
  a model-promotion or agent tool-call decision — per
  `../empirical-program.md`'s existing choice not to use a real production
  system initially, for the same access/privacy reasons already
  documented there).
- **Baseline preservation configuration:** Regime (i) — the decision outcome
  and its immediate evidence are recorded; no separate versioning of policy,
  retrieval corpus, model, or authority beyond what ordinary operation would
  produce incidentally (e.g., git history for code, but no bitemporal
  policy store, no retrieval-corpus snapshotting).
- **Intermediate preservation configuration (new relative to
  `../empirical-program.md`):** Regime (ii) — every dependency is
  independently versioned (a real policy version history exists; the
  retrieval corpus is snapshotted; the model registry retains prior
  versions; authority/role assignments have their own history) but **no
  decision record pins which version applied to this specific decision.**
  An investigator must infer the applicable version, e.g., by timestamp
  proximity — exactly the failure mode Objection 8 predicts.
- **Enriched preservation configuration:** Regime (iii) — regime (ii) plus
  an explicit minimal decision record (per `minimal-decision-record.md`)
  binding D to specific valid-time slices of each dependency at t0.
- **Perturbation / drift introduced between t0 and t1:** A condition matrix
  varying which dependencies drift (prompt template edited in place vs.
  versioned; retrieval corpus updated vs. snapshotted; policy revised,
  including at least one **retroactive** revision — a policy recorded after
  t0 but backdated to an effective time before t0, specifically to test the
  transaction-time/valid-time confound identified in
  `temporal-semantics.md`; model rotated; authority reassigned).
- **Reconstruction task:** A blinded investigator (a person or a specified
  evaluation protocol, not told which regime produced the retained
  artifacts) is asked to state: (a) which evidence was considered, (b)
  which policy version applied, (c) who/what had authority, and (d) why D
  was judged valid given (a)–(c).
- **Success criteria:** The investigator's answer to each of (a)–(d)
  matches ground truth fixed at design time — including, critically, that a
  retroactively-corrected policy is not silently substituted for the
  version the decision-maker actually relied on at t0 (the specific error
  mode `temporal-semantics.md` identifies as possible even under full
  bitemporal completeness).
- **Failure criteria:** Any of (a)–(d) cannot be answered, is answered with
  the wrong version/authority (a **false-confidence** failure, distinct
  from and more concerning than an acknowledged inability to answer), or is
  answered correctly only by the investigator's own inference/guesswork
  rather than from a recorded binding.
- **Measurable outcome:** A reconstruction-completeness score per (a)–(d),
  reported separately for regimes (i), (ii), and (iii), with the (ii)-vs-(iii)
  delta reported as the headline measure — this is the delta the original
  `../empirical-program.md` design could not isolate.
- **Possible confounders:** Investigator skill/inference ability (mitigated
  by blinding and a fixed scoring rubric, not investigator judgment alone);
  testbed artificiality (the domain is synthetic, so external validity to
  real production systems is explicitly not claimed — see the repository
  audit critique below for why a real-system study is not a viable
  substitute either, at least initially); scoring-rubric leakage (the
  rubric must be fixed before any regime's artifacts are inspected, to avoid
  post hoc rationalization of what "counts" as correct).

---

## Task 13 — Does the repository-audit idea survive for Contribution 2?

**No — rejected, consistent with and sharpened beyond
`../empirical-program.md`'s own redesign note.**

- Public repositories can show whether **code-visible** governance
  artifacts exist (a versioned prompt store, a bitemporal policy schema, a
  decision-record-writing call in the code) — this is a legitimate, if
  weak, proxy for Contribution 1's claims (which are about structural,
  code-visible patterns).
- For Contribution 2 specifically, the object of interest — whether a
  **specific runtime decision** was bound to the specific versions of
  policy/evidence/authority that applied at its own decision time — is not
  discoverable from a static repository at all. That binding, if it exists,
  lives in runtime databases, observability backends, or decision-record
  stores that are essentially never included in a public code repository,
  for reasons unrelated to whether the practice exists (privacy, size,
  operational separation of runtime data from source code).
- **Consequence:** a repository audit measures **absence of the pattern
  from public source code**, not **absence of the pattern in production
  behavior**. These are different claims, and conflating them risks a
  specific, avoidable error: concluding "most systems don't bind decisions
  to temporal context" when the true, supportable conclusion would only be
  "most public repositories don't expose code that does this," which is
  compatible with many production systems doing it via infrastructure never
  visible in the repository at all (e.g., a managed policy service with its
  own internal bitemporal store).
- **Rejected as the primary empirical method for Contribution 2.** The
  controlled failure/reconstruction experiment above is the correct primary
  method, for the same reason `../empirical-program.md` already concluded,
  now confirmed rather than merely asserted: Contribution 2's central claim
  is about a causal, testable property (does drift break reconstruction,
  and does binding fix it) that an observational code audit cannot address
  even in principle.

---

## Task 14 — Do controlled failure experiments survive, and what can they not prove?

**Survive, with the three-regime refinement above; critiqued explicitly
below.**

**What the experiment (as refined) can support:**
- Whether a reconstruction gap exists at all under realistic drift (regime
  i vs. iii).
- Whether the gap is attributable specifically to missing bindings rather
  than missing artifacts (the new regime ii vs. iii comparison) — this is
  the experiment's main value-add over the original design and the direct
  empirical test of this audit's central finding.
- Which specific dependency's drift (prompt, corpus, policy, model,
  authority) contributes most to reconstruction failure — not knowable in
  advance from the conceptual audit alone.
- Whether retroactive policy correction specifically produces
  false-confidence failures even under full bitemporal completeness (a
  distinct, sharper claim than "reconstruction fails," and one this audit's
  `temporal-semantics.md` predicts but has not tested).

**What it cannot prove, stated as explicitly as the brief requires:**
- **External validity beyond the synthetic testbed.** A finding here does
  not establish that real production systems exhibit the same failure
  rates or the same relative importance of dependency types — only that
  the mechanism is real and measurable in a controlled setting. A follow-up
  study using a real (consenting, access-permitted) production system would
  be required to generalize, and is explicitly out of scope for this next
  step.
- **That any specific proposed schema (the minimal decision record as
  drafted, or an AIGov-Core-style implementation) is the right or only way
  to close the gap** — the experiment tests whether binding closes the
  gap in principle, not whether this particular field set is optimal, minimal,
  or cost-effective to implement at scale.
- **Cost or practicality of adoption.** The experiment is silent on how
  expensive, in engineering effort, it is to retrofit binding into existing
  AI/ML tooling — a real and unaddressed question for any future
  implementation-focused work.
- **What the experiment actually tests, precisely stated:** primarily
  **reconstruction completeness** and, via the new regime (ii)-vs-(iii)
  comparison, **provenance-binding sufficiency** specifically. It tests
  **temporal correctness** only if the scoring rubric explicitly checks
  that the investigator identified the version that was *actually relied
  upon at t0*, not merely *a* plausible version retrievable from history —
  this must be built into the rubric deliberately (per the retroactive-policy
  condition above), or the experiment will silently conflate retrievability
  with correctness and overstate what regime (iii) achieves.

**Priority relative to the repository audit:** Programme 2 (the controlled
experiment, as refined here) should proceed; the repository audit should
not be attempted for Contribution 2 in any form. This aligns with, and
sharpens, `../empirical-program.md`'s own priority ordering.

---

## Summary of what changed relative to `../empirical-program.md`

1. Two preservation conditions become three, specifically to isolate the
   binding property from mere artifact versioning (Objection 8's finding —
   not available when the original design was written).
2. A retroactive-policy-correction perturbation is added, to test the
   transaction-time/valid-time confound identified in
   `temporal-semantics.md` (also not available previously).
3. The scoring rubric is required to check *temporal correctness*
   (identifying the version actually relied upon), not just *retrievability*
   of some plausible version — otherwise the experiment cannot distinguish
   the sharper failure mode this audit identifies from ordinary
   incompleteness.
4. The repository-audit rejection is sharpened from "less novel/motivated"
   (the original framing) to "cannot in principle observe the object of
   interest" (runtime binding is not code-visible) — a stronger and more
   specific reason to reject it, not merely a preference ordering.
