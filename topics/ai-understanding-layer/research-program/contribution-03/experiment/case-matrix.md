---
id: note-contribution-03-experiment-case-matrix
title: "Contribution 3 Experiment — Case Matrix"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-03, experiment, case-matrix]
refs: [research-question.md]
---

## Two distinct ambiguity mechanisms, not one

Per the requirement that ambiguity arise from missing cross-decision
relations, not from missing or degraded local records, this matrix uses
exactly two structurally distinct mechanisms, each realized in more than
one case so no single case's numbers carry the whole design:

- **Value-collision mechanism** (C3-1, C3-2, C3-3, C3-4, C3-6): a later
  decision's `consumed_input_value` is matched against every earlier
  decision's `output_value`. If exactly one match exists, the edge is
  unique. If two or more earlier decisions produced the same value, the
  edge is genuinely ambiguous from local records alone — the record
  cannot say *which* of the value-producing decisions was actually
  consumed, only that some decision produced a value equal to what was
  read.
- **Order/timing mechanism** (C3-5): a later decision's dependency rule
  is structural ("consumed the most recently completed prior decision"),
  not value-based. Ambiguity arises when two candidate predecessors'
  *observable* (precision-truncated) timestamps cannot be ordered,
  reusing the same observational-precision-loss principle Contribution
  2's follow-up already validated as a genuine, non-manufactured source
  of ambiguity — applied here to inter-decision order instead of
  intra-decision version validity.

## Case matrix

| Case | Mechanism | Decisions | Ground truth edge | Expected T1 | Expected T2 |
|---|---|---|---|---|---|
| **C3-1** — fully identifiable control | Value-collision, no actual collision | D1(out=10) → D2(in=10) | D2←D1 | Unique, correct (only one value match exists) | Unique, correct |
| **C3-2** — identical-value provenance ambiguity | Value-collision | D1(out=7), D2(out=7, independent) → D3(in=7) | D3←D1 | **Ambiguous** (D1, D2 both match) | Unique, correct |
| **C3-3** — branch/abstraction ambiguity | Value-collision (boolean-valued) | D1(out=True, branch A), D2(out=True, branch B, independent) → D3(in=True) | D3←D2 | **Ambiguous** (D1, D2 both match) | Unique, correct |
| **C3-4** — state-write ambiguity | Value-collision (shared-state framing) | D1(writes state=active), D2(writes state=active, independent) → D3(reads state=active) | D3←D1 | **Ambiguous** (D1, D2 both match) | Unique, correct |
| **C3-5** — concurrent/near-concurrent dependency ambiguity | Order/timing | D1(true t0 = boundary+0.2s), D2(true t0 = boundary+0.6s, both truncate to the same observable second) → D3(depends on most-recent) | D3←D2 (true t0 later) | **Ambiguous** (observable timestamps identical) | Unique, correct |
| **C3-6** — negative control | Value-collision, structurally identical to C3-2, plus one ordinary trace field on T1 only | D1(out=7), D2(out=7, independent) → D3(in=7, **plus** an ordinary `causal_trace_event` field naming D1) | D3←D1 | **Unique, correct** — T1 matches T2 exactly once given this one ordinary field | Unique, correct |

No combined-ambiguity case is included: six cases, covering both
mechanisms plus a clean control and a negative control, are judged
sufficient to test H0/H1 without combinatorial expansion, mirroring
Contribution 2's own ten-case ceiling rationale at a smaller scale
appropriate to this narrower question.

## Design notes

- **C3-1 is the manipulation check**: if T1 fails here, the case
  construction itself is broken (a decision's own local record already
  uniquely determines its predecessor with no ambiguity mechanism
  present) — not evidence about H0/H1.
- **C3-2, C3-3, C3-4 are the same underlying mechanism**, deliberately
  repeated with different narrative framing (raw value, boolean
  precondition, shared mutable state) specifically so the result does
  not rest on one handcrafted scenario — matching this task's own
  instruction not to let the result depend on a single case.
- **C3-5 is mechanistically independent of C3-2/3/4** — it would survive
  even if the value-collision mechanism turned out to be an artifact of
  case construction, and vice versa.
- **C3-6 is mandatory and decisive for interpretation**: if it resolves
  T1 to match T2, the correct reading is "cross-decision provenance/
  dependency relation is the relevant property," not "a new
  trajectory-binding architecture is required" — directly testing
  whether this experiment's own findings would repeat Contribution 2's
  F10-6 pattern one level up.
