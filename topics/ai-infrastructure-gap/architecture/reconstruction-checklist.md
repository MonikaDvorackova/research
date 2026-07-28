---
id: arch-ai-infrastructure-gap-reconstruction-checklist
title: "Reconstruction checklist: minimum information for historical AI-assisted decisions"
topic: ai-infrastructure-gap
type: architecture
status: draft
created: 2026-07-28
updated: 2026-07-28
tags: [evaluation, reconstruction, architecture, governance]
normative_for: evaluation
version: 0.1.0
---

## Reconstruction checklist

**Document role:** Evaluation framework (criteria), not a solution architecture.  
**Status:** `draft` — engineering criteria and hypotheses pending scenario validation.  
**Applies to:** Any system or abstraction under test (e.g. OpenTelemetry, event sourcing, W3C PROV, OPA, Cedar, AIGov Core, future designs).  
**Does not define:** Storage format, API, product module, or named architectural layer.

---

### 1. Purpose and non-purpose

#### 1.1 Purpose

This document defines the **minimum information categories and bindings** against which one may evaluate whether a historically situated **AI-assisted decision** can be **faithfully reconstructed** with respect to:

1. **Justification** — on what grounds the outcome was supported under the criteria then treated as applicable;
2. **Authorization** — under what authority and governing rules the outcome was permitted;
3. **Validity** — whether the outcome conformed to constraints and rules then in force.

#### 1.2 Non-purpose

This document **does not**:

- propose an architecture, layer, product, or reference implementation;
- rank or endorse vendor technologies;
- assert that current systems fail (that is a separate empirical claim);
- equate reconstruction with compliance certification in any jurisdiction.

#### 1.3 Independence from implementation technologies

**Engineering criterion:** Reconstruction adequacy SHALL be judged by whether required *information and bindings* are recoverable for a defined decision episode—not by whether a particular technology (logs, traces, ledgers, policy engines, graphs) is present.

**Rationale (hypothesis):** Implementation mechanisms are many-to-one relative to information needs. Evaluating “has OpenTelemetry” or “has PROV” without an information checklist conflates *mechanism presence* with *reconstruction completeness*. A technology-independent checklist enables fair comparison and composition testing: the same criteria apply to OTEL attributes, event-sourced projections, PROV graphs, OPA decision logs, Cedar authorizations, AIGov Core records, or any future design.

**Consequence for evaluation:** An abstraction “passes” a checklist item only if it can supply that item (alone or in an explicitly documented composition) for the scenario under test—not merely because it is related to auditing or AI governance in marketing terms.

---

### 2. Terms (provisional)

Unless marked *universally accepted*, definitions are **working senses** for this checklist and may be revised.

| Term | Working sense | Status |
|---|---|---|
| **AI-assisted decision** | An identifiable commit to an action, classification, recommendation acceptance, or controlled outcome in which AI system outputs materially participated | provisional |
| **Decision episode** | The bounded set of facts, rules, and bindings associated with one decision identity at decision time | provisional |
| **Reconstruction** | Production, by a later party using retained structured information, of statements about justification, authorization, and validity *as of decision time* | provisional |
| **Faithful reconstruction** | See §3 | provisional |
| **Binding** | An explicit association between information items and the same decision identity (and, where required, decision time / version axes) | provisional |
| **Retained** | Persistently available to the reconstructor under the retention policy assumed by the evaluation scenario | provisional |

The triad *justification / authorization / validity* is treated as **separable evaluation targets** (hypothesis; see claim inventory C2). An abstraction may satisfy one without satisfying others.

---

### 3. Faithful reconstruction

#### 3.1 Definition (engineering criterion)

**Faithful reconstruction** of a decision episode is achieved when a competent reconstructor, given only retained structured information (plus publicly stated reconstruction procedure for the system under test), can:

