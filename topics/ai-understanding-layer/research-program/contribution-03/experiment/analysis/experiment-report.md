# Experiment Report — Trajectory-Composition Experiment

## Question tested

Does per-decision reconstructability (Contribution 2's earned result:
Regime C makes every individual AI-mediated decision reconstructable)
**necessarily** compose into trajectory-level reconstructability once
decisions in a sequence depend on one another?

H0: yes, it composes. H1: no, not necessarily — local completeness can
coexist with global (cross-decision) ambiguity.

## What was built

Two regimes over six cases (`case-matrix.md`, `PRE-EXECUTION-MANIFEST.md`):

- **T1** — every decision individually carries complete, correct local
  facts (context, result, output/consumed values, timing) but no
  cross-decision relation field exists on the record type at all.
- **T2** — identical local facts, plus one additional field
  (`consumed_from_decision_id`) recording the true dependency edge.

`verify_t1_t2_local_equivalence` — run both as a pre-execution test and
as the first step of `run_experiment.py` itself — enforces that T1 and
T2 never differ on any local field, so any divergence in trajectory-level
outcomes cannot be attributed to a hidden local-information gap.

The investigator (`src/reconstruction.py`) is not a weak baseline: in T1
it actively infers a dependency wherever the local evidence uniquely
determines one (exact value match with no competing candidate, unique
latest timestamp among a "depends on most recent" decision's
predecessors), and returns AMBIGUOUS — never a guess — the moment two or
more candidates are equally consistent with the observable record.

## Result

Local Decision Reconstruction was perfect (1.00) in both regimes across
all 12 case×regime runs — confirming the experiment's own precondition
that any observed gap is not explained by a loss of local information.
Trajectory Identifiability was 1.00 under T2 (as designed: T2 resolves
every dependent edge by direct lookup) but only **0.33 (2/6)** under T1.
The four cases that failed under T1 — C3-2 (identical-value provenance),
C3-3 (branch/abstraction ambiguity), C3-4 (state-write ambiguity), C3-5
(concurrent/near-concurrent ordering) — are exactly the four built
around a cross-decision ambiguity mechanism; the control (C3-1) and
negative control (C3-6) both resolved correctly.

Critically, this is **honest ambiguity, not false confidence**:
Dependency Edge Accuracy = 1.00 and False Global Confidence Rate = 0.00
under T1. The investigator never returned a wrong UNIQUE answer — on
every case it could not resolve, it correctly said so
(Ambiguity Detection Rate = 1.00 against the four genuinely-ambiguous
edges).

## Interpretation

Per PRE-EXECUTION-MANIFEST.md's interpretation table, this run lands on
**B**: Trajectory Identifiability < 1.00 specifically on the
value-collision and order-timing cases, = 1.00 on the control and
negative control, with zero instance of category C (false confidence).
**H1 is supported**: per-decision reconstructability does not
necessarily compose into trajectory-level reconstructability, and the
gap is precisely the missing cross-decision relation — not a general
degradation of local information, and not a case where the investigator
was misled into a wrong confident answer.

This is a narrower, more favorable result than Contribution 2's own
finding. Contribution 2 found cases (e.g. Case 8, retroactive authority
correction) where a regime produced **false historical confidence** — a
wrong answer stated with unwarranted certainty. This experiment, testing
a structurally different mechanism (cross-decision composition rather
than within-decision temporal binding), found only honest ambiguity, no
false confidence, in six deliberately adversarial cases. That is a
genuine, disclosed asymmetry between the two contributions' results, not
a contradiction — the mechanisms are different and nothing in this
design guarantees false confidence would appear even if it exists for
some other trajectory-composition mechanism not tested here (see
Limitations).

## Prior-art interpretation

This result sits squarely inside, not outside, existing formalisms for
multi-step provenance:

