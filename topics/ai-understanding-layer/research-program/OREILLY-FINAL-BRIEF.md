---
id: note-research-program-oreilly-final-brief
title: "O'Reilly Final Brief"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [research-program, oreilly, final-brief, drafting-brief]
refs: [OREILLY-SYNTHESIS-MAP.md, PUBLICATION-ARCHITECTURE-FINAL.md, contribution-03/FINAL-EDITORIAL-DISPOSITION.md]
---

Authoritative drafting brief, produced by an adversarial re-review of
`OREILLY-SYNTHESIS-MAP.md` — not a re-trust of its recommendation.
Supersedes `OREILLY-SYNTHESIS-MAP.md` §5's ranking and §11's format
recommendation for drafting purposes; that document's layer map (§1),
prior-art audit (§7–8), and umbrella-term test remain valid inputs and
are drawn on directly below.

## Editorial verdict

**GO WITH CONDITIONS.** See §26 below for the exact conditions. No
research gap blocks drafting — every condition is a drafting-discipline
requirement, not a missing-evidence requirement.

## Final thesis

> A production AI decision must be authorized before it happens and
> explainable after it happens — and neither is possible without
> preserving the right relations, not just the right artifacts, around
> the decision itself, not just the model that produced it.

## Thesis in one sentence

> The decision — not the model — is what must be authorized and later
> explained, and those are two separate properties, each requiring its
> own preserved relations.

## Central surprise

> Most engineers assume that if a decision was properly evaluated and
> approved, and every version of the system was retained, the decision
> is both justified and explainable. That assumption fails because
> approval (an evidence-gated authorization) and explainability (a
> unique reconstruction of what was actually consumed) are two separate
> engineering properties — a system can have one without the other, and
> most systems today are architected to produce only the first.
> Contribution 1 shows production-consequential model outputs need an
> explicit, evidence-gated decision boundary before they become
> authorized actions. Contribution 2 shows a fully evidenced, fully
> gated decision can still become unreconstructable later — retaining
> every version is not the same as recording which version a decision
> actually consumed. Contribution 3 adds that this same gap recurs one
> level up, across a sequence of decisions, and that a trustworthy
> reconstruction mechanism must say "ambiguous" rather than invent a
> confident, wrong account. Therefore: production AI systems need two
> distinct, separately-engineered properties around every consequential
> decision — an enforced boundary that authorizes it, and a preserved
> relation that can later, honestly, explain it.

## Intellectual synthesis

- **What C1 contributes:** the decision boundary and the evidence-gated
  authorization mechanism (evidence / requirements / authority / gate);
  the "one model, many decisions" inversion establishing the decision,
  not the model, as the operational unit.
- **What C2 contributes:** the empirical demonstration that retained
  version history does not, by itself, identify what a specific decision
  consumed — "retained ≠ consumed" — and the honest-ambiguity-vs-false-
  historical-confidence distinction.
- **What C3 contributes, sparingly:** the same relation-preservation gap
  recurs across a sequence of decisions, and the honest-ambiguity
  principle holds one level up, closable with ordinary, already-existing
  mechanisms (no new architecture).
