---
id: note-contribution-03-diagnosability-review
title: "Contribution 3 — Diagnosability and System Identification Collision Review"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-03, diagnosability, system-identification]
refs: [operationalization-review.md, source-ledger.md]
---

## Purpose

The first review's `observability-review.md` did not develop diagnosability
or system identification. This is the single most important collision
test in this narrow pass, per the authorizing task's own assessment
("this may be a stronger collision than generic observability").

## Diagnosability, formally

Diagnosability is a precise, decades-old property of partially-observable
discrete-event systems: **"the occurrence of a faulty event can be
determined after a finite number of subsequent events... by observing
the generated output sequence"** [S30]. It originates in a formal
definition for finite-state machines and has since been extended to
fuzzy discrete-event systems, labeled automata, open systems via game
structures, and intermittent-fault variants [S30][S31] — an active,
continuously-developed formal literature, not a historical curiosity.

**Direct collision with reconstructability (R).** Contribution 2's own
object — "can an investigator determine, from retained records, which
specific version a decision consumed" — is structurally a diagnosability
question: replace "faulty event" with "the true consumed version among
several candidates," replace "observed output sequence" with "the
retained history a regime provides," and the definitions align almost
exactly. Contribution 2's own AMBIGUOUS/CORRECT_UNIQUE/WRONG_UNIQUE
classification (`../contribution-02/experiment/followup-case10/src/scoring.py`)
is, in diagnosability's own vocabulary, a **diagnosability verdict for a
specific system model**: Regime B is not diagnosable with respect to
the "which version" fault-like event under retroactive correction or
observational ambiguity; Regime C is diagnosable by construction (the
binding record is exactly the extra observation that restores
diagnosability).

**Consequence.** Contribution 2's central empirical finding can be
restated, without loss, in the vocabulary of a formal field that
predates this programme by decades. This does **not** invalidate
Contribution 2 — its contribution was never claimed to be new formal
theory, and `../contribution-02/article/FINAL-ACCEPTANCE.md`'s frozen
contribution statement already avoids claiming novel mechanism or
architecture. But it does mean: **if Contribution 3 wants to claim
"reconstructability" as part of a new system-level property, it must
either (a) explicitly position itself as applying diagnosability theory
to a new object class (AI-mediated multi-component decisions), citing
diagnosability directly, or (b) concede the term is already someone
else's formal property, correctly used.** Option (a) is a legitimate,
modest synthesis move — matching this whole programme's established
pattern (new synthesis, not new mechanism) — but it is not new theory
and must not be presented as such.

## Diagnosability vs. observability: genuinely distinct, confirmed

A system can be diagnosable without being fully observable (only the
fault-relevant distinction needs to be recoverable from observations,
not the complete state), and observable without being diagnosable with
respect to a specific fault class (full state recovery does not by
itself guarantee two fault-vs-no-fault trajectories remain
distinguishable under the available observation function) [S30][S31].
**This confirms R and O are genuinely separable dimensions**, not
redundant restatements of one property — a positive finding for the
vector model in `operationalization-review.md`, even though neither
dimension is itself new.

## System identification, and why it does not collide with R

System identification is "the art and science of building mathematical
models of dynamic systems from observed input-output data," to support
**prediction of future system responses** [S32]. This is Level 5
(behavioral envelope) territory, not Level 4 (historical-instance)
territory: system identification asks "what is this system's general
input-output behavior," never "which specific version did this one past
decision consume." **No collision with Contribution 2's object found** —
this confirms system identification is the correct existing name for
candidate dimension B (behavioral predictability), and that B is a
different question from R (reconstructability), at a different level of
analysis, correctly kept separate in the collision matrix.

## Verdict

Diagnosability is the **strongest single formal collision found across
both research passes** for the reconstructability dimension specifically
— stronger than the generic observability collision the first pass
identified, because it is a precise match for the specific
"determine-which-of-several-candidates" structure Contribution 2 actually
tested, not merely an adjacent concept. Any future Article 3 material
touching reconstructability must cite and position against diagnosability
theory directly, not merely observability or provenance.
