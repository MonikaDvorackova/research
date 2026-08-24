# Retained Is Not Consumed: Why Version History Doesn't Guarantee Decision Reconstruction

### What two controlled experiments — and a hard look at what the first one actually proved — show about reconstructing why an automated decision was authorized

---

At t0, a system authorizes a consequential action. Call it D. Reaching D depended on a specific model version, a specific policy, specific evidence, a specific authority to approve it, and specific configuration. Months later, someone asks why D was authorized.

Every artifact involved still exists. The model registry has every version. The policy store has every revision. Nothing was deleted. By any reasonable definition, this is a well-versioned system.

And there may still be no way to answer the question — not because the data is gone, but because nothing recorded which version of each of those things D actually used, and the versions that exist today are not necessarily the ones that applied then.

This is a general systems and provenance problem, not something unique to AI. It shows up anywhere a decision depends on several independently versioned things. AI-mediated decisions are a useful place to look at it because they routinely stack several of these dependencies at once — a model version, a prompt or configuration, retrieved evidence, a policy, an authority, sometimes live tool or retrieval state — in a single decision path, more often than most other automated-decision categories do. Nothing below claims AI creates this problem. It claims AI decisions are a dense, realistic setting to measure it in.

## Retained Is Not Consumed

An artifact history can answer a family of questions: which policy versions existed, and for what intervals; which model versions existed; which evidence was retrievable at a given time. Call the set of versions D actually used — the model, policy, evidence, authority, and configuration it consumed — its **consumed context**.

Reconstruction asks something different from "does a version of X exist in history": whether the relation connecting D to the specific member of that history it used is itself recoverable. Call this **consumption relation**: a record, of any shape, that lets a later investigator determine — not guess, not infer from timing — which version D actually used. (This is not statistical causal inference; it is closer to a reference or pointer than to a claim about cause and effect, and the rest of this article uses "consumption relation" rather than "causal relation" for exactly this reason.)

An artifact existing somewhere in a version history is not the same fact as a consumption relation connecting a specific decision to a specific version of it. Two controlled experiments test whether that gap is real.

## What Existing Systems Already Preserve

The obvious objection: *we have versioning, audit logs, event sourcing, bitemporal data, provenance graphs, traces.* Isn't this already solved?

Sometimes. Each of these mechanisms is real and, used correctly, capable of closing part or all of the gap — that is not in dispute here. What's tested below is narrower: whether retaining history and being able to identify what a specific decision consumed from that history are the same property. They are not, automatically, just because a system has both kinds of machinery running.

## Experiment: When Timestamps Don't Identify a Unique Context

The cleaner of the two experiments isolates **observational timestamp-precision loss**. A decision's true moment is known only to ground truth, at full precision; the *observed*, persisted decision timestamp is truncated to the nearest second — an ordinary logging practice. When a policy, authority, or model version boundary falls inside that one-second window, no query can determine which side of the boundary the decision's true moment fell on, because the information that would resolve it was never observed in the first place.

Across four such cases — ambiguity isolated to policy, to authority, to model version, and one case with two ambiguous dimensions at once — a versioned-but-unbound investigator did not produce a wrong answer. It correctly reported the affected dependency as **AMBIGUOUS**, naming the genuine candidates, every time a boundary actually fell inside the observable window, and never elsewhere: an Ambiguity Detection Rate of 1.00 on every genuinely ambiguous dimension, with a False Historical Confidence rate of 0.00 throughout the entire experiment, for both investigators, on every case. A bound investigator, whose record was authored using the decision's true, unrounded moment, resolved every one of the same cases correctly and uniquely.

This distinction matters more than it might look: **AMBIGUOUS is not the failure mode to worry about.** A procedure that says "I cannot uniquely determine which version applied" is behaving correctly under genuine uncertainty — an honest non-answer, not a wrong one. The property actually being tested is narrower and sharper than "does reconstruction succeed": can the retained record uniquely identify the consumed context, or does it only narrow the possibilities? Complete retained history, in these four cases, narrows but does not uniquely identify.

## The Negative Control That Reframes the Thesis

One more case in this experiment is the one to not skip past: identical in structure to the isolated policy-ambiguity case, except the versioned-but-unbound investigator was additionally given one ordinary field — a record of which policy version the request handler actually read, logged as an unremarkable trace attribute, never framed or structured as a formal binding.