- **Workflow provenance** (Buneman-style why/where-provenance, W3C
  PROV-DM) already distinguishes a record's own content from its
  derivation edges; T1 vs. T2 here is exactly that distinction, made
  operational for AI-decision trajectories specifically. The finding is
  not that provenance graphs are a new idea — it is a controlled
  demonstration that the specific object this research programme cares
  about (decision reconstructability) inherits the same local/global gap
  that provenance research already treats as basic.
- **Event sourcing / distributed tracing** (OpenTelemetry-style spans)
  solve exactly the T1→T2 gap in practice by attaching explicit parent
  references — which is structurally identical to this experiment's
  negative control (C3-6's `causal_trace_event`). The experiment
  reproduces, in miniature and under adversarial construction, why that
  parent-reference field is load-bearing rather than optional.
- **Process mining** discovers dependency structure post hoc from event
  logs precisely because logs like T1 (timestamps + local facts, no
  explicit edges) under-determine the true process graph when multiple
  cases could explain the same observed sequence — the same ambiguity
  mechanism as C3-2/3/4.
- **Diagnosability** (discrete-event systems) and **bisimulation**
  (concurrency theory) both formalize when two system executions are
  observationally indistinguishable; C3-2/3/4/5's AMBIGUOUS outcomes are
  cases where two candidate predecessor decisions are, from the
  observable record alone, exactly such an indistinguishable pair.
- **Compositional verification**'s standard caution — that
  component-level properties do not automatically imply system-level
  properties — is the general form of what this experiment demonstrates
  for one specific property (reconstructability) and one specific
  system class (AI-decision trajectories).

None of this is being claimed as a new formal result. The contribution,
if any, is the controlled empirical demonstration for the specific,
narrow object this research programme is about — not a new theorem.

## Article 3 consequence

A technical/practitioner article can survive from this result, but only
under a narrow framing: **trajectory reconstructability is not
guaranteed by decision-level reconstructability alone; the missing
ingredient is an explicit, retained cross-decision relation, not more
local detail.** This is consistent with, and should be framed as an
extension of, Contribution 2's "retained is not consumed" thesis — same
family of finding (structural retention without the specific relation
that use requires), one level up (trajectory vs. single decision).

Per this pass's binding instruction: **no resurrection of "Understanding
Layer" or "capability-vs-understanding" framing.** If Article 3 is
written, its title and thesis must use "trajectory reconstructability"
or "compositional reconstructability" only.

## O'Reilly consequence (recorded, not drafted)

A future synthesis chapter could note that per-decision auditability
guarantees (however well-engineered) do not by themselves certify that
an end-to-end AI-mediated workflow can be reconstructed after the fact;
teams building for auditability need to budget explicitly for capturing
and retaining cross-decision dependency edges, not just per-decision
records, and should expect the two to require separate engineering
effort rather than assuming one implies the other.

## Scientific limitations

- Synthetic testbed: six hand-constructed cases, not a sample from any
  real system; no claim about prevalence of these mechanisms in
  production AI-decision systems.
- No statistical inference is appropriate or attempted — this is a
  controlled demonstration (existence of a composition gap under
  specific, disclosed conditions), not a measurement of a rate in the
  wild.
- The dependency-graph definition (`consumed_input_value` /
  `output_value` matching, `depends_on_most_recent` ordering) is one
  reasonable operationalization of "decision dependency," not the only
  possible one; other definitions might narrow or widen the observed
  gap.
- Workflow-provenance and distributed-tracing systems may already solve
  this exact mechanism in practice (see Prior-art interpretation above)
  — the finding is that the gap exists and is structurally reproducible
  for AI-decision trajectories, not that no engineering solution exists.
- No claim is made about human understanding, comprehension, or
  cognition at any point — "reconstructability" here is strictly the
  narrow, previously-defined technical property from Contribution 2,
  extended to trajectories.
- Only two ambiguity mechanisms were tested (value-collision,
  order/timing). Other plausible mechanisms (e.g., partial/lossy
  propagation, many-to-one dependency fan-in) were not constructed and
  might behave differently, including possibly producing false
  confidence (category C) where this run found none.