- **What becomes visible only when combined:** that authorization (C1)
  and reconstruction (C2/C3) are *independent* properties of the same
  decision boundary — a system can pass one and fail the other, and nothing
  about passing C1 predicts success at C2. This is not visible from
  either contribution alone; it required the adversarial confirmation
  (`recommended-program.md`'s self-review) that control does not
  logically entail reconstruction, plus both contributions' concrete
  mechanisms to make the independence *actionable* rather than merely
  logical.

## Claim ladder

| # | Claim | Source | Evidence level | Prior art | Safe wording | Forbidden wording |
|---|---|---|---|---|---|---|
| C1 | A model output is not equivalent to an authorized production decision | Article 1 premise | Architecture argument, audited (Position B) | Access control's request/decision distinction | "a model output is not, by itself, a decision" | Implying this is a new observation about ML systems generally |
| C2 | An explicit, evidence-gated decision boundary (evidence/requirements/authority/gate) is needed before consequential action | Article 1 | Architecture argument, self-reviewed | XACML/Cedar, Kubernetes admission control, in-toto/SLSA, CI/CD gates | "a synthesis of existing enforcement patterns applied to the model-vs-decision boundary" | "we invented policy enforcement"; claiming runtime/agent-latency feasibility as proven |
| C3 | Retained version history does not guarantee identification of which version a decision consumed | Article 2 | EMPIRICAL, frozen, ACCEPTED | Bitemporal databases, W3C PROV, event sourcing | "the system must preserve the consumption relation, not just version history" | "bitemporal databases cannot solve reconstruction"; "explicit custom bindings are uniquely necessary" |
| C4 | A trustworthy reconstruction mechanism must report ambiguity honestly rather than invent a confident wrong answer | Article 2 (FHC) + research note (FGC) | EMPIRICAL, both experiment suites | Diagnosability theory's AMBIGUOUS-as-legitimate-verdict framing (adjacent, credit narrowly) | "a reconstruction system should be able to say 'ambiguous'" | Implying any production system currently does this well; that this solves reconstruction generally |
| C5 | The same relation-preservation gap recurs across a sequence of decisions, closable with ordinary mechanisms | Research note | EMPIRICAL, but structurally close to guaranteed by design (disclosed) | Workflow provenance, distributed tracing, event sourcing, compositional verification | "the same principle holds across a workflow of decisions, using mechanisms that already exist" | Any "new trajectory layer" claim; presenting this as a surprising discovery |
| C6 | The decision is the correct unit around which both authorization and reconstruction must be engineered | Cross-cutting synthesis of C1 + C2's decision-scoped reconstruction object + C3's trajectory-as-composed-decisions | SYNTHESIS (components independently earned) | Dynamic/continuous assurance cases (closest existing combined framework — S33–S36) | "a disciplined synthesis and practitioner translation, not a new mechanism" | "new architecture"; "Understanding Layer"; "capability vs. understanding"; any implication of formal proof |

Every article-spine section (§"Article spine" below) maps to at least
one row above.

## Prior-art positioning

**Strongest collision:** dynamic/continuous assurance cases already
combine a prospective authorization-type claim with retrospective,
in-operation evidence into one coordinated framework, including
applications specifically to AI systems (`assurance-integration-
review.md`, sources S33–S36). This is the closest existing field to the
combined thesis (C6) — closer than treating C1's and C2's prior art
separately.

**Novelty classification:** **NEW SYNTHESIS + PRACTITIONER TRANSLATION.**
The individual mechanisms (evidence-gating, consumption relations,
honest ambiguity) are each independently earned and audited within
their own contribution; the combined "decision as the dual unit of
authorization and reconstruction" framing is a synthesis across them,
translated into ML/MLOps-native vocabulary rather than assurance-
engineering vocabulary. **Not** NOTHING DISTINCTIVE — the translation and
the two independently-tested mechanisms behind each half are real,
disclosed contributions — but the high-level duality itself must credit
assurance-case literature directly, not be presented as if no field had
combined these before.

**Exact safe positioning:** "A synthesis and practitioner translation
connecting established enforcement patterns (access control, admission
control, supply-chain attestation), established preservation/provenance
patterns (bitemporal databases, W3C PROV, event sourcing, distributed
tracing), and assurance-case thinking (dynamic/continuous safety cases),
organized around the AI-mediated decision as the operational unit —
validated by two independently-run, disclosed, controlled experiments
and one supporting research note."

## AI-specificity

Removing "AI" from the final thesis leaves it true — expected, not
disqualifying (`OREILLY-SYNTHESIS-MAP.md` §12 already anticipated this).
Legitimate AI-specific reasons for the article, each evidenced by this
programme's own research (no prevalence claims):

- ML/MLOps governance culture organizes artifacts around **models**
  (registries, model cards, evaluation reports) rather than decisions —
  confirmed by this programme's own model-registry prior-art survey
  (`contribution-boundaries.md` Q6: these tools govern "versions and
  approval states," not a model-agnostic decision boundary).
- Generative/agentic systems multiply the number of runtime decision
  boundaries relative to traditional software — a structural,
  architectural observation.
- The context an AI-mediated decision consumes (model version, prompt,
  retrieval corpus state, tool state, policy version, human approval) is
  unusually heterogeneous, making "what did this decision actually
  consume" both harder to answer and easier to get silently wrong.
- Model outputs can propagate directly into consequential actions with
  less human mediation than historically typical — Article 1's own
  motivating premise.

State explicitly in the article that the underlying principles (control
≠ reconstruction; artifacts ≠ relations) are general systems-engineering
truths older than AI — this strengthens credibility rather than
weakening it.

## Umbrella terminology

**No single existing umbrella term cleanly spans both halves of the
earned research without either overclaiming or underclaiming one half**
(full comparison: `OREILLY-SYNTHESIS-MAP.md` §6, re-tested here against
ACCOUNTABILITY, TRACEABILITY, RECONSTRUCTABILITY, DECISION PROVENANCE,
and DECISION ASSURANCE in addition to AUDITABILITY — DECISION ASSURANCE
is the closest fit by prior-art alignment but has low ML/MLOps
practitioner familiarity, its main weakness). **Decision: do not force
one.** Use the explicit two-part framing "authorized now / explainable
later" as the operative structure. "Auditability" may appear only in its
ordinary, plain-English sense as a reader on-ramp (e.g., in the opening
paragraph), never redefined as this article's technical term — this
avoids both the compliance-guarantee misreading and the "relational
database" collision risk identified in this review's attack on
"Auditability is relational" (§ below).

### "Auditability is relational" — verdict

**DEMOTED to supporting subthesis, not the headline.** The insight
(auditability comes from preserving relations, not from artifact volume)
is real and earned — it survives as claim C3–C5's mechanism. As the
*headline thesis*, it fails three tests: (1) it flattens the earned
control/reconstruction duality into one word, losing the hard-won
"siblings, not sequence" finding; (2) "relational" risks a distracting
misreading as relational-database vocabulary for this exact audience;
(3) it is a slogan requiring unpacking, not a self-explanatory claim —
an engineer cannot tell what to build differently from the sentence
alone. Retained as the mechanism/HOW inside the combined thesis, not as
the printed one-liner.

### "The decision is the unit of auditability" — verdict

**PROMISING BUT NEEDS QUALIFICATION.** Directly earned by Article 1's
already-audited "model is not the unit" inversion (Position B), and
consistent with C2's decision-scoped reconstruction object and C3's
trajectory-as-composed-decisions. Weakness: bare "not the model" invites
an easy, correct rebuttal — models genuinely are audited in practice
(model cards, evaluation reports, interpretability research). **Must
always carry a qualifier** ("not only the model," "the primary
operational unit") — never printed bare. Used in the final thesis and
spine with this qualifier applied throughout.

## Scope

**In scope:** the decision boundary; evidence-gated authorization;
consumption relations; honest ambiguity vs. false confidence; the
trajectory-composition extension (one section only); the "decision, not
only the model, is the unit" framing; concrete design guidance.

**Out of scope:** complete AI governance; EU AI Act or any specific
regulatory implementation; compliance guarantees; general AI safety;
model interpretability; broad explainability (XAI); human understanding;
capability scaling; new provenance mechanisms; new policy engines; full
trajectory theory or case-by-case experimental detail; broad agent
architecture; new assurance-case formalism (credit the field, do not
propose an extension to it).

## Running example

**An AI agent authorized to call tools that modify production state**
(e.g., issuing a refund, modifying a database record, sending a customer
communication) — chosen over model-promotion (too infra-narrow),
credit/risk recommendation (unwanted regulatory heat), and content
moderation (unwanted political/regulatory heat) for technical clarity
and lowest distraction. One example carries the whole spine: the model
proposes a tool call → evidence/policy/authority determine whether the
gate allows it (Section 3 of the spine) → months later, an investigator
must determine which policy version, which retrieved context, and which
prior tool-call output this specific call actually consumed (Section 4)
→ if two candidate prior outputs are indistinguishable from the record,
the honest answer is "ambiguous," not a guess (Section 5). Illustrative
only — no empirical claim is made about this specific scenario; do not
present it as tested data.

## Contribution 3 role

**A — one short section** (~350–450 words), per the spine's Section 5.
Bounded explicitly: no case-matrix detail, no case IDs, no metric
tables, no T1/T2 regime terminology. State only the honest-ambiguity
principle and its one-level-up recurrence, both already disclosed in
`contribution-03/FINAL-EDITORIAL-DISPOSITION.md`'s "Findings retained
for synthesis" (Findings B, C, D — cite that document's classification
directly if useful, do not re-derive it in the article).

## Article spine

6–8 sections; each maps to at least one claim-ladder row. This is a
synthesis spine, not Article-1-summary / Article-2-summary /
Article-3-summary concatenation.

1. **The Gap Between Approved and Explainable** — Purpose: state the
   central surprise; introduce the running example. Claim: C1+C2
   combined (approval ≠ explainability). Evidence: running example,
   approved-then-later-unreconstructable. Budget: ~500–600 words. NOT:
   architecture mechanics yet.
2. **The Decision Is the Unit — Not Only the Model** — Purpose:
   establish the operational unit, with the required qualifier. Claim:
   C1's inversion, extended by C2/C3's decision-scoped object. Evidence:
   the inversion argument + reconstruction object definition. Budget:
   ~400–500 words. NOT: dismissing model-level audit practice.
3. **Authorizing a Decision** — Purpose: explain the control half via
   the running example. Claim: C1/C2 (evidence/requirements/authority/
   gate). Evidence: the tool-call gate walkthrough. Budget: ~600–700
   words. NOT: reconstruction; deep HITL treatment.
4. **Explaining a Decision, Later** — Purpose: explain the reconstruction
   half via the same example. Claim: C3 (retained ≠ consumed). Evidence:
   the tool-call revisited months later. Budget: ~700–800 words. NOT:
   bitemporal database internals; full case-matrix detail.
5. **When the Record Can't Decide** — Purpose: honest ambiguity, one
   level up. Claim: C4/C5. Evidence: one sentence on the trajectory
   extension. Budget: ~350–450 words. NOT: T1/T2 design, case numbering.
6. **This Isn't a New Mechanism** — Purpose: prior-art positioning.
   Claim: C6's honest attribution. Evidence: named fields (access
   control, admission control, supply-chain attestation, W3C PROV, event
   sourcing, dynamic assurance cases). Budget: ~400–500 words. NOT:
   exhaustive literature review, academic citation format.
7. **What to Actually Build** — Purpose: concrete design change.
   Claim: synthesis takeaway. Evidence: a checklist derived from the
   running example. Budget: ~400–500 words. NOT: prescribing one schema
   or reference implementation.
8. **What This Doesn't Claim** — Purpose: explicit boundaries, closing.
   Claim: scope list above. Evidence: n/a. Budget: ~300–400 words. NOT:
   reopening any retired concept even to explain its exclusion at
   length.

Target total: ~3,650–4,450 words, inside the recommended length band.

## Title ranking

Full candidate set (12), tagged by category — Provocative (P), Technical
(T), O'Reilly practitioner (OR), Conservative (C); decision-as-unit (DU),
artifact-vs-relation (AR), and control-vs-reconstruction (CR) axes each
covered by 3+ candidates:

1. [P] "Approved Doesn't Mean Explainable"
2. [P] "Your AI Decision Passed Review. Can You Still Prove Why?"
3. [P, AR] "The Record That Approved It Isn't the Record That Explains It"
4. [T, CR] "Decision-Level Authorization and Decision-Level Reconstruction: Two Separate Guarantees"
5. [T, DU] "The Decision, Not Only the Model, Is the Unit of Production AI Auditability"
6. [T, AR] "Authorization Relations and Consumption Relations: What Production AI Systems Must Preserve"
7. [OR, DU] "Model Outputs Aren't Decisions — And Decisions Aren't Self-Explaining"
8. [OR, AR] "What Your AI Audit Trail Is Missing: The Relations, Not the Records"
9. [OR, CR] "Building AI Systems That Can Be Authorized Now and Explained Later"
10. [C, CR] "Two Properties Every Production AI Decision Needs: Authorization and Reconstruction"
11. [C] "Why Retaining Every Version Still Isn't Enough to Audit a Decision"
12. [C, DU] "The Decision Is the Unit — Not the Model"

**Top 5, ranked:**

1. **#8 — "What Your AI Audit Trail Is Missing: The Relations, Not the
   Records"** — practitioner-familiar hook, avoids the "auditability"
   redefinition risk entirely by naming a concrete artifact.
2. **#9 — "Building AI Systems That Can Be Authorized Now and Explained
   Later"** — directly encodes the control/reconstruct duality in active
   voice.
3. **#3 — "The Record That Approved It Isn't the Record That Explains
   It"** — vivid, concrete, captures the "two records" illustrative
   device.
4. **#5 — "The Decision, Not Only the Model, Is the Unit of Production
   AI Auditability"** — strongest technical framing, carries the
   required qualifier already in the title.
5. **#1 — "Approved Doesn't Mean Explainable"** — punchy; strongest as a
   pull-quote/subtitle pairing with #8 or #9 as the main title.

## Final thesis ranking

13 candidates scored 1–5 on technical defensibility (TD), surprise (S),
practitioner usefulness (PU), synthesis quality (SQ), prior-art
resilience (PAR), AI relevance (AIR), title potential (TP).

| Thesis | TD | S | PU | SQ | PAR | AIR | TP | Total/35 |
|---|---|---|---|---|---|---|---|---|
| **Combined thesis (selected)** | 5 | 5 | 5 | 5 | 4 | 4 | 5 | **33** |
| Fully authorized yet unexplainable (runner-up) | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 29 |
| Two records: authorized vs. explained | 4 | 4 | 5 | 4 | 3 | 4 | 5 | 29 |
| Audit trail ≠ proof of reconstruction | 4 | 4 | 5 | 3 | 4 | 4 | 5 | 29 |
| Control now, reconstruct later | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 27 |
| Same artifacts, different provability | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 26 |
| Decision is the unit of auditability (unqualified) | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 26 |
| Storing more ≠ explaining more | 3 | 4 | 4 | 2 | 3 | 4 | 4 | 24 |
| Passing evaluation ≠ authorization | 4 | 3 | 4 | 1 | 4 | 3 | 3 | 22 |
| Auditability is relational (best rejected) | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 21 |
| Evidence without relations is not enough | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 20 |
| Decisions need boundaries and histories | 3 | 2 | 3 | 2 | 3 | 3 | 2 | 18 |
| From output to accountable action | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 17 |

**Selected: the combined thesis** (§"Final thesis" above), 33/35 —
highest score on every dimension except prior-art resilience and AI
relevance, where it ties the top alternatives.

**Runner-up: "A decision can be fully authorized and still become
unexplainable"** (29/35) — the single sentence with the highest surprise
score; recommended as the article's opening hook sentence even though
the combined thesis is the printed headline.

**Best rejected: "Auditability is relational"** (21/35) — the insight is
real and earned, but as a standalone headline it flattens the earned
control/reconstruction duality into one word, risks a relational-
database misreading for this audience, and is a slogan requiring
unpacking rather than a self-explanatory claim. Demoted to a supporting
subthesis (the mechanism/HOW inside the combined thesis), not discarded
entirely.

## Original proposal → validated synthesis

**ORIGINAL:** "Model outputs are routinely treated as decisions without
enforceable validation, structured evidence, or accountability... every
decision is validated, traceable, and enforceable before it is allowed
into production." (Source B marketing description.)

**RESEARCH-VALIDATED:** "A model output is not a decision, and an
explicit, evidence-gated boundary is a defensible, if unoriginal,
synthesis for closing that gap — but passing that gate does not, by
itself, make the decision explainable later. Retaining every version of
a system's dependencies does not guarantee anyone can determine which
version a specific decision consumed, and a trustworthy reconstruction
mechanism must say 'ambiguous' rather than guess. Authorization and
reconstruction are two separate properties production AI systems must
be engineered for, not one property that follows automatically from the
other."

## Source A → surviving intuition

Original direction: capability is outpacing "understanding," and a
missing architectural "Understanding Layer" is the fix. **Both the
scaling comparison and the dedicated architectural layer are retired —
neither was earned by any experiment in this programme**
(`contribution-03/FINAL-EDITORIAL-DISPOSITION.md`, Findings F/G).

**Surviving intuition, narrowly:** Source A's core observation that
"the current state of a system rarely explains how that state was
reached, and AI systems increasingly violate the traditional assumption
that this can be reconstructed from other artifacts" survives, precisely
and only, as Article 2's empirically-earned "retained ≠ consumed"
finding — not as a general claim about AI capability or system
understanding. No terminology from Source A ("Understanding Layer,"
"missing layer," "capability vs. understanding") is used anywhere in
this brief or should appear in the drafted article.

## Claims allowed

- A model output is not equivalent to a decision (C1).
- An explicit evidence-gated boundary is a defensible synthesis of
  existing enforcement patterns (C2).
- Retained version history does not guarantee consumption identification
  (C3).
- A reconstruction mechanism should report honest ambiguity (C4).
- The same relation-preservation principle holds across a decision
  trajectory, closable with existing mechanisms (C5).
- The decision, not only the model, is the correct unit for both
  authorization and reconstruction (C6, qualified).
- This is a synthesis and practitioner translation of established
  fields, organized around the AI-mediated decision.

## Claims forbidden

- Any claim of a newly invented mechanism, architecture, or layer.
- "Understanding Layer" or "capability vs. understanding," in any
  wording.
- "We invented provenance" / "we invented policy enforcement."
- A compliance or regulatory guarantee.
- Any prevalence claim about how often this gap occurs in production.
- "Bitemporal databases cannot solve reconstruction."
- "Explicit custom bindings are uniquely necessary."
- "Not the model" without the "not only" qualifier.
- Presenting the running example as tested empirical data.

## Evidence/citation requirements

- Every empirical number used (if any are quoted directly) must trace to
  `contribution-02/experiment/results/` or
  `contribution-03/experiment/results/` exactly as recorded, not
  paraphrased or rounded beyond what those files support.
- Prior-art citations must reuse the already-verified entries from
  Article 2's reference list (W3C PROV, OpenTelemetry, Fowler) and the
  research note's verified entries (Sampath et al. 1995; Bakirtzis &
  Topcu 2022) where relevant; the dynamic-assurance-case citations
  (S33–S36 in `contribution-03/source-ledger.md`) must be added fresh
  for §6 of the spine, verified before use per this programme's
  established citation-hygiene discipline (independent re-fetch, not a
  search-snippet citation).
