# Why Keeping Every Version Still Isn't Enough to Explain an AI Decision

### Retained is not consumed: a measured causal gap in AI decision reconstruction

---

At t0, a production system authorizes a consequential action. Call it D. Reaching D depended on a specific model version, a specific policy, specific evidence, a specific authority to approve it, and specific configuration. Nothing about this is exotic — it's an ordinary automated approval, or an agent's tool call, or a deployment gate passing.

Months later, at t1, someone asks why D was authorized.

Every artifact involved still exists. The model registry has every version. The policy store has every revision. The evidence that was consulted is sitting in a retrieval index somewhere. Nothing was deleted. By any reasonable definition, this is a well-versioned system.

And there may still be no way to answer the question.

Not because the data is gone. Because nothing recorded which version of each of those things D actually used — and the versions that exist today are not necessarily the ones that applied then. This article works through two controlled experiments that test exactly this gap, a negative control that changes what the result actually means, and the engineering property the whole thing points to.

## Version History Is Not Decision History

The obvious objection arrives immediately, and it deserves a straight answer rather than a strawman: *we have versioning. We have audit logs. We have event sourcing. We have bitemporal data. We have provenance graphs. We have traces.* Isn't the reconstruction question already closed?

Sometimes, yes. Each of those mechanisms is real, mature, and — done correctly — capable of closing part or all of this gap. Bitemporal databases have solved "what was true at a given point in time" as a query problem since the 1980s. Event sourcing, done right, replays state exactly. Provenance graphs represent lineage relations precisely. None of this article argues that these mechanisms don't work.

The argument is narrower, and it survives the objection rather than contradicting it: **retaining history and being able to identify what a specific decision consumed from that history are different properties.** A system can have both. It can also have the first without the second — and having the first is not evidence that it has the second, no matter how complete the history is.

That distinction sounds abstract until it's made concrete, which is what the rest of this article does.

## What a Historical Decision Actually Depends On

An artifact history can answer a family of questions: which policy versions existed, and for what intervals; which model versions existed; which authority assignments existed; which evidence was retrievable at a given time. Call the set of versions D actually used — the model, policy, evidence, authority, and configuration it consumed — its **consumed context**.

Reconstruction asks a different question than "does a version of X exist in history": it asks whether the *relation* connecting D to the specific member of that history it used is itself recoverable. Call that property **decision-context identifiability**: for each element x of D's consumed context, is there a preserved relation R such that R(D, x) picks out exactly one x, correctly, from later-available records?

Written compactly:

```
x retained in history        -- does NOT imply -->   R(D, x) recoverable
```

An artifact existing somewhere in a version history is not the same fact as a relation existing that connects a specific decision to a specific version of it. The rest of this article is two experiments testing whether that gap is real or merely a definitional nicety.

## Experiment 1: When History Changes After the Decision