1. **Identify** the decision episode unambiguously;
2. **State the outcome** that was decided;
3. **Locate the episode in time** (and, where the scenario requires it, in applicable versioned contexts);
4. **Restate authorization**: who/what was authorized to decide, under which governing policy (including version), yielding what permit/deny (or equivalent) result;
5. **Restate justification**: which evidence and criteria were treated as supporting the outcome, including what was relied upon versus merely available;
6. **Restate validity**: which constraints and applicable rules were treated as in force, and whether the outcome was represented as conforming;
7. **Distinguish** contemporaneous system narrative from decision-time structure (i.e., avoid silent substitution of *current* policies, models, or explanations for *historical* ones).

Completeness is scenario-relative: see requirement classes in §5.

#### 3.2 Adequacy threshold (hypothesis)

**Hypothesis:** “Faithful” does **not** require bit-exact replay of all internal compute, full model weight reproducibility, or recovery of every discarded intermediate token. It requires recovery of the **normative and evidential basis** of the decision as retained structure—not an unlimited forensic dump.

Evaluators MUST declare the scenario’s completeness bar (e.g. internal engineering review vs. external audit) before scoring.

#### 3.3 Failure modes (non-exhaustive)

Reconstruction is **not faithful** if the reconstructor must rely on:

- undocumented operator memory;
- current (post-drift) policy or model versions unbound to the episode;
- post-hoc explanations generated after the fact without decision-time binding;
- ambiguous correlation across stores that cannot be shown to refer to the same decision identity.

---

### 4. What reconstruction is not

The following capabilities are **related but not equivalent**. Passing their native success criteria does **not**, by itself, establish faithful reconstruction under §3.

| Concept | Typical success criterion | Why it is not reconstruction (engineering criterion) |
|---|---|---|
| **Replay** | Re-execute a workflow or event log to obtain the same computational path or state | Replay may restore *how* steps ran without restoring *why* the outcome was authorized/justified/valid under then-applicable criteria; non-determinism and missing normative inputs often break equivalence |
| **Audit logging** | Record that events occurred (who/what/when at some granularity) | Audit trails may omit governing policy versions, relied-upon evidence, or validity constraints; volume ≠ normative completeness |
| **Provenance / lineage** | Show derivation: entities, activities, agents, data/model lineage | Provenance answers “from what / by whom derived” more directly than “under which authorization and justification criteria was this outcome valid” |
| **Explainability** | Produce a human-facing account of model behavior (local/global) | Explanations are often contemporaneous, unstable, or unbound to authorization/validity; UX explanation ≠ durable decision-time justification record |
| **Reasoning traces** | Retain chain-of-thought, tool calls, or intermediate reasoning artifacts | Traces may reconstruct token/tool paths without binding to governing policy versions, authority, or validity rules then in force |
| **Model reproducibility** | Re-obtain the same model outputs given weights, seeds, and inputs | Reproducing an output does not reconstruct authorization or validity; may be impossible or irrelevant for faithfulness under §3.2 |

**Hypothesis:** Conflating any row above with faithful reconstruction is a primary source of false confidence in existing stacks.

---

### 5. Requirement classes

Every information category in §6 is labeled with exactly one default class. Scenario profiles may elevate Optional → Conditionally required, or Conditionally required → Required.

| Class | Meaning for evaluation |
|---|---|
| **Required** | Omission means the checklist item **fails** for any scenario claiming faithful reconstruction of the full triad under §3.1 |
| **Conditionally required** | Omission fails **when** the stated condition holds for the scenario; otherwise N/A |
| **Optional** | Strengthens confidence, integrity, or forensic depth; omission does **not** by itself fail faithfulness for the base triad, unless a scenario profile elevates it |

**Binding criterion (applies to all classes):** Where an item is Required or Conditionally required, it MUST be recoverable **as bound to the same decision identity** (and to decision-time version axes where versioning is in scope). Unbound global “latest policy” stores do not satisfy versioned items.

---

### 6. Information categories

Categories are **candidates for minimum structure**. The set is **not claimed complete**. Items may be merged in an implementation if semantics are preserved; evaluators score **information presence**, not table row count.

For each category:

- **Description** — what must be recoverable  
- **Why it matters** — role in justification, authorization, and/or validity  
- **When required** — default class and conditions  
- **Omission** — whether omission prevents faithful reconstruction under the default class  

#### 6.1 Identity and outcome

##### IC-01 Decision identity

