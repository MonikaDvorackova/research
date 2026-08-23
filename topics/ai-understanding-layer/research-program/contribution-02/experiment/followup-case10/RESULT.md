# Follow-up Case 10 — Result

1. **Did the mechanism (timestamp-precision ambiguity) manifest for B?**
   Yes, cleanly, in all four cases built to test it (F10-2, F10-3, F10-4,
   F10-5).
2. **Did C outperform B on those cases?** Yes — TC and URR are 1.00 for C
   and lower for B on every one (TC: 0/1 on three of four; URR: 0.33–0.67
   vs. 1.00 on all four).
3. **Did B fail honestly or falsely?** Honestly. False Historical
   Confidence is 0.00 for B on every single case in this run — it
   reported `AMBIGUOUS`, correctly, rather than guessing. Ambiguity
   Detection Rate = 1.00 on all four ambiguous cases.
4. **Negative control (F10-6):** B, given one causal consumption event
   never called "binding," matched C exactly on every metric.
5. **Strongest result supporting the thesis:** F10-2/F10-3/F10-5 — with
   no causal signal at all, complete version history genuinely cannot
   resolve which version applied; binding resolves it.
6. **Strongest result against the specific "binding" formulation:**
   F10-6 — an ordinary, non-binding causal event resolves the same
   ambiguity just as well. The requirement is a causal relation, not
   specifically Regime C's binding schema.
7. **Which formulation survives:** **Formulation B** — some preserved
   causal relation between decision and consumed version is required;
   explicit decision-time binding is one sufficient, general, buildable
   implementation of that relation, not the only one.
8. **Does this change the primary experiment's results?** No. Cases 1–9
   of the primary experiment are untouched; primary commit
   `31c58ddc6e95b5f66153b4c2dd35d91f4ae8e725` remains the record of that
   run. This follow-up only closes the one gap that run's own report
   disclosed (Case 10 never actually tested concurrency ambiguity).
9. **Integrated Contribution 2 verdict:** **NARROWED SUPPORT.** Both
   named failure mechanisms (retroactive correction; timestamp-precision
   ambiguity) are now empirically demonstrated in this synthetic testbed.
   The thesis itself narrows: from "explicit binding is required" to "a
   preserved causal relation from decision to consumed version is
   required, and explicit binding is one general way to build it."
10. **Contribution 2 empirical phase:** **CLOSED.** No further
    pre-drafting empirical question is currently known to be a
    must-have. (A third study combining both mechanisms, testing clock
    skew, or testing unreliable causal signals would be interesting
    future work, not a blocker — per the explicit instruction not to
    generate more experiments merely because more are possible.)
