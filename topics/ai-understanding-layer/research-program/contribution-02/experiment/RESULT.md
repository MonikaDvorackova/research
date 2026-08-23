# Result

1. **Did B outperform A?** Yes, clearly — on AC and AIA across every
   forward-drift case, and on TC specifically where policy/authority
   themselves drift (Cases 2, 4). Manipulation check passes.
2. **Did C outperform B?** Yes, but only on some cases, not all.
3. **On Temporal Correctness:** C beats B categorically on Cases 3, 8, 9
   (TC: B=0.00, C=1.00). C ties B on Cases 1, 2, 4, 5, 6, 7, 10 (both
   1.00).
4. **On False Historical Confidence:** C beats B on Cases 3, 8, 9 (FHC:
   B=0.50–1.00, C=0.00). Tied at 0.00 elsewhere.
5. **In which cases?** Cases 3 (isolated retroactive policy correction),
   8 and 9 (combined drift including retroactive correction). Not Case
   10 (concurrency) — see limitation below.
6. **Did the primary hypothesis survive?** Partially. H1 predicted the
   C-over-B advantage would concentrate in Cases 3, 8, 9, **and** 10. It
   concentrated in 3, 8, 9. Case 10 showed no gap — not because the
   mechanism is false, but because this implementation modeled the
   policy boundary with exact timestamps rather than injecting the clock
   imprecision the concurrency mechanism depends on. That was a disclosed
   implementation choice, made before execution, not a post hoc excuse.
7. **Strongest legitimate conclusion:** In this synthetic system, when a
   policy or authority record is retroactively corrected after a decision
   was made, a correctly implemented bitemporal query over a genuinely
   complete history can be confidently and silently wrong about which
   version actually applied — and an explicit, decision-time binding
   avoids exactly this failure, by construction. This is now an empirical
   result, not just a design argument.
8. **Strongest result against our thesis:** Case 10 shows B and C
   performing identically on the concurrency-ambiguity scenario the
   thesis's second mechanism depends on. As implemented, this run gives
   zero evidence for that half of the thesis. A more adversarial
   implementation (genuine clock/logging imprecision near the boundary)
   is required before that half can be claimed.
9. **Does Contribution 2 remain independently publishable?** Yes — the
   retroactive-correction result is a clean, non-trivial, disclosed-
   limitations-and-all empirical finding, and the concurrency gap is now
   a named, scoped, honestly-reported open question rather than an
   untested assumption.
10. **What should happen next?** A follow-up run of Case 10 with genuine
    timestamp/clock-precision fault injection (not a redesign of the
    matrix, hypotheses, or metrics — an alternate implementation of the
    one case the current design already flagged as open). This is future
    work requiring a new authorization, not performed here.
