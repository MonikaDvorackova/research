---
id: review-2026-07-29-oasis-ws-humantask-human-review-workflow
title: "Review: OASIS WS-HumanTask 1.1 against reconstruction checklist (human review workflow records)"
topic: ai-infrastructure-gap
type: review
status: active
created: 2026-07-29
updated: 2026-07-29
tags: [evaluation, ws-humantask, human-workflow, review-records, escalation, reconstruction]
refs: [oasis2010wsHumanTask]
sut: "OASIS WS-HumanTask Specification Version 1.1 — Committee Specification 01 (17 August 2010)"
checklist_version: "0.1.0"
review_kind: complete
primary_sources_available: true
related_claims: [C1, C2, C6]
compares_to_reviews:
  - review-2026-07-29-nistir-8312-xai-principles
  - review-2026-07-29-eu-ai-act-decision-audit-records
---

# Review

## Bibliographic Information

**Title:** Web Services – Human Task (WS-HumanTask) Specification Version 1.1

**Editors:** Luc Clément; Dieter König; Vinkesh Mehta; Ralf Mueller; Ravi Rangaswamy; Michael Rowley; Ivana Trickovic

**Issuing organization:** OASIS (BPEL4People / WS-HumanTask Technical Committee)

**Version pin:** Version **1.1**, **Committee Specification 01**, **17 August 2010**

**DOI / URL:**

