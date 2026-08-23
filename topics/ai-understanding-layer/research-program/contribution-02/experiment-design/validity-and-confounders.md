---
id: note-contribution-02-experiment-validity
title: "Contribution 2 Experiment — Threats to Validity"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, experiment-design, validity, threats]
refs: [preservation-regimes.md, metrics-and-scoring.md]
---

## Threats to Validity

Per the brief's instruction to be severe here — this section is written to
find problems, not to reassure.

### Construct validity

**Are we actually measuring historical decision reconstruction?**

Only in a narrowed, structural sense. The eight-question schema
(`reconstruction-task.md`) operationalizes reconstruction as "correctly
naming the specific versions/values bound to a decision," which is the
scope `../minimal-decision-record.md` deliberately settled on. A real
investigator's reconstruction task can be more open-ended — exploring
unanticipated context, questioning whether the *policy itself* was
reasonable, or discovering a dependency nobody thought to version. This
experiment does not, and cannot, test reconstruction in that fuller sense.
**Mitigation:** claims drawn from this experiment must be scoped explicitly
to "structured reconstruction of the fields specified in
`../minimal-decision-record.md`," never generalized to "AI decisions are
[not] reconstructable" as an unqualified statement.

### Internal validity

**Does the B-vs-C difference isolate binding, and nothing else?**

This is the threat the B-vs-C information-equivalence table
(`preservation-regimes.md`) is built to control, and it holds by
construction for the *data* each regime provides. The remaining risk is in
the **deterministic algorithms**, not the data: if Regime B's as-of-t0
query procedure is specified as a weak or naively-implemented algorithm
(e.g., "use the most recently recorded row" instead of a correct
valid-time interval match), an observed B-vs-C gap would reflect algorithm
quality, not information availability — a confound that would invalidate
the experiment's central claim. **Mitigation:** `reconstruction-task.md`
and `implementation-spec.md` specify Regime B's algorithm as the
*objectively correct* use of bitemporal query semantics (a genuine
valid-time interval match, not a heuristic shortcut) — implementers must
not weaken this algorithm to make Regime C look better; doing so would be
exactly the researcher-bias failure mode addressed below.

### External validity

**Does a synthetic test system generalize to real production AI?**

Not established by this experiment, and not claimed to be. The synthetic
"Tier-2 Access Advisor" (`experimental-system.md`) has a small, fixed
number of cleanly delineated dependencies. Real agentic AI systems have
higher-dimensional, less cleanly separable context (overlapping retrieval
sources, cascading tool calls, ambiguous authority chains). A result here
establishes that the mechanism is **real and measurable in a controlled
setting** — it does not establish prevalence, severity, or even
directionality of the same effect in a real production system.
**Required follow-up, explicitly out of scope here:** a subsequent study
using a real, consenting production system, which `../empirical-program.md`
already flags as a separate, later undertaking.

### Ecological validity

**Are the three preservation regimes realistic?**

- Regime A matches a genuinely common pattern (no history retained at
  all) — realistic.
- Regime B is designed to match a mature ML platform using bitemporal
  policy/authority storage plus solid event-sourced request logging **but
  without deliberate per-decision binding discipline** — this is a
  plausible, not hypothetical, configuration (it is, in fact, close to
  what MLflow-plus-a-config-service tooling gives you today, per
  `../prior-art-audit.md`), though it is more disciplined about bitemporal
  storage than most current AI tooling actually is, which the audit
  confirms is not built this way by default. **This makes Regime B, if
  anything, more favorable to H0 than a typical real system would be** —
  a deliberate, disclosed choice that strengthens rather than weakens the
  experiment's fairness to the null hypothesis.
- Regime C is realistic as an achievable engineering target (an in-toto-
  shaped predicate populated per `../minimal-decision-record.md`) but is
  **not** currently standard practice anywhere identified in the prior-art
  audit — it should be described as "buildable with today's mechanisms,"
  not "commonly deployed."

### Researcher bias

**Are we designing C to win?**

Addressed directly by three controls, stated so they can be checked
independently later: (1) the information-equivalence table
(`preservation-regimes.md`) is a falsifiable claim in itself — anyone can
verify C adds no new underlying facts; (2) the pre-registered
interpretation table (`preregistered-interpretation.md`) commits, in
advance, to specific result patterns that would count as evidence *against*
the thesis, including the single most damaging possible result
(`metrics-and-scoring.md`, "what would specifically kill the thesis");
(3) Regime B is deliberately specified as strong (genuinely bitemporal,
genuinely event-sourced) rather than weak, precisely to prevent the
comparison from being won by under-resourcing the competitor. The residual
risk — that the *case matrix itself* was chosen to include disproportionately
many cases where B is expected to fail — is addressed by including four of
ten cases (2, 4, 6, 7) specifically constructed as cases where B is
expected to **succeed**, deliberately built into the design rather than
added defensively after the fact.

### Prior-art equivalence

**Is Regime C simply an existing pattern (PROV/in-toto) implemented
correctly?**

Yes, conceded directly and in full in `preservation-regimes.md`'s
dedicated PROV and event-sourcing sections. This experiment does not test
representational novelty — `../novelty-verdict.md` already settles that
question (no new mechanism). It tests whether the **discipline** of
applying these existing mechanisms at decision time, with version-identifier
references rather than raw values, is empirically consequential under
realistic drift. If the experiment shows no measurable consequence, the
honest conclusion is that this discipline, while conceptually distinct, is
not behaviorally load-bearing — pushing the programme's verdict toward
"framing only" (Verdict C in `../novelty-verdict.md`), not toward denying
the prior-art collision.

---

## Manipulation check (required before drawing thesis conclusions)

Before interpreting any B-vs-C difference as support or non-support for
H1, verify: does **Regime A** perform measurably worse than **both** B and
C on the forward-drift cases (2, 4, 6, 7)? If Regime A does not fail there,
the case matrix does not actually introduce enough drift to be
discriminating, and no conclusion about B vs. C can be drawn from that
case until the drift magnitude is increased. This check must be run and
reported before any H1/H0 conclusion, per `preregistered-interpretation.md`.
