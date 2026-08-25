# When Reconstructable Decisions Produce an Unreconstructable System

*Every individual step in an AI-mediated workflow can be perfectly auditable, and the trajectory those steps form can still be ambiguous — because the property that lets you audit one decision is not the property that lets you connect it to the next one.*

## Every Decision Is Reconstructable. The System Still Isn't.

Take a four-step AI-mediated workflow: D1 → D2 → D3 → D4. A retrieval step, a scoring step, a policy step, an action step — the exact shape doesn't matter. Assume your logging is as good as logging gets. For every one of the four decisions, you retain the exact model version, the exact policy version, the exact evidence it evaluated, the exact authority under which it ran, and its own local output. Nothing was dropped. Nothing was overwritten. Each decision, examined on its own, is fully reconstructable: an investigator looking only at D3's own record can determine, without doubt, what D3 consumed and why it did what it did.

Now ask a different question: which earlier decision actually produced the input D4 used?

If two earlier decisions — say D1 and D2 — happened to produce observationally identical output, and nothing in the retained record says which one D4's input actually came from, the question has no answer. Not a hard-to-find answer — no answer. D4's own record is complete. D1's own record is complete. D2's own record is complete. Every local fact anyone could ask for is sitting right there, correct and unambiguous. And the one fact that would let you reconstruct the trajectory — which of D1 or D2 fed D4 — is simply not present in any of those records, because no individual decision's own record was ever the place that fact would live.

This is not a hypothetical edge case invented to make a point. It is the direct, necessary consequence of a fact about what a decision record can and cannot contain: a decision's own record describes what that decision did. It does not, by construction, describe how that decision relates to every other decision around it. Those are different kinds of information, and having all of the first kind does not give you any of the second kind for free.

## Local Reconstruction Is Not Trajectory Reconstruction

It's worth being precise about the two questions being conflated when "can we reconstruct what happened" gets asked of a multi-step AI system.

**Decision reconstruction** asks, for one decision D: which context did D consume — which model version, which policy, which evidence, which authority?

**Trajectory reconstruction** asks, for a set of decisions: which decisions depended on which others? What state or output propagated from one to the next? What is the dependency graph — not a timestamp-sorted list, but the actual causal structure — that is uniquely consistent with the retained record?

That second question is not answered by sorting decisions by when they happened. Timestamps tell you an ordering; they do not tell you a dependency. Two decisions can be strictly ordered and completely unrelated, or loosely ordered and tightly coupled. Trajectory reconstruction is about recovering *which relation actually held*, not about recovering *what order things happened in* — and it is entirely possible for the second to be fully known while the first remains genuinely open.

This distinction matters because it is easy to assume the two questions have the same answer — that once you've solved decision-level auditability, trajectory-level auditability comes along for free as a matter of aggregation. It doesn't, and the rest of this article is a controlled demonstration of exactly where and how that assumption breaks.

## What Has to Compose

A previous piece in this line of work established that a single AI-mediated decision's consumed context is not automatically reconstructable from a retained version history — keeping every version of a policy, a model, or an authority assignment does not by itself let you determine which version a specific past decision actually used, unless the record also retains the *relation* connecting the decision to the specific version it consumed. Retention and consumption are different facts, and only one of them is usually kept.

That result was scoped to a single decision. The natural next question is whether it composes: if every decision in a trajectory individually has this guarantee — if decision-context reconstructability holds pointwise, at every step — does trajectory reconstructability follow automatically? Formally: for decisions D = {d1, ..., dn}, each with its own locally consumed context C(di), local reconstructability means C(di) is uniquely recoverable for every i. A trajectory additionally has a dependency relation E ⊆ D × D connecting decisions to one another. Trajectory reconstructability requires both C(di) *and* E to be uniquely recoverable. The question is whether

> ∀i, identifiable(C(di))

implies

> identifiable(E).

Stated that way, the two are visibly different claims — one is a per-element property, the other is a property of a relation defined *across* elements, and nothing about the first automatically supplies the second. But visibly different is not the same as *actually* different in practice; it's possible that in ordinary systems E just falls out of the C(di)'s once you have all of them. That's an empirical question, and it's the one this piece tests directly.