- This version (HTML): [ws-humantask-1.1-spec-cs-01.html](http://docs.oasis-open.org/bpel4people/ws-humantask-1.1-spec-cs-01.html)
- Latest version: [ws-humantask-1.1.html](http://docs.oasis-open.org/bpel4people/ws-humantask-1.1.html)
- OASIS standard page: [ws-humantask-1-1](https://www.oasis-open.org/standard/ws-humantask-1-1/)
- No DOI; stable official identifier is the OASIS Committee Specification URI above

**Source type:** Primary technical specification (OASIS Committee Specification)

**Primary sources inspected:**

| Source | Role |
|---|---|
| §1–§3 (concepts; generic human roles; composite tasks; routing) | Design intent; reviewer roles; assignment patterns |
| §3.8 Task Instance Data | Presentation / context / operational data |
| §4.7–§4.10 (deadlines, escalation, state transitions) | Timing, escalation, approval/completion/fail/skip |
| §4.11 History of a Human Task; `getTaskHistory` | Retrievable task-event history |
| §7.1 Task Client API (claim, complete, fail, forward, delegate, comments, attachments, queries) | Concrete operations and queryable columns |

**Primary source availability:** Sufficient for a complete review (official CS-01 HTML retrieved and inspected).

**Not SUT:** BPEL4People process orchestration beyond HumanTask bindings; BPMN 2.0; Camunda/Flowable/engine-specific history schemas; EU AI Act; NISTIR 8312; vendor task-list products; organizational SOPs layered on top of the API.

**Pre-scoring notes:**

- Credit only **first-class task instance data, state transitions, APIs, and history retrieval** defined by WS-HumanTask 1.1.
- Distinguishing rule: **operations that humans may perform** ≠ **duty to preserve durable legal decision records**. History/query APIs imply processor-accessible instance history; they do **not** mandate retention periods, immutability, or binding to AI model/policy versions.
- `MAY` features (ad-hoc attachments, comments, advanced query) cannot raise scores to “systematic” alone.

---

## Source identity

| Field | Value |
|---|---|
| **Title** | WS-HumanTask Specification Version 1.1 |
| **Issuing organization** | OASIS |
| **Publication date** | 17 August 2010 (CS-01) |
| **Version / identifier** | 1.1 / Committee Specification 01 |
| **Stable URL** | [CS-01 HTML](http://docs.oasis-open.org/bpel4people/ws-humantask-1.1-spec-cs-01.html) |
| **Source type** | Primary technical specification |
| **Scope (this review)** | Human task lifecycle, people assignments, operational data, deadlines/escalation, client API, and task history—as a model of **human review / approval / override-class workflow records** |

Chosen because it defines **concrete procedural operations and instance/history structures** for human work (claim, start, complete, fail, skip, forward, delegate, escalate via deadlines, comments, attachments), not merely a requirement that humans oversee AI.

---

## Problem addressed

WS-HumanTask addresses **integration of human work into service-oriented applications**: defining human tasks (and notifications), their properties, state machines, people assignments, and interoperable APIs so applications and task-list clients can create tasks, assign them, carry them out, and observe outcomes (§1 Abstract; §1.4 architecture).

In consequential decision workflows, this supplies a **standard shape for human-gate records**: who may act, who did act, when, with what input/output, via which lifecycle transitions, with optional notes/attachments and a retrievable event history—without itself defining AI justification, legal authorization, or long-term archival policy.

---

## 1. Design intent

The specification introduces human tasks as work to be accomplished by people—typically within business processes, but also as human interactions invoked as services (§Abstract). It standardizes:

- task/notification definitions and instance data;
- generic human roles and people assignment;
- lifecycle behavior and client operations;
- coordination protocol with a task parent;
- deadlines and escalation actions;
- history retrieval for a task.

**Intent for this review:** evaluate whether these **human-task instance and history structures** preserve information needed for faithful reconstruction of legally relevant AI-supported *decisions*—especially human review, approval, override, escalation, and responsibility—while distinguishing procedural/API capabilities from preservation duties.

---

## 2. Observed capabilities

### Human reviewer / decision-maker identity

- Users and organizational entities (`htt:tUser`, `htt:tOrganizationalEntity`) identify people and groups (§3.5).
- **Actual owner** is the person performing the task after claim (§3.1).
- Query view includes **CreatedBy**, **LastModifiedBy**, and generic-human-role columns (§7.1 complete task view).
- Operations execute on behalf of an invoking person; unauthorized callers get `illegalAccessFault` / `recipientNotAllowed` (§7.1).

### Reviewer role and authority

First-class **generic human roles** (§3.1):

| Role | Documented function |
|---|---|
| Task initiator | Creates the task instance |
| Task stakeholders | Oversight/outcome responsibility; attachments, forwarding, admin actions; ≥1 person at runtime |
| Potential owners | May claim and complete; pre-claim influence (priority, comments, attachments) |
| Actual owner | Performs the task (claim, release, forward, suspend/resume, etc.) |
| Excluded owners | Cannot become actual/potential owner |
| Business administrators | Stakeholder-like authority at definition level; ≥1 at runtime |
| Notification recipients | Informational recipients (e.g., missed deadlines) |

Authority here is **task-processor authorization** for operations by role/state—not external legal mandate or governing-policy authority (IC-05 in the checklist sense).

### Assignment and timing of review

- People assignment via logical people groups, literals, expressions, and **routing patterns** (sequence/parallel) (§3.3–§3.5; §4.7).
- Timestamps in context/query view: CreatedTime, ActivationTime, ExpirationTime, StartByTime, CompleteByTime, LastModifiedTime (§3.8.2; §7.1).
- Start/completion **deadlines** with escalation actions and notifications (§4.deadline material; Escalated column).

### Automated output reviewed

- Task **input data** is first-class operational data (§3.8.3)—suitable to carry an AI recommendation/output as application payload.
- The specification does **not** define an “AI output” type; binding of model output into `input` is an application modeling choice.

### Evidence considered

- **Input / output / fault** messages as operational data (§3.8.3).
- **Ad-hoc attachments** (`MAY`): name, type, content or URL, attachedTime, attachedBy (§3.8.3.1).
- **Comments** (`MAY`): text with addedBy/addedTime and last-modified audit fields (§3.8.3.2).
- No relied-upon vs available evidence distinction (IC-11).

### Approval, rejection, override, or escalation

| Action class | Spec support |
|---|---|
| **Approval-like completion** | `complete` → Completed, with optional output data (§7.1) |
| **Rejection / unsuccessful outcome** | `fail` → Failed, with fault name/data when defined (§7.1) |
| **Skip** | skipable tasks → Obsolete; coordination `skipped` (§4.10; §8) |
| **Reassignment / handoff** | `forward`, `delegate`, `nominate`, `release`, `claim` (§7.1) |
| **Interrupt / pause** | `stop`, `suspend` / `suspendUntil`, `resume`; parent `exit` (§7.1; §8) |
| **Deadline escalation** | Deadlines trigger escalation actions / notifications; not legal “appeal” (§4) |
| **Composite / multi-party review** | Subtasks; sequential/parallel routing (§3.2–§3.4) |

“Override” of an automated recommendation is **not named**; it is expressible if the human `complete`/`fail` output differs from input—application semantics, not a mandated override record type.

### Reasons

- Optional **comments**; optional **attachments**; structured **output/fault** payloads.
- No required free-text legal rationale field.

### Appeal or reconsideration

- **Not** a first-class appeal/reconsideration construct.
- Closest mechanisms: new tasks/subtasks, reassignment, fail then re-create, composite review chains—**application patterns**, not specified appeal records.

### Correction and remediation

- Comments/attachments can be modified/deleted per API rules; output/fault can be set/deleted before completion under state constraints.
- No mandated post-completion correction history or remediation case object.

### Binding of human action to a specific decision episode

- Strong binding to a **task instance** via task **identifier** (`xsd:anyURI`), state, actual owner, input/output, and `getTaskHistory` events (§3.8; §4.11; §7.1).
- Binding that task instance to a **legally relevant AI decision episode**, governing policy, and model version is **outside** the specification (task parent / application responsibility).

### Preservation of policy, evidence, and system state at that time

| Element | Spec position |
|---|---|
| Task input/output/fault at completion | Instance operational data (accessible via API while retained by processor) |
| Attachments/comments | Optional; deletable |
| Policy / rule version | Not defined |
| Model / system version | Not defined |
| Durable retention / WORM / integrity | Not defined |
| History | `getTaskHistory` returns events (filter by status, principal, event type; optional includeData)—implies history is maintained for retrieval, **not** a retention-period or archival duty |

---

## 3. Checklist interpretation

| Distinction | Application to WS-HumanTask 1.1 |
|---|---|
| **Procedural duty** | Humans claim/start/complete/fail/etc. under role/state rules |
| **Recordkeeping duty** | Instance data + history **API** for processors/clients; **no** mandated retention schedule or legal archive |
| **Human-task identity** | Task ID + lifecycle |
| **Legal decision identity** | Not defined |
| **Escalation** | Deadline/notification escalation ≠ appeal/contestation record |

### Unit-level comparison (not aggregate scoring)

| Dimension | NISTIR 8312 | EU AI Act (decision/audit-records review) | WS-HumanTask 1.1 (this review) |
|---|---|---|---|
| Focus | Explanation quality principles | Mandatory high-risk event logs + oversight *capabilities* + biometric minimum fields | Interoperable **human-task instance, API, and history** |
| Human identity in records | Audience of explanations | Verifiers (biometric subclass); oversight assignment | Actual owner, roles, CreatedBy, operation principal |
| Approval/override records | Not structured | Override *capability* (Art. 14); override logging not generally required | `complete` / `fail` / `skip` / forward / delegate as first-class transitions |
| Retention | Not required | ≥6 months logs; 10-year system docs | No retention period; history retrieval only |
| Decision-time policy/model binding | Not required | Not required in general logs | Not required |
| Explanation rights | Meaningful/accurate explanations | Art. 86 explanation right | Out of scope (task UI/rendering only) |

---

## 4. Scored criteria

Scale: 0 = Not addressed; 1 = Mentioned or partially supported; 2 = Substantially supported; 3 = Explicitly and systematically supported.  
N/A = outside the legitimate purpose of a human-task middleware specification.

Scores are independent of other SUT reviews. Requiring a human action without a preservable instance field does not earn recordkeeping credit.

### System state — **Score: 1**

| Field | Content |
|---|---|
| **Evidence** | Task context includes state, priority, role values, timestamps (§3.8.2). Processor MAY extend context (e.g., intermediate save). |
| **Justification** | Partial support for **task-instance state**, not AI/system operational state at decision time. |
| **Why not higher** | No reconstructable snapshot of model/system/policy state bound to an AI decision. |
| **Confidence** | High |

### Decision process — **Score: 3**

| Field | Content |
|---|---|
| **Evidence** | Normative state transitions and operations: claim, start, stop, complete, fail, skip, forward, delegate, nominate, suspend/resume; composite tasks and routing patterns; deadlines/escalation; `getTaskHistory` (§4.10–§4.11; §7.1). |
| **Justification** | Explicit and systematic support for **human review/approval-class workflow processes** and their observable transitions. |
| **Why not higher** | Already maximum; still process-of-human-task, not full legal decision procedure. |
| **Confidence** | High |

### Evidence — **Score: 2**

| Field | Content |
|---|---|
| **Evidence** | Operational data MUST expose input and output/fault; attachments and comments are specified with actor/time metadata but usage is optional (`MAY`) (§3.8.3). |
| **Justification** | Substantial support for carrying **review inputs/outputs and optional supporting materials** on the task instance. |
| **Why not higher** | Attachments/comments not mandatory; no IC-11 reliance subset; no excluded-evidence construct; content semantics are application-defined. |
| **Confidence** | High |

### Rules — **Score: 1**

| Field | Content |
|---|---|
| **Evidence** | Operation authorization by role and state; `illegalAccessFault`; people assignment rules; deadline constraints (§3.1; §7.1). |
| **Justification** | Partial: **task-authorization rules** for who may perform which operation. |
| **Why not higher** | Not governing policy identity/version or applicable legal/business rule paths for the underlying decision (IC-06–IC-08). |
| **Confidence** | High |

### Human context — **Score: 3**

| Field | Content |
|---|---|
| **Evidence** | Systematic generic human roles; actual owner; stakeholders/business administrators mandatory non-empty at runtime; CreatedBy/LastModifiedBy; attachment/comment authorship (§3.1; §3.8; §7.1). |
| **Justification** | Explicit and systematic support for **who is responsible/acting in the human workflow**. |
| **Why not higher** | Maximum for human-task context; still not external legal authority artifacts. |
| **Confidence** | High |

### Temporal continuity — **Score: 2**

| Field | Content |
|---|---|
| **Evidence** | Created/activation/expiration/start-by/complete-by timestamps; deadline escalation; history events via `getTaskHistory`; LastModifiedTime/By (§3.8.2; §4; §7.1). |
| **Justification** | Substantial support for **ordering and timing of human-task actions** while the processor retains the instance/history. |
| **Why not higher** | No mandated durable retention, immutability, or binding of policy/model versions to task time (IC-07/IC-13/IC-19 as decision temporality). |
| **Confidence** | High |

### Checklist marks (WS-HumanTask 1.1 only)

Exactly one mark per item.

| ID | Mark | Notes |
|---|---|---|
| IC-01 | PASS | Task identifier (`xsd:anyURI`) for the human-task episode |
| IC-02 | PARTIAL | Output/fault/outcome fields; business decision semantics in application payload |
| IC-03 | PASS | Created/activation/completion-oriented timestamps |
| IC-04 | PASS | Generic human roles + actual owner + CreatedBy |
| IC-05 | PARTIAL | Role-based task authority; not external legal authority object |
| IC-06 | FAIL | No governing policy artifact |
| IC-07 | FAIL | No policy version binding |
| IC-08 | FAIL | No applicable rule-path record |
| IC-09 | PARTIAL | Deadlines / skipability / escalation constraints |
| IC-10 | PARTIAL | Task input (+ optional attachments) |
| IC-11 | FAIL | No relied-upon distinction |
| IC-12 | FAIL | Not defined |
| IC-13 | N/A | Outside human-task middleware purpose |
| IC-14 | N/A | Outside purpose |
| IC-15 | N/A | Outside purpose |
| IC-16 | N/A | Outside purpose |
| IC-17 | FAIL | Not defined |
| IC-18 | PARTIAL | Priority, skipable, deferred activation—not decision assumptions |
| IC-19 | PARTIAL | Deadlines/expiration; not bi-temporal policy/evidence as-of |
| IC-20 | N/A | Outside purpose |
| IC-21 | FAIL | No integrity/tamper-evidence requirement |
| IC-22 | N/A | Outside purpose as reviewed |
| IC-23 | PARTIAL | ParentTaskId / subtasks / history events—not evidence provenance graph |
| IC-24 | FAIL | Not a data/model lineage model |

---

## Base-triad assessment

| Target | Present | Partial | Missing | Result |
|---|---|---|---|---|
| **Authorization** | Who may/did perform task operations | Role/state authorization | Governing policy id/version; legal mandate objects | **FAIL** |
| **Justification** | Input/output/fault; optional comments/attachments | Application-defined rationale in payloads | Relied-upon evidence package; normative criteria binding | **FAIL** |
| **Validity** | Deadline/escalation constraints on the *task* | — | Then-applicable rules/constraints for the *decision* | **FAIL** |
| **Faithful reconstruction (base)** | Strong human-gate process records | — | Triad incomplete | **FAIL** |

WS-HumanTask can **substantially record a human review gate**; it does **not**, alone, reconstruct why an AI-supported outcome was justified, authorized, and valid under then-applicable criteria.

---

## Claim relevance

This review supplies unit-level evidence relevant to **C2** (human-gate authorization/process records are separable from justification/validity structure), **C6** (human approval trails are richer than policy-engine allow/deny logs yet still insufficient for full triad reconstruction), and **C1** (structured workflow artifacts without normative bindings remain insufficient). The claims were not updated, and no aggregate conclusion was derived.

Relative to **C7** / NISTIR 8312: WS-HumanTask is not an explainability method; unit comparison shows it addresses **workflow records**, whereas NISTIR 8312 addresses **explanation properties**—orthogonal fragments.

Relative to the **EU AI Act decision/audit-records review**: the Act mandates **retention-backed operational logs** and oversight *capabilities* (with biometric minimum fields); WS-HumanTask specifies a **richer human-task record/API model** but **no** legal retention floor. Neither closes the base triad alone.

---

## 5. Evaluation boundary

- Only WS-HumanTask 1.1 CS-01 concepts receive credit.
- BPEL4People, BPMN, and engine histories receive **no** credit.
- Application payloads that *could* store policy hashes earn **no** credit unless required by the specification.
- `MAY` attachments/comments do not upgrade IC-10/IC-11 to PASS.
- EU AI Act and NISTIR 8312 are comparison references only; this file does not modify those reviews.

---

## 6. Threats to validity

- HTML/PDF extracts omit some schema listings; normative prose and API tables were relied upon for scoring.
- Conformance targets vary (what a Processor MUST implement); optional advanced query must not inflate scores.
- Equating task completion with legal “approval” over-reads application semantics.
- History API availability during the task lifetime can be mistaken for archival preservation.

---

## 7. Remaining uncertainty

- Whether particular conforming processors retain history after task purge is implementation-defined.
- Composition of WS-HumanTask + policy decision logs + AI Act logs is out of scope.
- Claims are not updated.

---

## Limitations

- Middleware/workflow standard, not a legal recordkeeping regime.
- Requirements are **technical conformance** obligations, not statutory retention mandates.
- Domain-agnostic: no AI-specific evidence/policy/model fields.
- Defines **records structures and retrieval APIs** without sufficient bindings to authorization policy versions or model versions.
- Assumes an external task parent/application to interpret payloads as consequential decisions.
- Omits appeal/reconsideration as first-class objects; omits integrity, durable retention, and legal jurisdiction frames.

---

## 8. Overall assessment / Principal finding

**OASIS WS-HumanTask 1.1 systematically specifies human-task identity, roles, timing, lifecycle operations (including complete/fail/skip/forward/delegate), optional comments/attachments, deadline escalation, and retrievable task history.** That is a concrete **human review workflow record model**, stronger on human-gate process/identity than NISTIR 8312 (explanations) and more structured for human actions than the AI Act’s general event-log duty (while weaker on mandated retention).

**Principal finding:** WS-HumanTask supports **decision-linked human-workflow records** (task episode, actors, transitions, I/O) but remains **generic workflow auditability** relative to faithful reconstruction: without policy/model/evidence-reliance bindings and preservation duties, the **base triad fails**.

**Not updated:** comparison matrix; reconstruction evaluation dataset; aggregate claims; coverage audit; synthesis documents.  
**Not modified:** `2026-07-29-eu-ai-act-decision-audit-records.md`; BibTeX `eu2024aiAct`.
