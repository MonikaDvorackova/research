---
id: pub-02-jurix2026-terminology-review
title: "Terminology review — Publication 02"
type: publication
status: draft
created: 2026-07-29
updated: 2026-07-29
tags: [jurix, terminology, publication-02]
source: planning/jurix-specification.md
---

## Terminology review

Focus terms from the specification: **Decision Knowledge** and **Knowledge Continuity**.

---

### Decision Knowledge

#### Specification definition

> Decision Knowledge is the structured set of information required to explain, justify, review or contest a specific AI-assisted decision after the decision has been made.

#### Does the term already exist?

| Sense | Status |
|---|---|
| Exact phrase as AI & Law technical term | **Not established** as a standard definition in core AI & Law venues surveyed for this map |
| Near synonyms | Decision provenance records; reviewability records; audit/decision traces; evidence packages; case files; “meaningful information” about logic (GDPR debates); process-centric explanations |
| Industry usage | “Decision memory,” “decision trace,” “decision event schema” appear in recent industry/preprint governance writing—**not** settled scholarly terms |

#### Conflicts

- Risk of confusion with **legal knowledge** (norms, doctrine) or **knowledge bases** used for inference.
- Risk of confusion with **XAI explanations** (generated artefacts) vs retained decision-time information.
- Risk of overlap with **evidence** in evidentiary reasoning (AI & Law)—must say Decision Knowledge includes but is not limited to input evidence.

#### Alternatives to consider

| Alternative | Pros | Cons |
|---|---|---|
| Decision record / decision dossier | Familiar, concrete | Sounds like passive filing; weak on “knowledge” structure |
| Decision evidence package | Links to evidence theory | May under-emphasise policy, rationale, review context |
| Reviewability record set | Aligns with Cobbe | Cedes novelty; may look derivative |
| Decision provenance graph | Aligns with Singh / PROV | Provenance-centric; may miss legal criteria/rationale |
| **Keep Decision Knowledge** | Matches spec; signals KR framing | Needs careful definition and disambiguation |

#### Recommendation

**Retain “Decision Knowledge”** as in the specification, with:

1. early formal definition (§4);
2. explicit “not merely model explanation text”;
3. working component inventory labelled non-exhaustive;
4. contrast sentence vs provenance/logs/XAI outputs.

#### Reviewer risks

Terminology inflation; “just a new name for audit logs.”

---

### Knowledge Continuity

#### Specification definition

> Knowledge Continuity is the ability of an AI system to preserve the decision knowledge necessary for future explanation, accountability, contestation and legal review across time, system changes and institutional contexts.

#### Does the term already exist?

| Sense | Status |
|---|---|
| Knowledge management / organisational memory | **Yes** — “knowledge continuity” and continuity of organisational knowledge appear in KM and enterprise-memory discourse |
| Formal AI & Law system property | **No established standard** matching this definition |
| Related technical framings | Reviewability over time; institutional memory; persistent cognitive threads (non-legal continuity frameworks); agent memory durability |

#### Conflicts

- KM readers may expect HR/succession “knowledge continuity,” not AI decision retention.
- “Continuity” may be read as service continuity / business continuity.
- Overlap with **persistence**, **durability**, **traceability**, **reviewability**.

#### Alternatives to consider

| Alternative | Pros | Cons |
|---|---|---|
| Decision-knowledge persistence | Clear engineering | Less elegant; drops “system property” rhetoric |
| Reviewability (adopt Cobbe term) | Strong prior | Loses distinct thesis brand; looks subsumed |
| Traceability / auditability | Familiar in governance | Too broad; often satisfied by weak logs |
| **Keep Knowledge Continuity** | Matches spec; emphasises temporal/system property | Disambiguate from KM and business continuity |

#### Recommendation

**Retain “Knowledge Continuity”** with mandatory disambiguation:

- “as a **system property of legally relevant AI systems** concerning **Decision Knowledge**,” not organisational KM in general.

Optional shorthand after definition: *DK-continuity*.

#### Reviewer risks

Buzzword; unmeasurable property; collision with KM literature.

---

### Other specification terms (brief)

| Term | Note |
|---|---|
| System state | Keep; contrastive workhorse for §2 |
| Decision object / evidence object / … (§5) | Treat as **conceptual vocabulary**, not ontology commitment; reduce set if page-limited |
| Epistemological problem (C1) | Use carefully—some reviewers read “epistemology” as overclaim; “representational / informational problem” may be safer *in prose* while keeping C1 label if authors insist |

---

### Literature support for conclusions

- Near-synonym landscape: Cobbe et al. reviewability; Singh decision provenance; Alfrink contestable AI; W3C PROV; Wachter et al. counterfactuals as contest-oriented explanations.
- Absence of a canonical “Decision Knowledge” definition in those works supports introducing the term **if** differentiation is explicit.
- KM “knowledge continuity” usage supports **disambiguation obligation**, not abandonment.