## The Experiment

The test uses two regimes built on identical local data, differing only in whether a trajectory relation is present.

**Regime T1 — locally complete, globally unlinked.** Every decision's record is fully populated: its own consumed context, its own output, its own local facts, all present and correct. No field on the record type stores any relation to another decision at all — not absent-but-empty, but structurally not there.

**Regime T2 — locally complete, plus one relation.** The exact same local records as T1, with exactly one addition: a field naming which prior decision this one's input actually came from.

The comparison only means something if T1 and T2 are genuinely identical everywhere except that one relation — otherwise a difference in outcomes could just be a difference in local data quality, and the whole exercise would prove nothing about composition specifically. So this was enforced mechanically, not just asserted: every local field on every decision record was checked field-for-field equal between T1 and T2, for every case, and that check re-runs automatically before every execution of the experiment. If it fails, the run halts. It never failed.

Six cases were constructed. One is a fully identifiable control, where exactly one earlier decision could plausibly be D3's predecessor. Four exercise two distinct ambiguity mechanisms: two earlier decisions producing an identical output value that a later decision consumes (an inventory count, a boolean precondition, a shared state write — genuinely different scenarios, same underlying mechanism: value collision); and two earlier decisions occurring close enough in time that, at the precision the system actually observes events, their order is indistinguishable, even though a later decision's dependency is defined as "whichever happened last." The sixth case is a negative control, structurally identical to the value-collision case, with one ordinary dependency-trace field added to T1's record — deliberately built to show that an ordinary, unremarkable engineering mechanism resolves the ambiguity, so the result of this experiment cannot be mistaken for evidence that something exotic is required.

An investigator was built for each regime. Neither is a strawman. T1's investigator actively infers a dependency wherever the local evidence uniquely determines one — an exact value match with no competing candidate, a strictly latest timestamp with no tie — and returns AMBIGUOUS, never a guess, exactly when two or more candidates are equally consistent with what's retained. T2's investigator reads the relation directly. This distinction — infer-when-determined vs. read-directly — is the entire point of the comparison.

## Perfect Local Records, Ambiguous Global History

Local Decision Reconstruction — whether each decision's own context and result were correctly recoverable — was **1.00 in both regimes, across all six cases.** This is the experiment's own precondition, checked directly rather than assumed: whatever happens next cannot be explained by T1 having worse local data, because it doesn't.

Trajectory Identifiability — whether the full dependency structure of a case was correctly and uniquely recovered — was **1.00 under T2** and **0.33 (two of six cases) under T1.** The two T1 successes were the control case, where only one candidate predecessor existed, and the negative control, where the added trace field settled it directly. The four failures were exactly the four cases built around the two ambiguity mechanisms — value collision and near-concurrent ordering.

That is the composition failure, stated plainly: local completeness held at 1.00 the entire time; global identifiability dropped to 0.33 the moment cross-decision dependencies stopped being uniquely determined by local facts alone. Nothing about having every decision individually reconstructable prevented the trajectory from becoming ambiguous. The two properties simply are not the same property, and this is what it looks like when they come apart.

## Ambiguous Is Better Than Wrong

The more important number is not the 0.33. It's what didn't happen alongside it.

Dependency Edge Accuracy — the fraction of the times T1's investigator was willing to name a specific predecessor that it named the *correct* one — was **1.00.** False Global Confidence — the fraction of dependent edges where the investigator confidently named the *wrong* predecessor — was **0.00.** Every one of the four cases T1 failed to identify, it failed honestly: it returned AMBIGUOUS, listed the genuinely tied candidates, and stopped, rather than picking one and reporting it as settled.

This distinction is worth dwelling on because the two failure modes have completely different consequences for anyone relying on the record later. An investigator that says "I cannot tell you which of these two decisions D4 actually depended on, but here are the two candidates" leaves a human free to go find more evidence, or to flag the gap, or to simply not trust a downstream conclusion built on that link. An investigator that confidently names the wrong one hands a human a false trajectory that looks exactly like a true one. This experiment found none of the second kind. That is a genuinely favorable result, and it's worth being honest that it need not have come out this way — a differently constructed investigator, or a differently constructed ambiguity mechanism, could produce false confidence instead of honest ambiguity. This one didn't, in these six cases, and the reason is architectural: the investigator was built, by design, never to break a tie.