| | |
|---|---|
| **Description** | Stable identifier (or equivalent unambiguous key) for the decision episode |
| **Why it matters** | Without identity, no other category can be bound; reconstruction collapses into ambiguous log correlation |
| **When required** | **Required** for all scenarios |
| **Omission** | **Prevents** faithful reconstruction |

##### IC-02 Decision outcome

| | |
|---|---|
| **Description** | The outcome that was decided (action taken, label assigned, recommendation accepted/rejected, control signal, etc.), in a form interpretable without the live system |
| **Why it matters** | Reconstruction without outcome has nothing to justify, authorize, or validate |
| **When required** | **Required** |
| **Omission** | **Prevents** faithful reconstruction |

##### IC-03 Decision time

| | |
|---|---|
| **Description** | Timestamp (and declared clock domain) at which the decision is considered to have occurred |
| **Why it matters** | Anchors historical applicability of policies, models, and rules; enables temporal reconstruction |
| **When required** | **Required** |
| **Omission** | **Prevents** faithful reconstruction for historically situated claims |

#### 6.2 Actors and authority

##### IC-04 Actor(s)

| | |
|---|---|
| **Description** | Parties that participated in producing or accepting the decision (human users, service principals, agents, delegated roles)—as known at decision time |
| **Why it matters** | Authorization and accountability attach to actors; justification may depend on who acted |
| **When required** | **Required** when any human or non-system principal can affect the outcome; **Conditionally required** for fully autonomous system-only episodes if the scenario still demands accountability attribution (then the system principal counts as actor) |
| **Omission** | **Prevents** when accountability/authorization attribution is in scope; otherwise may leave authorization incomplete |

##### IC-05 Authority

| | |
|---|---|
| **Description** | The authority under which actors were permitted to decide (role, delegation, mandate, system authority statement)—distinct from the policy text itself when authority is external to a single policy document |
| **Why it matters** | Separates “who may decide” from “what rule was evaluated” |
| **When required** | **Conditionally required** when authorization is in scope for the scenario (default for governance/audit scenarios: treat as required) |
| **Omission** | **Prevents** faithful *authorization* reconstruction when the condition holds |

#### 6.3 Policy and rules

##### IC-06 Governing policy

| | |
|---|---|
| **Description** | Identification of the policy artifact(s) treated as governing the decision (name/URI/id), not merely a boolean allow/deny |
| **Why it matters** | Authorization and often validity are uninterpretable without knowing which policy governed |
| **When required** | **Required** when the decision is policy-governed (hypothesis: most AI-assisted production decisions under this research program are); else N/A |
| **Omission** | **Prevents** authorization (and often validity) reconstruction when policy-governed |

##### IC-07 Policy version

| | |
|---|---|
| **Description** | Version, hash, or immutable snapshot reference of governing policy *as applicable at decision time* |
| **Why it matters** | Policies drift; “current policy” substitution falsifies historical authorization/validity |
| **When required** | **Required** whenever IC-06 applies |
| **Omission** | **Prevents** historically faithful authorization/validity reconstruction |

##### IC-08 Applicable rules

| | |
|---|---|
| **Description** | The specific rules, clauses, or policy paths that were treated as applicable (not only the policy bundle id)—including evaluation inputs/outputs where needed to interpret the path |
| **Why it matters** | Bundle identity alone may not reveal *which* rules fired or were decisive |
| **When required** | **Conditionally required** when policies contain multiple rules/paths and reconstruction must explain authorization/validity beyond allow/deny |
| **Omission** | **Prevents** detailed authorization/validity reconstruction when the condition holds; allow/deny-only scenarios may still pass a reduced profile |

##### IC-09 Constraints

| | |
|---|---|
| **Description** | Hard constraints treated as limiting the outcome space (safety limits, allow-lists, regulatory caps, system invariants) |
| **Why it matters** | Validity often depends on constraints distinct from discretionary justification |
| **When required** | **Conditionally required** when constraints exist in the decision setting |
| **Omission** | **Prevents** validity reconstruction when constraints existed and mattered |

#### 6.4 Evidence and reliance

##### IC-10 Evidence used (available to the decision process)