With that one field present, the unbound investigator matched the bound one exactly — same unique, correct answer, same score on every metric.

This result is what the rest of the article has to be read through. The stronger, more architecturally specific claim — that an explicit, decision-time-authored binding record is what's required — does not survive this case. An ordinary consumption-relation record, with no special schema and no distinctive name, closed exactly the same gap. What the evidence actually supports is not that one particular artifact type is necessary. It's that *some* preserved consumption relation is necessary, and a formal binding record is one way to guarantee it exists — not the only way. A provenance edge, an event log entry, or any other explicit "D used version X" record satisfies the same property.

## Experiment: When History Changes After the Decision

The second experiment tests **retroactive correction**: whether a later, legitimate correction to a retained history can make a correctly-executed query about the past return an answer other than the one a decision actually relied on.

A decision at t0 relied on policy v1 (threshold 0.50). Later, a correction is recorded: v1 was itself wrong, and the corrected threshold (0.45) is backdated to have applied since before t0 — the kind of correction that happens routinely and legitimately in policy administration. Across three cases built around this mechanism, the initial finding looked uniform: the versioned-but-unbound investigator's Temporal Correctness fell to 0.00 in each, while the bound investigator stayed at 1.00.

Closer inspection — done deliberately, as a check on the experiment's own claim, not as damage control — found that this uniformity did not hold up. The clean, unqualified case is the one involving a **retroactive authority correction**: an approver's assignment is retroactively revised, and nothing in the retained record identifies who actually approved the decision beyond a bare "an approver existed" flag. No amount of clever querying against the retained data recovers the correct approver's identity, because that identity was never captured anywhere except as a boolean. This case stands as clean, direct evidence: retained history, even complete and correctly queried, does not by itself preserve who was consulted.

The two cases involving only a **retroactively corrected policy value**, by contrast, turned out to be weaker than they first appeared. The retained event trace in those cases held the *raw threshold value* actually read at decision time (0.50) — unaffected by the later correction, because it was captured before the correction was ever recorded. That value uniquely matches the historically correct policy version among the retained candidates. An investigator that cross-referenced this already-retained value against every candidate policy record, rather than relying on interval matching alone, would have recovered the correct answer without any binding. The tested procedure did not perform that cross-reference. So these two cases demonstrate a limitation of the specific reconstruction procedure that was run, not a clean information gap in what was retained — a materially different, and weaker, claim than the original result suggested.

This also corrects an overstatement worth naming directly: it is not true that no bitemporal implementation could have avoided this failure. Authoritative system-versioned database implementations are explicitly designed to preserve a superseded record's original system time rather than overwrite it when a correction is recorded [2][3] — the test system's retained history did not fully implement that discipline for the corrected records. That is a property of the specific test system, not a limitation of bitemporal databases as a category.

## False Historical Confidence, Precisely Scoped

The authority case is where **False Historical Confidence** — a reconstruction that is concrete, internally coherent, and simply wrong, with no signal that anything is amiss — is genuine, unqualified evidence: the versioned-but-unbound investigator did not merely fail to resolve the correction, it named a specific, wrong approver with full confidence. The bound investigator's false-confidence rate was zero across every case in both experiments, without exception.

The two policy-only cases are false-confidence findings of a different, narrower kind: they show that an *incomplete reconstruction procedure* can produce a confidently wrong answer even when the retained record contains enough information, elsewhere, to avoid it. That is a real and useful distinction — **information insufficiency** and **reconstruction-procedure insufficiency** are not the same failure, and conflating them would overstate what those two cases show.

## Prior Art, Revisited Honestly

Returning to the mechanisms named earlier: each can supply a consumption relation. Whether a given deployment actually does is a separate, checkable question, not something the mechanism guarantees by existing.

**W3C PROV**'s Usage relation between an Activity and an Entity is structurally exactly a consumption record — "D used version X" [1]. What PROV does not natively provide is a valid-time interval on the Entity it references, so a PROV graph populated with raw values rather than version identifiers closes the observational-ambiguity mechanism but not the retroactive-correction one.

**Event sourcing** [5], correctly instrumented, is exactly the negative control's mechanism. The qualifier is what typical instrumentation captures: values read ("threshold consulted: 0.62"), not the version identifiers that produced them. A system logging values only reproduces the versioned-but-unbound condition tested here; a system logging identifiers reproduces the bound one, under a different name.