## The Relation That Resolves the Ambiguity

The negative control is the case that keeps this result from being overclaimed, and it deserves to sit at the center of the argument rather than at the edge of it.

C3-6 is built identically to the value-collision case that fails under T1 — same structure, same colliding output values, same setup — with exactly one difference: T1's record for the dependent decision carries one additional field naming its true predecessor, the kind of field an ordinary tracing or event-sourcing system attaches as a matter of course. Under that single addition, the ambiguity disappears completely; the case resolves correctly, T2-style, without needing to become T2.

That single fact rules out a stronger, more dramatic claim this experiment might otherwise be read as supporting: that trajectory-level reconstruction *needs* some new mechanism — a new kind of trajectory-binding layer, a new architectural component purpose-built for this problem. It doesn't. What the negative control shows is narrower and more mundane: **preserving an ordinary cross-decision dependency relation is sufficient to close the gap this experiment demonstrates.** No new kind of record is required. The kind of record already required is simply, in the four failing cases, absent.

## This Is Not a New Provenance System

The most direct objection to this whole piece is: *isn't this just workflow provenance?*

The honest answer is yes, largely. Workflow-provenance formalisms have modeled exactly this distinction — an entity's own attributes versus the derivation edges connecting it to other entities — since well before this line of work existed, and the W3C's own provenance data model represents precisely the relation this experiment's T2 regime adds: a record stating that one activity `used` a specific prior entity, distinguishable from that activity's own descriptive attributes [1]. If a system's workflow-provenance instrumentation already captures the "used" edges between every pair of dependent decisions, the mechanism this experiment demonstrates as missing is, in that system, already present, and nothing here is news to it.

Distributed tracing systems solve the same problem in practice for a different reason: a trace's parent-span reference exists specifically to let a system reconstruct causal execution order across components, and mature tracing infrastructure has treated this as a first-class concern for over a decade [2]. Event-sourcing architectures can capture the same relation if the event log is instrumented to record which prior event a later one consumed, rather than only what the later event itself did [3]. None of these are new tools, and none of them were invented for AI systems.

So this piece is not a new provenance mechanism, and does not claim to be one. What it contributes instead is narrower: a controlled demonstration, for AI-mediated decision trajectories specifically, that the gap workflow provenance and tracing already know how to close is a gap that actually opens — that decision-level completeness genuinely does not entail trajectory-level completeness, rather than the two being trivially the same property under a different name. The formal literature on diagnosability — determining, from a system's observed output sequence, whether a specific event occurred, without necessarily observing the event directly [4] — supplies the right vocabulary for what Regime T1's honest AMBIGUOUS verdict actually is: a formal statement that the observed record does not diagnose which of two candidate histories occurred, not a failure of instrumentation effort. And the broader caution that local, component-level correctness does not automatically compose into global, system-level guarantees is not new either — it is one of compositional verification's standing results for systems built from independently-verified parts, established well outside any AI context [5]. This piece's contribution is to show that caution applies, concretely and measurably, to reconstructability specifically, in a domain — multi-step AI-mediated decision-making — where the parts being composed are model calls, tool invocations, and policy evaluations rather than the software components that literature was originally written about.

If that feels like a modest claim, it is meant to. The alternative — presenting six deliberately constructed cases as evidence of a widespread production problem, or as justification for a new architectural layer — would be a larger claim than the evidence supports, and this piece is deliberately not making it.

## What to Preserve Across Decisions

The practical question this leaves for anyone building a multi-step AI-mediated workflow is simple to ask and worth asking directly:

*Can I reconstruct every decision locally? Can I also reconstruct which prior decision, output, or state each later decision actually consumed?*