The first experiment compared three preservation regimes for a synthetic access-decision system (a risk score, a policy threshold, an approver role, a watchlist check — deliberately simple, so the mechanism under test isn't obscured by domain complexity):

- **Regime A (bare):** only the decision outcome is kept. No history.
- **Regime B (versioned, unbound):** complete, genuinely bitemporal version histories for policy and authority, a full event trace of every value read, model and context history — everything a well-instrumented, competently engineered system would retain. Deliberately built strong, not strawmanned.
- **Regime C (versioned, bound):** everything in B, plus one additional artifact per decision — an explicit record, authored at decision time, of exactly which policy version, authority assignment, model version, and evidence snapshot were consulted.

A deterministic investigator — not a human, not an LLM, to keep the test about information availability rather than reasoning skill — reconstructed each decision from whatever artifacts its assigned regime provided, across ten cases: a no-drift control, five cases of ordinary forward-moving drift (a policy revised, an approver reassigned, evidence corrected upstream), and — the case this section is about — retroactive drift.

In the retroactive-drift case, the decision-maker at t0 relied on policy v1 (threshold 0.50). Later, a correction is recorded: v1 was itself wrong, and the *actually* correct threshold (0.45) was backdated to have applied since before t0. This is not a contrived scenario — backdated corrections happen routinely in policy administration, for defensible reasons.

Regime B's temporal-correctness score on this case dropped to 0.00, versus 1.00 for Regime C. On the two forward-drift cases where policy and authority genuinely changed (non-retroactively), B and C were identical — both at 1.00 — which matters as much as the failure: B is not weak in general, it fails specifically here. Across two combined-drift cases mixing retroactive correction with several simultaneous forward changes, the pattern held: B's temporal correctness stayed at 0.00 while C stayed at 1.00.

The reason is structural, not a data-completeness problem. Regime B's reconstruction procedure asks: *as of t0, according to what the record currently says, which policy applied?* Before the backdated correction is recorded, that query returns v1. After it, the identical query — same logic, same code — returns v1bis, because the record itself changed. **A query against retained history answers what the record now says was valid at t0. That is a different question from what the decision actually relied on at t0**, and the two diverge exactly when a correction is recorded after the fact. No amount of additional bitemporal completeness fixes this, because the problem isn't missing data — it's that the record's own account of the past has been legitimately revised.

## The More Dangerous Failure: A Wrong Answer That Looks Right

The retroactive-drift case could have failed in two different ways. Regime B could have had no answer at all — an honest "I don't know." Instead, it produced a specific, concrete, wrong answer, with no internal signal that anything was amiss.

This is False Historical Confidence, and it's the sharper of the experiment's two primary metrics for exactly this reason. On the retroactive-drift case, B's false-confidence rate was 0.50; on one of the combined-drift cases, 1.00. Regime C's rate was 0.00 on every case in the experiment, without exception.

The distinction matters for how this result should be read. A system that says "I can't determine which policy applied" is not the failure mode this article is about — it's arguably the correct behavior under genuine uncertainty. The failure mode that matters is a reconstruction that is internally coherent, supported by retained records, superficially complete, and simply wrong about what actually happened. That's a harder failure to catch, because nothing about the output looks incomplete. This is a result from one synthetic testbed, not a claim about how often this happens anywhere else — but within that testbed, it is not a hypothetical: it's what a strong, correctly implemented Regime B actually produced.

## Experiment 2: When Time Does Not Identify a Unique Context

The first experiment included a tenth case meant to test a second, distinct failure mode: two decisions straddling a policy boundary, to see whether timestamp-based attribution could go wrong. It didn't induce genuine ambiguity — each decision was recorded a full 60 seconds from the boundary, on its own side, which a plain interval query resolves without difficulty. That gap was reported as a disclosed limitation, not quietly dropped, and a follow-up was run specifically to close it.

The follow-up isolates a different mechanism: **observational timestamp-precision loss**, not retroactive correction. A decision's true moment is known only to ground truth, at full precision. The *observable*, persisted decision timestamp is truncated to the nearest second — an ordinary, common logging practice. When a policy, authority, or model version boundary falls inside that one-second window, no amount of correct querying can determine which side of the boundary the decision's true moment actually fell on, because the information that would resolve it was never observable in the first place.

Across the follow-up's four ambiguous cases (isolated ambiguity in policy, authority, and model version identification, plus one combined case), Regime B did not produce a wrong answer. It correctly reported the dependency as ambiguous — naming the genuine candidates — every single time a boundary actually fell inside the observable window, and never when it didn't. Regime C, whose binding was authored using the decision's true, unrounded moment, resolved every one of the same cases correctly and uniquely.

This is a structurally different failure than the first experiment's. There, B was confidently wrong. Here, B is honestly stuck. Both are failures of unique reconstruction — but only one of them is dangerous in the way the previous section described, and the experiment's design was built specifically to be able to tell them apart rather than collapse them into one undifferentiated "failed" bucket.

## The Negative Control That Changed the Thesis

The follow-up included one more case, and it's the one that should not be skipped over: identical in structure to the isolated policy-ambiguity case, except that Regime B was additionally given one ordinary field — a record of which policy version the request handler actually read, logged as an unremarkable trace attribute, never framed, named, or structured as a "decision binding."

With that one field present, Regime B matched Regime C exactly. Same unique, correct answer. Same score on every metric.

This result directly narrows the thesis this article would otherwise be tempted to argue. The original, stronger claim — that explicit, decision-time binding is what's required — does not survive this case. An ordinary causal-consumption record, with no special schema and no distinctive name, closed exactly the same gap. What the two experiments together actually support is not that one particular artifact is necessary. It's that *some* preserved relation connecting the decision to its consumed context is necessary — and an explicit binding record is one way to guarantee that relation exists, not the only way.

This makes the finding smaller than it might have first appeared, and more defensible for being smaller. The experiment does not establish a new, proprietary reconstruction mechanism. It identifies and measures a property — and then shows, by trying to defeat its own preferred implementation, that the property is what matters, not the implementation.

## This Is Not a New Provenance System

Returning to the mechanisms dismissed too quickly at the start: each of them can supply the required relation. Whether they do, in practice, is a separate, checkable question.

**W3C PROV** models exactly the right kind of relation — an Activity's Usage of an Entity is structurally a causal-consumption record. What PROV's specification does not natively provide is a valid-time interval on that Entity ("this policy was in force from t_a to t_b"), so a PROV graph populated with raw values rather than version identifiers doesn't close the first experiment's failure mode, even though it would close the second's.

**Event sourcing**, correctly instrumented, is exactly the negative control's mechanism — this is precisely what the negative control captured. The catch is the qualifier: event-sourcing implementations typically capture the *values* a decision read ("threshold consulted: 0.62"), not the *version identifiers* that produced them. A system logging values only reproduces the first experiment's Regime B; a system logging identifiers reproduces its Regime C, by a different name.

**Bitemporal databases** are the closest theoretical match for the policy and authority side of this problem, and they solve it completely — for exactly the cases without retroactive correction. The first experiment's central result is precisely the boundary of that "completely."

**Distributed tracing**, **audit logs**, and **model/data lineage** tools each capture a real, useful slice of history — execution paths, compliance-mandated fields, training-time provenance — but none of them, as typically deployed, are schema'd to distinguish "this attribute identifies the applicable policy version" from incidental debug context, and none extend by default from training-time lineage to runtime decision consumption.

No mechanism in this list needs to be reinvented. What's missing by default is not a new artifact type — it's the discipline of capturing identifiers rather than values, applied to the specific things a decision actually depends on.

## The Property to Design For

For any AI-mediated decision D whose history might need to be reconstructed later, the design question is not "is everything D might have used versioned somewhere?" Both experiments show that question can be answered "yes" and still leave reconstruction impossible. The design question is:

> For D's model version, policy, evidence, authority state, and relevant configuration — does a preserved relation exist that identifies, specifically and correctly, which version D consumed? Not which version currently exists. Not which version the record now says was valid then. Which one D actually used.

If the honest answer for any of those five is "we'd have to infer it from timestamps" or "we'd query current state and assume it matches," that's exactly the gap both experiments measured.

## Two Ways to Preserve It

Neither experiment prescribes a single schema. Two structurally different implementations both closed the gap in these tests:

**An explicit decision-context record**, authored at decision time and never subsequently altered — a small artifact naming the specific model, policy, evidence, authority, and configuration versions consulted:

```
D ->
  model_version:    m17
  policy_version:    p7  (valid 2026-01-04 .. 2026-03-11)
  evidence_ids:      [e441, e502]
  authority_version: a3  (agent X, valid from 2025-11-01)
  config_version:    c5
```

**A causal-consumption event**, logged as part of ordinary request handling — no dedicated schema, just a trace field or event attribute recording *which version was read*, not merely *what value it returned*:

```
event: policy_consulted
  policy_version_id: p7
  read_at: <request time>
```

Both satisfy the same property. Neither is presented here as the correct one — the negative control's entire point is that the property, not the implementation, is what the evidence supports.

## What the Experiments Do — and Do Not — Show

Both experiments used small, synthetic, purpose-built testbeds, deliberately, to isolate one mechanism at a time. That has a cost worth stating plainly:

- **No prevalence claim.** Nothing here measures how often real production systems exhibit either failure mode, or how costly it is when they do.
- **No universal-mechanism claim.** Regime B, in both experiments, was built stronger than the prior-art review found typical AI/ML tooling to be by default — the tests were designed to be fair to the strongest existing practice, not to a weak baseline.
- **Explicit binding is not shown to be required.** The negative control is the article's own strongest evidence against that stronger claim.
- **Only two mechanisms were tested.** Clock skew across independent components, general multi-timeline ordering ambiguity, and unreliable or contested causal signals were out of scope for this pass.
- **External validity to real systems remains an open question**, not something either experiment resolves.

What the experiments do show, within that scope: complete version history, competently implemented, is not sufficient for two independently demonstrated reasons, and closing the gap requires a preserved relation between a decision and what it consumed — which more than one existing mechanism can supply, if deliberately configured to.

## The Question to Ask

The question worth asking of a system that needs to survive an audit, a postmortem, or a "why did this happen" months later is not *did we keep every version*. Both experiments show a system can answer yes to that and still fail. The question is *did we preserve enough of a causal trail to know which versions this decision actually used* — and if the honest answer is "we'd have to guess," that gap is worth closing before it's needed, not after.

Historical reconstructability is only one dimension of what it means to preserve understanding of a system over time.

---

*Word count: 2,723 (full file, including headings and code blocks — see `editorial-notes.md` for sourcing notes).*
