---
id: note-contribution-03-earned-premises
title: "Contribution 3 — What Contributions 1 and 2 Actually Earned"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-03, earned-premises]
refs: [../article-01-decision-level-control/novelty-audit.md, ../contribution-02/article/FINAL-ACCEPTANCE.md]
---

## Earned Premises for Contribution 3

Contributions 1 and 2 may be used as premises here only to the extent
their own final, accepted materials actually establish — not to the
extent Source A's framing assumes they will.

## Contribution 1 — Decision-Level Control

**EMPIRICALLY EARNED:** Nothing. Contribution 1's evidence base is
architecture/design argument and adversarial prior-art comparison
(`../article-01-decision-level-control/novelty-audit.md`), not a
controlled experiment. No claim from Contribution 1 is empirically
earned in the sense Contribution 2's experiments earn a claim.

**CONCEPTUALLY EARNED:**
- The output/decision distinction (an AI-derived output is not
  automatically an authorized state transition) survives adversarial
  prior-art testing (Position B: new synthesis, not new mechanism, per
  `../research-program/contribution-boundaries.md`).
- Decision-time enforcement (a gate checking evidence against policy
  before a decision takes effect) is a useful, explicit systems boundary
  — conceptually argued and adversarially reviewed, not measured.

**DOES NOT EARN:** Any claim about historical reconstruction, knowledge
preservation, or system-wide "understanding" — Contribution 1 is
explicitly scoped to decision-time control, orthogonal to preservation
(`../notes/intellectual-progression.md` Task 7's finding, which this
review's `ai-systems-review.md` independently reconfirmed for assurance
cases: enforcement is a downstream consumer of evidence, not a
preservation mechanism).

## Contribution 2 — Preservation & Reconstruction

**EMPIRICALLY EARNED**, precisely, per
`../contribution-02/article/FINAL-ACCEPTANCE.md`'s frozen contribution
statement:
- Retained version history does not guarantee unique reconstruction of
  which versions a historical decision consumed — demonstrated for two
  distinct, named mechanisms (retroactive correction; observational
  timestamp-precision loss), in a synthetic, controlled testbed.
- The property required to close the demonstrated gap is a **preserved
  consumption relation**, not any one named architecture — explicit
  decision-time binding is one sufficient implementation, not the only
  one (the F10-6 negative control).
- A reconstruction that is honestly ambiguous ("I cannot uniquely
  determine which version applied") is a categorically different, better
  failure mode than one that is confidently wrong — measured directly via
  False Historical Confidence.

**CONCEPTUALLY EARNED:**
- The C/D/E/F/G problem decomposition and the replay-vs-reconstruction
  distinction (`../contribution-02/collision-tests.md` Task 6) — not
  found named this way in the prior art that contribution surveyed.
- The finding, reused directly in this review's `provenance-review.md`,
  that reconstruction (recovering what happened) and explanation/
  justification (why it was valid) are separable, and existing
  mechanisms close the former far more completely than the latter.

**DOES NOT EARN:**
- Any claim about system behavior generally, only about a single,
  discrete, well-defined historical decision (`../contribution-02/article/FINAL-ACCEPTANCE.md`'s
  explicit non-claim: no prevalence claim, no generalization to
  production systems, no universal-mechanism claim).
- Any claim that the retained-vs-consumed gap generalizes from decisions
  to **system behavior over time**, **behavioral envelopes**, or
  **human/operator knowledge about a system** — Contribution 2's own
  frozen scope is explicit and narrow, and generalizing beyond it is
  exactly the missing premise `../recommended-program.md` flagged as Q3
  and this review's `residual-gap-analysis.md` must not silently assume.
- Any claim that explicit binding, or any specific schema, is required —
  directly and explicitly rejected by Contribution 2's own negative
  control.

## What this means for Contribution 3's argument, if it proceeds

Contribution 3 cannot say "Contributions 1 and 2 showed that AI systems
generally are becoming unreconstructable and uncontrollable." The
honest, earned premise is much narrower: **one specific, synthetic,
decision-shaped instance of the reconstruction problem was tested and
found real, under two named mechanisms, and closing it requires a
consumption relation, not a specific architecture.** Whether this
narrow, decision-specific finding generalizes to system-wide
"understanding" is precisely the missing premise this review's
`residual-gap-analysis.md` addresses directly rather than assumes.