- No new source may be cited without the same verification discipline
  used throughout this programme (primary source located and confirmed,
  not a summary taken on faith).

## Recommended article length

**Tier B — one 3,500–5,000 word deep O'Reilly article.** Rejected tier A
(2,500–3,500 words): too tight to synthesize C1+C2+C3 without reverting
to concatenated summary, the exact failure mode this review was
instructed to guard against. Rejected tiers C/D (multi-part series):
the synthesis payload (one running example, one combined thesis) does
not require serialization, and a single article better matches the
"article first, book later" strategy's intent to demonstrate the
complete synthesis at once. If drafting naturally lands under 3,000
words without cutting required content, fall back to tier A framing
rather than padding.

## Drafting instructions

1. Open with the running example and the central surprise — do not open
   with definitions or a literature survey.
2. Use the qualified "decision, not only the model" framing every time
   the unit claim appears.
3. Keep Contribution 3 to Section 5 of the spine, ≤450 words, no
   experiment-internal vocabulary (T1/T2, case IDs).
4. Credit dynamic/continuous assurance cases explicitly in Section 6 —
   this is the single most important prior-art addition this review
   identified relative to `OREILLY-SYNTHESIS-MAP.md`'s original prior-art
   treatment.
5. Do not force an umbrella noun; use "authorized now / explainable
   later" as the operative two-part structure throughout.
6. Close with the explicit boundaries section (spine §8) — do not let
   the article's own final paragraph gesture toward a bigger claim than
   §"Scope" above allows.
7. Verify, before finalizing any draft, that "Understanding Layer" and
   "capability vs. understanding" do not appear anywhere, including in
   material quoted from Source A for illustrative contrast.

## GO / NO-GO

**GO WITH CONDITIONS.**

1. The printed one-sentence thesis must be the combined form above, not
   the bare "Auditability is relational" slogan.
2. Every "decision is the unit" claim must carry the "not only the
   model" qualifier — never printed bare.
3. Contribution 3 material capped at one spine section, ~350–450 words,
   no experiment-internal vocabulary.
4. Dynamic/continuous assurance-case literature (S33–S36) must be cited
   explicitly in the prior-art section — identified by this review as a
   real gap in the prior synthesis-map treatment.
5. No umbrella noun forced; use the explicit two-part framing throughout.
6. Target 3,500–5,000 words; fall back to a tighter framing rather than
   padding if the material runs shorter.

No condition above reflects a missing-evidence gap — every condition is
a drafting-discipline instruction derived from this review's adversarial
testing of the thesis candidates. **Ready to draft**, subject to the six
conditions.