A "yes" to the first and "no" to the second is not a hypothetical failure mode — it's the exact structure of Regime T1 in four of this experiment's six cases, and it describes a system that is locally auditable and globally ambiguous: every individual step defensible on its own, the sequence connecting them not defensible at all. Closing that gap does not require inventing anything. It requires making sure at least one of the following is actually retained, for every dependent decision, and not just for some of them: a parent-decision identifier, a consumed-event identifier, a trace or span linkage back to the producing step, an explicit provenance edge, a state-transition producer identifier, or a workflow-level dependency reference. Which one fits depends entirely on the system's own architecture — there is no single schema this piece is prescribing, and no reason to expect one design to fit every case. The requirement is narrower than a schema: whichever mechanism a system already uses for this, it has to actually be populated for the decisions where trajectory reconstruction will matter, not merely available as a feature nobody turned on.

## What the Experiment Does Not Show

This is a controlled, synthetic testbed of six handcrafted cases, run through a deterministic investigator built specifically for this test. It establishes existence — that there exist systems in which decision-level reconstructability does not imply trajectory-level reconstructability — and nothing about prevalence: no claim is made, or supportable, about how often this gap occurs in production AI systems, because six designed cases are not a statistical sample and no inference about a broader population is appropriate from them.

Only two ambiguity mechanisms were tested — value collision and near-concurrent ordering. Other plausible mechanisms (partial or lossy state propagation, many-to-one dependency fan-in, adversarial timestamp manipulation) were not constructed, and this piece makes no claim about how they would behave, including no claim that they would also produce honest ambiguity rather than false confidence. The dependency-graph definition used here — value matching and recency — is one reasonable operationalization of "what does it mean for one decision to depend on another," not the only one a different system might reasonably use. Where a system's workflow-provenance or tracing instrumentation already captures the relevant relation fully, this gap does not apply to it; the finding is that the gap is real and reproducible where that instrumentation is absent, not that it is universal. And no claim is made anywhere in this piece about human understanding, comprehension, or organizational knowledge — "reconstructability" here is the same narrow, technical, previously-defined property as before, applied one level up, from a single decision to a trajectory of them.

## The Composition Question

Decision-level reconstructability and trajectory-level reconstructability are different properties, and having the first does not give you the second for free. That is the entire finding, stated without embellishment: a sequence of individually reconstructable decisions is not necessarily reconstructable as a trajectory, because local decision records can preserve every decision's own consumed context in full while leaving the relations connecting decisions to each other completely undetermined — and trajectory reconstruction needs both.

Nothing here says this gap is common, says it requires new tooling to close, or says AI systems are special in having it — the same composition question applies to any system built from dependent, individually-auditable steps, and every mechanism that closes it already exists. What this piece adds is narrower and, hopefully, more useful than a broader claim would have been: the gap is real, it is demonstrable under controlled conditions, it produces honest ambiguity rather than false confidence when the investigator is built not to guess, and it closes completely the moment an ordinary dependency relation is retained. For a system where trajectory reconstruction will eventually matter — an incident review, an audit, a "why did the agent do that" months later — that is the concrete question worth asking now, while the answer can still be engineered rather than reconstructed after the fact: not just *is every decision reconstructable*, but *is the relation between them retained anywhere at all*.

---

## References

[1] W3C, "PROV-DM: The PROV Data Model," W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-dm/

[2] OpenTelemetry, "Traces," OpenTelemetry Documentation. https://opentelemetry.io/docs/concepts/signals/traces/

[3] Fowler, M., "Event Sourcing," 2005. https://martinfowler.com/eaaDev/EventSourcing.html

[4] Sampath, M., Sengupta, R., Lafortune, S., Sinnamohideen, K., Teneketzis, D., "Diagnosability of Discrete-Event Systems," IEEE Transactions on Automatic Control, 40(9):1555–1575, September 1995.

[5] Bakirtzis, G., Topcu, U., "AlgebraicSystems: Compositional Verification for Autonomous System Design," arXiv:2203.16343, 2022.

---

*Word count: 3,257 (full file, including headings, code blocks, and references — see `draft-v1-audit.md` for the self-audit).*