**Distributed tracing**, via OpenTelemetry, captures causal execution relationships between spans [4], but span attributes are undifferentiated key-value pairs with no schema distinction between "this identifies the applicable policy version" and incidental debug context — the relation can be there without being identifiable as the relation that matters.

**Temporal and bitemporal databases**, correctly implemented per the system-versioning model standardized in SQL:2011 [2][3], solve the retroactive-correction mechanism directly — a genuinely system-versioned table preserves a superseded record's original system time rather than overwriting it, which is precisely the property the test system in this article did not fully implement for its corrected records (see above). None of this makes the mechanism solved by default: it requires the storage layer to actually be built this way, which the dependencies most relevant to AI-mediated decisions — prompt stores, retrieval corpora, policy-as-config services — typically are not.

No mechanism in this list needs to be reinvented. What's inconsistently present by default is the discipline of capturing identifiers, not values, wherever a version-time distinction later matters.

## The Property to Design For

The design question is not "is everything D might have used versioned somewhere?" Both experiments show that can be true and reconstruction can still fail or remain ambiguous. The question is:

> For D's model version, policy, evidence, authority state, and relevant configuration — does a preserved relation exist that identifies, specifically, which version D consumed? Not which version currently exists. Not which version the record now says was valid then. Which one D actually used.

If the honest answer for any of those is "we'd have to infer it from timestamps" or "we'd query current state and assume it matches," that is the gap both experiments measured.

## Two Ways to Preserve It

Neither experiment prescribes one schema. Two structurally different approaches both closed the gap in these tests, and the property is what matters, not the representation:

**A direct decision record**, authored at decision time:

```
D ->
  model_version:    m17
  policy_version:    p7  (valid 2026-01-04 .. 2026-03-11)
  evidence_ids:      [e441, e502]
  authority_version: a3  (agent X, valid from 2025-11-01)
```

**A provenance/event relation**, logged as part of ordinary request handling:

```
D used policy_version p7
D wasAssociatedWith agent X
```

## Limitations

Both experiments used small, synthetic, purpose-built testbeds, deliberately, to isolate one mechanism at a time — with real, disclosable costs:

- Controlled, deterministic cases, not a statistical sample — there is no p-value here and none is implied; "case-regime executions," not "trials."
- No prevalence measurement and no claim of statistical representativeness for real production systems.
- The retroactive-correction test system implemented strong version and temporal history, but not a complete SQL-style system-versioned temporal table — a specific, disclosed implementation gap, not a general critique of bitemporal storage.
- Two of the three retroactive-correction cases are algorithm-limitation findings, not clean evidence of an information gap; the authority case is the one to cite as clean evidence.
- The timestamp-precision experiment tests one precision model (second-level truncation) and one boundary offset — not clock skew, not multi-timeline ordering ambiguity.
- The negative control's consumption-relation field was correct by construction; this article does not test what happens when such a signal is itself unreliable or contested.
- External validity to production systems remains open — this establishes the mechanisms are real and measurable in a controlled setting, nothing about their frequency or cost elsewhere.

## The Question to Ask

The question worth asking of a system that needs to survive an audit, a postmortem, or a "why did this happen" months later is not *did we keep every version*. The question is *does the retained record identify which versions this decision actually used, or only narrow the possibilities* — and if the honest answer is "we'd have to guess" or "we can only narrow it down," that gap is worth closing before it's needed, not after.

Historical reconstructability is only one dimension of what it means to preserve understanding of a system over time.

---

## References

[1] W3C, "PROV-DM: The PROV Data Model," W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-dm/

[2] Microsoft, "Query Data in a System-Versioned Temporal Table," SQL Server documentation (implementing the SQL:2011 system-versioning model). https://learn.microsoft.com/en-us/sql/relational-databases/tables/querying-data-in-a-system-versioned-temporal-table

[3] MariaDB, "System-Versioned Tables," MariaDB Server documentation. https://mariadb.com/docs/server/reference/sql-structure/temporal-tables/system-versioned-tables

[4] OpenTelemetry, "Traces," OpenTelemetry Documentation. https://opentelemetry.io/docs/concepts/signals/traces/

[5] Fowler, M., "Event Sourcing," 2005. https://martinfowler.com/eaaDev/EventSourcing.html

---

*Word count: 2,519 (full file, including headings, code blocks, and references — see `editorial-notes-v2.md` for sourcing notes).*