| | |
|---|---|
| **Description** | Inputs/evidence items presented to or retrieved by the decision process (documents, features, retrieved context, sensor readings, prior decisions) |
| **Why it matters** | Justification is relative to an evidential field; availability defines the opportunity set |
| **When required** | **Required** for justification reconstruction in evidence-using decisions (default for AI-assisted decisions) |
| **Omission** | **Prevents** justification reconstruction |

##### IC-11 Evidence actually relied upon

| | |
|---|---|
| **Description** | Subset (or weighting/selection record) of evidence treated as decisive or relied upon for the outcome—not merely present in context |
| **Why it matters** | **Hypothesis:** Conflating “in context” with “relied upon” is a primary failure mode of naive log retention |
| **When required** | **Required** whenever IC-10 applies and selection/attention/filtering can change justification |
| **Omission** | **Prevents** faithful justification reconstruction when reliance is non-trivial |

##### IC-12 Excluded evidence

| | |
|---|---|
| **Description** | Evidence known to the process but excluded, filtered, redacted, or ruled out—and, where applicable, the exclusion reason |
| **Why it matters** | Justification and fairness/validity challenges often turn on what was *not* considered |
| **When required** | **Conditionally required** when exclusion/filtering occurred or when the scenario profile demands negative evidential accounting |
| **Omission** | **Prevents** faithful justification (and some validity) reconstruction when the condition holds |

#### 6.5 Model and tool context

##### IC-13 Model version

| | |
|---|---|
| **Description** | Identifier/version/hash of model(s) whose outputs materially participated |
| **Why it matters** | Model drift changes outputs and implicit decision behavior; historical justification may depend on the model then used |
| **When required** | **Required** when model outputs materially participated; else N/A |
| **Omission** | **Prevents** historically faithful reconstruction of model-participating decisions |

##### IC-14 Prompts

| | |
|---|---|
| **Description** | Prompt templates and instance prompts (system/user/tool) that materially shaped model participation, including versioned template ids where templates are managed |
| **Why it matters** | For LLM-mediated decisions, prompts often encode criteria and task framing that function as de facto policy/justification structure |
| **When required** | **Conditionally required** when prompts materially shaped the outcome |
| **Omission** | **Prevents** justification reconstruction when the condition holds |

##### IC-15 Tools

| | |
|---|---|
| **Description** | Tools/functions invoked during the episode, with versions/ids and relevant arguments/results as needed for interpretation |
| **Why it matters** | Tool results often constitute relied-upon evidence or actions |
| **When required** | **Conditionally required** when tools were invoked |
| **Omission** | **Prevents** justification (and sometimes outcome) reconstruction when the condition holds |

##### IC-16 External services

| | |
|---|---|
| **Description** | External services consulted (identity, identity provider responses, credit bureau, weather, feature stores, etc.) with enough identity/versioning to interpret responses |
| **Why it matters** | External responses may be relied-upon evidence or authorization inputs |
| **When required** | **Conditionally required** when external services materially participated |
| **Omission** | **Prevents** reconstruction of dependent justification/authorization when the condition holds |

##### IC-17 Confidence

| | |
|---|---|
| **Description** | Scores, calibrated probabilities, thresholds, or uncertainty representations that were treated as decision inputs or gates |
| **Why it matters** | Thresholds often encode validity/authorization gates (“only auto-approve if …”) |
| **When required** | **Conditionally required** when confidence/thresholds affected the outcome |
| **Omission** | **Prevents** justification/validity reconstruction when the condition holds |

#### 6.6 Assumptions and contexts

##### IC-18 Assumptions

| | |
|---|---|
| **Description** | Explicit assumptions treated as holding for the decision (data freshness, user consent state, environment mode, fall-back defaults) |
| **Why it matters** | Invalid assumptions void justification/validity even when policy allow/deny is recorded |
| **When required** | **Conditionally required** when the process relies on stated or default assumptions that are not otherwise implied by IC-06–IC-09 |
| **Omission** | **May prevent** faithful justification/validity reconstruction when assumptions were material |

##### IC-19 Temporal context

