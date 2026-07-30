---
id: review-2026-07-29-eu-ai-act-decision-audit-records
title: "Review: EU AI Act record-keeping and decision/audit logs against reconstruction checklist"
topic: ai-infrastructure-gap
type: review
status: active
created: 2026-07-29
updated: 2026-07-29
tags: [evaluation, eu-ai-act, record-keeping, audit-logs, human-oversight, reconstruction]
refs: [eu2024aiAct]
sut: "Regulation (EU) 2024/1689 (AI Act) — record-keeping, automatically generated logs, human oversight, and related deployer/provider documentation duties"
checklist_version: "0.1.0"
review_kind: complete
primary_sources_available: true
related_claims: [C1, C3, C7]
---

# Review

## Bibliographic Information

**Title:** Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act)

**Issuing organization:** European Parliament and Council of the European Union

**Venue / publication:** Official Journal of the European Union, L series, 12.7.2024

**Version pin:** Regulation (EU) **2024/1689**; adopted **13 June 2024**; OJ publication **12 July 2024**; CELEX **32024R1689**

**DOI / URL:**

- ELI: [eur-lex.europa.eu/eli/reg/2024/1689/oj](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- CELEX HTML: [CELEX:32024R1689](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1689)
- No DOI; official identifier is the OJ / CELEX / ELI citation

**Primary sources inspected:**

| Source | Role |
|---|---|
| Art. 12 Record-keeping | Automatic event logs; purpose of logging; biometric minimum fields |
| Art. 13(3)(d)–(f) | Instructions: human oversight measures; log collect/store/interpret mechanisms |
| Art. 14 Human oversight | Override/disregard/interrupt capabilities; dual verification for Annex III 1(a) |
| Art. 18 Documentation keeping | 10-year retention of technical/QMS/conformity documentation |
| Art. 19 Automatically generated logs | Provider retention (≥6 months, purpose-appropriate) |
| Art. 20–21 | Corrective actions; authority access to logs |
| Art. 26(5)–(6), (10)–(11) | Deployer monitoring; deployer log retention; biometric use documentation; informing persons |
| Art. 27 | Fundamental rights impact assessment (incl. complaint mechanisms) |
| Art. 86 | Right to explanation of individual decision-making |
| Annex IV | Technical documentation elements (system-level) |
| Recitals (71), (73) | Traceability/logs intent; dual-verification may be recorded in logs |

**Primary source availability:** Sufficient for a complete review (official OJ / CELEX text retrieved and inspected).

**Not SUT:** Entire AI Act beyond the record-keeping / oversight / logs / explanation-of-decision cluster; GPAI Chapter V model obligations; prohibited practices (Art. 5); harmonised standards under Art. 40; national implementing measures; vendor logging products; GDPR as a separate instrument (cited only where the AI Act defers to it).

**Pre-scoring notes:**

- **Credit rule:** only express duties and structured minimum fields; Recital illustrations credit only where they clarify Art. 12/14 obligations (e.g. dual verification “could be sufficient” if automatically recorded in logs).
- **Do not credit** theoretical completeness of unspecified “events (logs).”
- **Mandatory** legal duties for in-scope high-risk systems (with Annex III subclass specifics).

---

## Source identity

| Field | Value |
|---|---|
| **Title** | Regulation (EU) 2024/1689 (Artificial Intelligence Act) |
| **Issuing organization** | European Parliament and Council of the European Union |
| **Publication date** | OJ 12 July 2024 (adopted 13 June 2024) |
| **Version / identifier** | 2024/1689; CELEX 32024R1689 |
| **Stable URL** | [ELI oj](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) |
| **Source type** | Binding Union regulation (authoritative regulatory primary law) |
| **Scope (this review)** | High-risk AI **record-keeping**, **automatically generated logs**, **human oversight** measures that produce or presuppose records, related **provider/deployer retention and authority access**, **system technical documentation** (Annex IV / Art. 18) insofar as it relates to auditability, and **Art. 86** individual-decision explanation rights |

Chosen because it is an official legal instrument that expressly mandates automatic recording of events for high-risk AI, durable log retention, human oversight (including override), and—for a biometric subclass—minimum decision-relevant log fields. That matches the decision-record / audit-trail family better than general observability or provenance SUTs already reviewed.

---

## Problem addressed

The Act addresses **traceability of high-risk AI system functioning**, **verification of regulatory compliance**, **post-market monitoring**, and **operational monitoring** by requiring technical capability for automatic event logging and by requiring providers/deployers to **keep** those logs when under their control (Recital 71; Arts. 12, 19, 26(6)).

It also addresses **human accountability in use**: systems must be overseen by natural persons who can monitor, interpret, disregard/override/reverse outputs, and halt the system (Art. 14); deployers must assign competent oversight persons (Art. 26(2)). For remote biometric identification (Annex III point 1(a)), it further requires dual human verification before action/decision and minimum log fields including verifying persons (Arts. 12(3), 14(5); Recital 73).

Separately, affected persons gain a **right to clear and meaningful explanations** of the AI system’s role and main elements of certain deployer decisions (Art. 86)—a contestability/accountability *right*, not a prescribed decision-record schema.

---

## 1. Design intent

Within the scored cluster, the Act’s design intent is **regulatory auditability and safe human-controlled use of high-risk AI**, not a reconstruction information model for justification/authorization/validity of arbitrary legally relevant AI-supported decisions.

Logs exist to support risk identification, substantial-modification detection, post-market monitoring, and deployer operational monitoring (Art. 12(2)). Technical documentation (Arts. 11, 18; Annex IV) demonstrates **conformity of the system**, not episode-level legal justification.

**Intent for this review:** evaluate whether these **express record-keeping and oversight duties** preserve information needed for faithful reconstruction of historically situated decisions under the repository checklist.

---

## 2. Observed capabilities

### Unit of record

**Explicitly required or structured:**

| Unit | Source support |
|---|---|
| **System events (logs)** | Art. 12(1): high-risk systems shall technically allow automatic recording of events (logs) over the lifetime of the system. |
| **Events relevant to risk / modification / monitoring** | Art. 12(2)(a)–(c): logging shall enable recording events relevant for risk (Art. 79(1)) or substantial modification; post-market monitoring (Art. 72); deployer monitoring (Art. 26(5)). |
| **Use-period timestamps (biometric subclass)** | Art. 12(3)(a): start and end date/time of each use. |
| **Reference database identity (biometric)** | Art. 12(3)(b). |
| **Matching input data (biometric)** | Art. 12(3)(c): input data for which the search led to a match. |
| **Human verifiers of results (biometric)** | Art. 12(3)(d); Art. 14(5); Recital 73 (verifications may be automatically recorded in logs). |
| **Human oversight capabilities (design)** | Art. 14(4): understand/monitor; resist automation bias; interpret; **disregard, override or reverse** output; interrupt/stop. |
| **Deployer oversight assignment** | Art. 26(2): assign oversight to persons with competence, training, and **authority**. |
| **Provider/deployer retained logs** | Arts. 19, 26(6): keep Art. 12(1) logs under their control ≥ **six months** (purpose-appropriate; subject to other law, esp. personal data). |
| **System technical documentation** | Arts. 11, 18; Annex IV: system description, development, monitoring/control, human-oversight assessment, lifecycle changes, risk management, post-market plan—kept **10 years** (Art. 18). |
| **Police-file documentation (narrow)** | Art. 26(10): each use of post-remote biometric identification documented in the relevant police file (law-enforcement context). |
| **Explanation to affected persons** | Art. 86: right to obtain explanations of AI role and main elements of certain decisions—not a mandated log field list. |

**Reasonable implications (not credited as first-class schema):**

- Generic “events” *might* include outputs, overrides, or model versions if implementers choose so—Art. 12(1)–(2) do **not** enumerate those fields for high-risk systems generally.
- Art. 86 implies deployers must be able to produce an explanation later; it does **not** specify retained decision identity, relied-upon evidence, or policy versions.

**Not explicit as decision-episode records:** governing organizational policy identity/version; authorization permit/deny under external rules; relied-upon vs available evidence packages; model/prompt/tool versions bound to a decision; integrity/signatures of logs; ordered causal event graphs; remediation/outcome records for ordinary high-risk decisions.

### Temporal properties

| Property | Assessment |
|---|---|
| **Durable retention** | **Required** for logs under provider/deployer control: ≥6 months, purpose-appropriate (Arts. 19, 26(6)). **Required** for technical/conformity documentation: 10 years (Art. 18). |
| **Timestamps** | **Explicit** for biometric use periods (Art. 12(3)(a)). **Implied** that “events” are temporally situated, but no general timestamp schema. |
| **Ordering of events** | Not required as a formal ordering/consistency model. |
| **Linkage to state at decision time** | Not required (no binding of policy/model/criteria versions to a decision timestamp). |
| **Later reconstruction** | Purpose language is **traceability of functioning**, compliance verification, and monitoring (Recital 71; Art. 12(2))—not reconstruction of justification/authorization/validity. |
| **Immutability / tamper evidence** | Not required for logs. |
| **Version preservation** | Annex IV / Art. 18 preserve **system** documentation and approved changes; Art. 13(3)(c) discloses pre-determined performance changes—**not** per-decision version pins. |
| **Correction / amendment history** | Art. 20 corrective actions for non-conformity of the *system*; not amendment history of decision records. |

### Identity and binding

| Binding | Assessment |
|---|---|
| **Particular decision / action** | No general decision-episode identifier. Biometric subclass records **each use** period and match-related inputs (Art. 12(3))—closer to use-session than checklist IC-01. |
| **System execution** | Automatic event logs over system lifetime (Art. 12(1)); underspecified schema. |
| **Input data** | Explicit only for biometric match inputs / reference database (Art. 12(3)(b)–(c)). Deployer duty that inputs be relevant/representative (Art. 26(4)) is quality control, not retention binding. |
| **Output** | Not a general required log field. Art. 14 presupposes outputs humans may override; recording overrides is not generally mandated. |
| **Evidence** | Biometric match inputs only; no IC-11 reliance distinction. |
| **Applicable policy / rule** | Not bound in logs. |
| **Model / system version** | System-level docs and lifecycle changes (Annex IV; Art. 18)—not decision-bound. |
| **Responsible human / org actor** | Explicit for biometric verifiers (Art. 12(3)(d)); oversight *assignment* required (Art. 26(2)) without a general requirement to log each oversight act. |
| **Subsequent review / override / appeal** | Art. 14 enables override/interrupt; Recital 73 allows logging dual verification; Art. 27(1)(f) expects complaint-mechanism *arrangements* in FRIA; Art. 86 is an explanation right—**no** general appeal/override audit schema. |

Generic logging is **not** treated here as decision identity.

### Human review

| Capability | Records support? |
|---|---|
| **Human approval / verification** | **Yes (narrow):** dual verification before action/decision for Annex III 1(a) (Art. 14(5)); verifying persons in logs (Art. 12(3)(d)). |
| **Human override / disregard / reverse** | **Capability required** (Art. 14(4)(d)); **record of override** not generally required. |
| **Escalation / stop** | Interrupt/stop capability required (Art. 14(4)(e)); not a mandated stop-event schema. |
| **Review / investigation** | Logs accessible to competent authorities on reasoned request (Arts. 21(2), 26(12)); post-market monitoring (Arts. 12(2), 72). Investigation of *system* risk/non-conformity (Art. 20). |
| **Contestation / appeal** | Art. 86 explanation right; Art. 27 complaint mechanisms as FRIA content—**process expectations**, not retained appeal records. |
| **Remediation** | System-level corrective actions (Art. 20); not per-decision remediation records. |
| **Allocation of responsibility** | Provider/deployer/oversight-person roles structured; biometric verifier identity in logs for one subclass. |

---

## 3. Checklist interpretation

Nearest claims: **C1** (artifact/log retention ≠ triad reconstruction), **C3** (retention without decision-time criteria binding), **C7** (explanation rights/outputs ≠ durable justification records).

| Distinction | Application |
|---|---|
| **Generic auditability** | Art. 12 event logs + Arts. 19/26(6) retention + authority access. |
| **Decision-linked records** | Strongest only for Annex III 1(a) minimum fields; elsewhere purpose-based event logging without a decision schema. |
| **Faithful reconstruction** | Requires justification/authorization/validity structure bound to decision identity—mostly outside express duties. |
| **Art. 86 explanation** | Contemporaneous/right-based account of role and main elements—not a retained justification package under authorization/validity constraints. |

---

## 4. Scored criteria

Scale: 0 = Not addressed; 1 = Mentioned or partially supported; 2 = Substantially supported; 3 = Explicitly and systematically supported.  
N/A = outside the legitimate scope of the Act’s record-keeping/oversight cluster as reviewed.

Scores are independent of other SUT reviews. Unspecified “events” do not receive credit for fields not enumerated.

### System state — **Score: 1**

| Field | Content |
|---|---|
| **Evidence** | Art. 12(1)–(2): automatic recording of events over system lifetime to support traceability of functioning, risk/substantial-modification detection, and monitoring. Annex IV §3: detailed information on monitoring, functioning and control of the AI system. |
| **Justification** | Partial support for retaining **operational event history** and system-level monitoring documentation. |
| **Why not higher** | No reconstructable decision-time system-state snapshot schema; event contents largely unspecified for general high-risk systems. |
| **Confidence** | High |

### Decision process — **Score: 2**

| Field | Content |
|---|---|
| **Evidence** | Art. 12 automatic logs for operational monitoring; Art. 14(4) requires that oversight persons can monitor, interpret, disregard/override/reverse, and interrupt; Art. 12(3)+14(5) require dual verification and log identifying verifiers for Annex III 1(a); Recital 73 notes verifications may be recorded in logs; Art. 26(5) deployer monitoring duties. |
| **Justification** | Substantial, systematic support for **human-in-the-loop process capabilities** plus **mandatory logging infrastructure**, with concrete process-linked log fields for the biometric identification subclass. |
| **Why not higher** | For high-risk systems generally, the Act does not systematically require recording each recommendation, approval, override, or multi-step decision workflow as a decision episode. Process *capability* ≠ process *record*. |
| **Confidence** | High |

### Evidence — **Score: 1**

| Field | Content |
|---|---|
| **Evidence** | Art. 12(3)(b)–(c): reference database and matching input data for Annex III 1(a). Art. 26(4): deployer ensures input data relevance/representativeness when controlling inputs. Annex IV includes training-data provenance at system-documentation level. |
| **Justification** | Partial: explicit **input/match evidence logging** for one high-risk subclass; system-level dataset documentation elsewhere. |
| **Why not higher** | No general IC-10/IC-11 decision-evidence package; no relied-upon vs available distinction; no excluded-evidence construct. |
| **Confidence** | High |

### Rules — **Score: 1**

| Field | Content |
|---|---|
| **Evidence** | Annex IV / Arts. 11 and 18: durable technical documentation of design choices, risk-management system, human-oversight measures, and conformity. Art. 13 instructions disclose intended purpose, risks, oversight measures. Art. 26(10) judicial/administrative authorisation for certain biometric uses (domain-specific). |
| **Justification** | Partial support for **system conformity and use-instruction rules**, plus a narrow external-authorisation requirement in one law-enforcement pattern. |
| **Why not higher** | Not governing policy identity/version or applicable rule paths for ordinary AI-supported decisions (IC-06–IC-08). |
| **Confidence** | High |

### Human context — **Score: 2**

| Field | Content |
|---|---|
| **Evidence** | Art. 14 human oversight design; Art. 26(2) assignment of oversight persons with competence, training, and authority; Art. 12(3)(d) identification of verifying natural persons; Art. 26(11) informing natural persons subject to Annex III decision assistance; Art. 86 explanation right for affected persons; Art. 27 FRIA categories of affected persons and complaint arrangements. |
| **Justification** | Substantial, systematic support for **oversight roles, verifier identity (subclass), affected-person notice, and explanation/complaint-facing accountability**. |
| **Why not higher** | Does not define a general retained actor/authority model for every decision episode; override acts need not be logged generally. |
| **Confidence** | High |

### Temporal continuity — **Score: 2**

| Field | Content |
|---|---|
| **Evidence** | Arts. 19 and 26(6): log retention ≥6 months (purpose-appropriate). Art. 18: 10-year documentation keeping. Art. 12(3)(a): start/end timestamps per biometric use. Annex IV lifecycle/pre-determined change descriptions. |
| **Justification** | Substantial support for **durable retention periods** and **use-period temporal marking** in the biometric subclass. |
| **Why not higher** | Retention ≠ decision-time binding of policy/model/criteria versions (IC-03/IC-07/IC-19 as reconstruction axes). No immutability requirement. |
| **Confidence** | High |

### Checklist marks (AI Act record-keeping / oversight cluster only)

Exactly one mark per item.

| ID | Mark | Notes |
|---|---|---|
| IC-01 | PARTIAL | Biometric *use* periods; no general decision-episode identity |
| IC-02 | FAIL | Decision outcomes not a general required log field |
| IC-03 | PARTIAL | Biometric use timestamps; general event time underspecified |
| IC-04 | PARTIAL | Oversight assignees; biometric verifiers in logs |
| IC-05 | PARTIAL | “Authority” for oversight persons; narrow judicial authorisation Art. 26(10) |
| IC-06 | FAIL | System conformity docs ≠ episode governing policy |
| IC-07 | FAIL | No policy-version binding to decisions |
| IC-08 | FAIL | Not defined for decision rule paths |
| IC-09 | PARTIAL | Risk/operational constraints via oversight design and monitoring purposes |
| IC-10 | PARTIAL | Biometric match inputs / reference DB only |
| IC-11 | FAIL | No reliance distinction |
| IC-12 | FAIL | Not defined |
| IC-13 | PARTIAL | System/lifecycle documentation—not decision-bound model version in logs |
| IC-14 | N/A | Outside this cluster’s purpose |
| IC-15 | N/A | Outside this cluster’s purpose |
| IC-16 | N/A | Outside this cluster’s purpose |
| IC-17 | FAIL | Not a required log field |
| IC-18 | PARTIAL | Intended purpose / misuse context in instructions; not decision assumption records |
| IC-19 | PARTIAL | Retention floors; biometric use intervals |
| IC-20 | PARTIAL | Annex III / FRIA / Art. 86 legal-effects framing—not per-decision jurisdiction object |
| IC-21 | FAIL | No tamper-evidence duty for logs |
| IC-22 | N/A | Outside purpose as reviewed |
| IC-23 | PARTIAL | Annex IV training-data provenance at system level |
| IC-24 | PARTIAL | Annex IV architecture/data descriptions; not decision lineage |

---

## Base-triad assessment

Base profile: legally relevant AI-supported decisions (checklist §8.3).

| Target | Present | Partial | Missing | Result |
|---|---|---|---|---|
| **Authorization** | Oversight authority expectations; narrow Art. 26(10) authorisation | Actor/verifier identity (subclass) | Governing policy id/version; applicable rules; general decision permit/deny record | **FAIL** |
| **Justification** | Biometric match inputs; Art. 86 explanation *right* | Event logs of unspecified content; system technical docs | Relied-upon evidence package; decision outcome record; decision-bound criteria | **FAIL** |
| **Validity** | Risk/monitoring-oriented logging purposes; system constraints via oversight design | Retention enabling later inspection | Then-applicable rules/constraints bound to the episode | **FAIL** |
| **Faithful reconstruction (base)** | — | — | Triad incomplete | **FAIL** |

**Elements present:** mandatory automatic logging capability; durable log retention (≥6 months); durable system documentation (10 years); human oversight capabilities including override/stop; biometric-subclass minimum fields (use interval, reference DB, matching inputs, verifier identities); authority access to logs; Art. 86 explanation right.

**Partial:** general event logs without field schema; human override *capability* without mandated override records; system version/lifecycle docs unbound to decisions.

**Missing for triad pass:** stable decision identity; decision outcome; policy/rule version binding; relied-upon evidence distinction; general authorization decision structure.

---

## Claim relevance

This review supplies unit-level evidence relevant to **C1** (legally mandated logs and conformity documentation still underspecify bindings needed for triad reconstruction), **C3** (retention periods without decision-time criteria/model/policy binding), and **C7** (Art. 86 explanation rights and transparency-to-deployers duties are not durable justification-record architectures). The claims were not updated, and no aggregate conclusion was derived.

---

## 5. Evaluation boundary

- Credit only Arts. 12, 13(3)(d)–(f), 14, 18–21, 26(5)–(6)/(10)–(11), 27, 86, Annex IV, and clarifying Recitals 71/73.
- Do **not** invent log fields from “events” generally.
- Do **not** treat Art. 86 explanations as IC-11 justification packages.
- Do **not** score GDPR, national police-file practice, or future harmonised standards as AI Act capabilities.
- Implementation quality must not influence scoring.

---

## 6. Threats to validity

- Minimum log fields are **subclass-specific** (Annex III 1(a)); over-generalising them to all high-risk systems would inflate scores.
- Recital 73’s “could be sufficient” language about recording dual verification is facilitative, not a full override-audit schema.
- “Traceability of functioning” (Recital 71) is easy to conflate with checklist faithful reconstruction.
- Retention “appropriate to intended purpose” and personal-data law carve-outs can shrink practical durability.
- OJ consolidated text vs later corrigenda: this review pins CELEX 32024R1689 as retrieved 2026-07-29.

---

## 7. Remaining uncertainty

- Whether forthcoming harmonised standards under Art. 40 will specify decision-linked log schemas—would require a separate version-pinned review.
- Composition of AI Act logs + policy-engine decision logs + evidence stores is out of scope.
- Claims **C1**/**C3**/**C7** receive unit-level evidence only; aggregate status is not updated.

---

## Limitations

- **Scope:** high-risk (and listed subclasses); not all AI systems.
- **Mandatory** within scope, but many log *contents* are purpose-relative rather than field-mandatory.
- **Domain-specific** intensification for remote biometric identification and certain law-enforcement uses.
- Requires **records without sufficient technical bindings** for checklist decision identity, policy versions, or reliance.
- Assumes external governance (deployer organisation of oversight; national competent authorities; personal-data regimes).
- Omits general authorization reconstruction, provenance graphs, policy versioning, tamper-evident decision identity, and mandated override/appeal audit trails.

---

## 8. Overall assessment / Principal finding

**Regulation (EU) 2024/1689 mandates automatic event logging, durable log retention, human oversight (including override/stop), authority access to logs, and—for remote biometric identification—minimum use- and verification-linked log fields.** That is **stronger than generic “auditability” rhetoric**: it is decision-adjacent record-keeping for monitoring, compliance, and (in one subclass) human verification.

It is **not** faithful reconstruction of past decision context under the repository checklist. Missing are systematic decision identity/outcomes, relied-upon evidence packages, governing policy/rule versions, and decision-time binding. Art. 86 supplies an explanation *right*, not a reconstruction record.

**Principal finding:** the AI Act’s record-keeping cluster establishes **legally mandated, retention-backed operational audit logs and human-oversight duties**—with **decision-linked minimum fields only in a narrow biometric subclass**—but **fails** the base triad for faithful reconstruction of justification, authorization, and validity.

**Not updated:** comparison matrix; reconstruction evaluation dataset; aggregate claims; coverage audit; synthesis documents.