| | |
|---|---|
| **Description** | Temporal frame beyond a single timestamp: effective intervals, as-of times for reference data, business time vs. system time, retention of bi-temporal axes where used |
| **Why it matters** | **Hypothesis:** Many failures labeled “missing justification” are temporal binding failures |
| **When required** | **Conditionally required** when reference data, policies, or entitlements are time-varying |
| **Omission** | **Prevents** historically faithful reconstruction when the condition holds |

##### IC-20 Legal context

| | |
|---|---|
| **Description** | Jurisdiction, contractual regime, or regulatory frame treated as applicable to the episode (identifiers/references—not a legal opinion) |
| **Why it matters** | Validity and authorization may be jurisdiction-relative |
| **When required** | **Conditionally required** when multi-jurisdictional or explicitly regulated scenarios are in scope |
| **Omission** | **Prevents** validity/authorization reconstruction for those scenarios; N/A for pure internal technical gates |

#### 6.7 Integrity and derivation

##### IC-21 Integrity information

| | |
|---|---|
| **Description** | Integrity metadata for retained decision-bound records (checksums, content hashes, Merkle references, storage WORM flags)—sufficient to detect tampering relative to stated trust assumptions |
| **Why it matters** | Without integrity, reconstruction may be possible but not trustworthy |
| **When required** | **Optional** for base faithfulness of *content*; **Conditionally required** when the scenario profile demands tamper-evident reconstruction (audit/forensic profiles: elevate) |
| **Omission** | Does **not** by itself fail §3.1 content faithfulness; **fails** integrity-elevated profiles |

##### IC-22 Signatures

| | |
|---|---|
| **Description** | Cryptographic or organizational signatures/attestations bound to the decision record or critical sub-artifacts |
| **Why it matters** | Supports non-repudiation and authenticity of actors/authority claims |
| **When required** | **Optional** by default; **Conditionally required** under scenarios demanding non-repudiation |
| **Omission** | Does **not** fail base faithfulness; **fails** non-repudiation profiles |

##### IC-23 Provenance

| | |
|---|---|
| **Description** | Structured derivation metadata for evidence, models, and outcomes (who/what/when derived), bound to the decision identity |
| **Why it matters** | Supports justification via lineage; does not replace authorization/validity criteria |
| **When required** | **Conditionally required** when lineage is necessary to interpret evidence/model trust for the scenario |
| **Omission** | **May prevent** justification reconstruction when lineage is material; does not substitute for IC-06–IC-08 |

##### IC-24 Lineage

| | |
|---|---|
| **Description** | End-to-end data/feature/model lineage relevant to the episode (may overlap IC-23; scored separately when lineage systems are distinct from decision-bound provenance) |
| **Why it matters** | Distinguishes pipeline heritage from decision-time normative basis |
| **When required** | **Optional** for base triad; **Conditionally required** when scenario disputes turn on training/pipeline heritage |
| **Omission** | Does **not** fail base faithfulness unless elevated by scenario |

---

### 7. Binding and composition criteria

**Engineering criteria** (apply when scoring any system):

1. **Same-identity binding:** Required/conditionally required items MUST be associable to IC-01 without undocumented heuristics.
2. **Decision-time binding:** Versioned items (IC-07, IC-13, and temporal reference data under IC-19) MUST reflect applicability *at IC-03*, not merely “latest at query time.”
3. **Separation of reliance:** Where IC-11 is required, “all context logged” without reliance distinction does **not** pass IC-11.
4. **Composition allowed:** An abstraction may fail alone but pass as part of a **declared composition**. Evaluators MUST list components and the binding mechanism.
5. **No credit for adjacent capability:** Presence of replay, explainability, or model reproducibility earns no checklist credit unless mapped to specific IC-* items.

---

### 8. Evaluation checklist (scoring sheet)

Use this sheet for each **system under test (SUT)** and each **scenario**.  
Marks: `PASS` | `FAIL` | `N/A` | `PARTIAL` (PARTIAL requires written missing element).

#### 8.1 Header

| Field | Value |
|---|---|
| SUT name / version | |
| Composition components (if any) | |
| Scenario id | |
| Scenario completeness profile | base triad / audit / forensic (specify) |
| Evaluator | |
| Date | |
| Checklist document version | 0.1.0 |

#### 8.2 Category scores

| ID | Category | Class | Score | Evidence pointer (doc/field/API) | Notes |
|---|---|---|---|---|---|
| IC-01 | Decision identity | Required | | | |
| IC-02 | Decision outcome | Required | | | |
| IC-03 | Decision time | Required | | | |
| IC-04 | Actor(s) | Req / Cond | | | |
| IC-05 | Authority | Cond | | | |
| IC-06 | Governing policy | Cond/Req if policy-governed | | | |
| IC-07 | Policy version | Req w/ IC-06 | | | |
| IC-08 | Applicable rules | Cond | | | |
| IC-09 | Constraints | Cond | | | |
| IC-10 | Evidence used | Req if evidence-using | | | |
| IC-11 | Evidence relied upon | Cond/Req as in §6 | | | |
| IC-12 | Excluded evidence | Cond | | | |
| IC-13 | Model version | Cond | | | |
| IC-14 | Prompts | Cond | | | |
| IC-15 | Tools | Cond | | | |
| IC-16 | External services | Cond | | | |
| IC-17 | Confidence | Cond | | | |
| IC-18 | Assumptions | Cond | | | |
| IC-19 | Temporal context | Cond | | | |
| IC-20 | Legal context | Cond | | | |
| IC-21 | Integrity information | Opt / Cond | | | |
| IC-22 | Signatures | Opt / Cond | | | |
| IC-23 | Provenance | Cond | | | |
| IC-24 | Lineage | Opt / Cond | | | |

#### 8.3 Triad roll-up

| Target | PASS only if | Score |
|---|---|---|
| **Authorization reconstructable** | IC-01–03; IC-05–07 as applicable; IC-08 when multi-rule; IC-04 when attribution required | |
| **Justification reconstructable** | IC-01–03; IC-10–11 as applicable; IC-12–18 as conditioned by scenario | |
| **Validity reconstructable** | IC-01–03; IC-06–09 as applicable; IC-19–20 as conditioned; constraints/rules decisive | |
| **Faithful reconstruction (base)** | All three triad rows PASS under declared profile | |
| **Faithful reconstruction (elevated)** | Base PASS + elevated IC-21/IC-22 as profiled | |

#### 8.4 Suggested SUT rows (empty templates)

Run §8.2–8.3 separately for:

| SUT | Composition notes |
|---|---|
| OpenTelemetry (traces/metrics/logs) | |
| Event sourcing | |
| W3C PROV | |
| OPA decision logs | |
| Cedar authorizations / logs | |
| AIGov Core | |
| Declared composition: ________ | |
| Future architecture: ________ | |

---

### 9. Conformance language for later use

When this checklist is cited by later specifications or publications:

- **Checklist PASS** means: for a stated scenario and profile, required and applicable conditionally required items were recoverable under §7.
- **Checklist FAIL** means: at least one such item was missing, unbound, or only available via non-retained narrative.
- **No architecture claim:** PASS/FAIL does not imply that a new layer is necessary or unnecessary; it only scores information adequacy of the SUT or composition.

---

### 10. Revision policy

- Breaking changes to Required items increment **minor** version while `status: draft`, then **major** after acceptance.
- Adding categories increments minor version.
- Scenario profiles may tighten classes without changing this document if published as profile overlays; overlays MUST NOT weaken Required items silently.

---

### 11. Open issues

1. Is the justification/authorization/validity triad the right partition, or should “accountability” be a fourth target?
2. Minimum bar for IC-11 (relied-upon evidence) in opaque model settings—hypothesis under active research.
3. Whether IC-23 and IC-24 should merge after empirical scoring.
4. Completeness of category list pending Phase 0 scenarios in `future-work/research-plan.md`.

---

### Related artifacts

| Artifact | Relationship |
|---|---|
| [charter.md](../charter.md) | Problem framing; kill list consumes this checklist |
| [claim-inventory.md](claim-inventory.md) | Claims to be tested *using* these criteria |
| [research-plan.md](../future-work/research-plan.md) | Phase 0–1 produce scenarios scored here |
