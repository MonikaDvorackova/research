---
id: note-article-01-decision-level-control-evidence
title: "Article 1 Evidence Inventory — Decision-Level Control"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-21
updated: 2026-08-21
tags: [article-planning, evidence-inventory, decision-level-control]
refs: []
---

## Article 1 Evidence Inventory (Task A)

Every claim Article 1 can currently draw on, from Source B in full and only
the decision-architecture portions of Source A (§1, the front half of §3,
the front half of §6, §7). No claim below is invented; several are flagged
as requiring softening or external validation before they can be stated as
fact in prose.

| # | Claim | Source | Explicit / inferred | Needs external verification | Needs empirical evidence | AIGov Core can illustrate | Risk of overclaiming |
|---|---|---|---|---|---|---|---|
| 1 | "Most AI systems fail in production not because of poor models, but because they lack a mechanism to control and verify decisions." | B, marketing description | Explicit (asserted, not demonstrated in-source) | Yes — causal/prevalence claim about failure rates | Yes | No — this is a general industry claim, not something AIGov Core's design demonstrates | **High.** Must not be stated as an established finding; recast as motivating framing ("the argument this article makes is...") rather than a claimed fact. |
| 2 | "Model outputs are routinely treated as decisions without enforceable validation, structured evidence, or accountability." | B, marketing description | Explicit | Yes — "routinely" is a prevalence claim | Yes | Weakly — Source A §7 gives one qualitative anecdote (context "scattered across deployment records, evaluation results, prompts...") that is consistent with this, not proof of prevalence | **Medium.** Present as an architectural pattern the article argues for, not a quantified industry statistic. |
| 3 | Model output ≠ production decision (Ch. 3 title: "From Outputs to Decisions"; "Why model outputs are not decisions") | B, Ch. 3 (chapter theme only — book not written) | Explicit as a chapter theme; the argument itself must be constructed by this article | No — definitional/architectural claim | No | No | **Low**, provided the article builds the argument itself rather than claiming the book already made it. |
| 4 | A decision requires structured, first-class evidence (Ch. 4: "Evidence as a First-Class Concept") | B, Ch. 4 | Explicit chapter theme | No — design/conceptual claim | No | No | **Low.** |
| 5 | "Why governance without enforcement does not work" | B, "What the reader will learn" | Explicit | Partially — the logical claim (unenforced ⇒ advisory) can be argued from first principles; the strength of "does not work" benefits from failure examples the source doesn't supply | No, not required to state the logical version | No | **Low–medium.** State the logical form (an unenforced requirement is advisory by definition) rather than an empirical "it doesn't work" verdict. |
| 6 | CI-style gates as the enforcement mechanism (Ch. 7: "CI Gates for AI Systems — Implementing enforcement in pipelines") | B, Ch. 7 | Explicit chapter theme | No — proposed design pattern | No | Weakly — Source A frames AIGov Core as originating from this kind of governance/enforcement problem, but gives no gate implementation detail | **Low**, as long as it is framed as a proposed pattern, not a claim that this is standard industry practice today. |
| 7 | Human-in-the-loop approval as a "controlled mechanism" (Ch. 8: "Approval and Risk Review") | B, Ch. 8 | Explicit chapter theme | No | No | No | **Low.** |
| 8 | Industry attention has gone disproportionately to model performance and explainability, leaving a gap in decision validation/approval/enforcement | B, "About the topic" | Explicit | Partially — fair, widely-observable framing claim, but stated as fact in the source without measurement | Would strengthen, not required | No | **Medium.** Present as a framing observation, not a measured finding. |
| 9 | "The modern AI stack contains mature abstractions for producing behaviour. It contains comparatively few abstractions whose primary purpose is to preserve the decision context..." | A §3 | Explicit | No | No | No | **Medium — boundary-sensitive.** Only the front half (mature production abstractions vs. immature decision-support abstractions) belongs to Article 1. The back half ("...needed to reconstruct, investigate, or challenge that behaviour later") is Article 2 territory (reconstruction over time) and must be trimmed if this sentence is excerpted. |
| 10 | "...the engineering support for preserving [a decision's] justification, supporting evidence, applicable policies, delegated authority, and decision context is often fragmented across independent systems or missing entirely." | A §6 | Explicit | No | No | No | **Medium — boundary-sensitive.** Usable for "decision support is fragmented, not structurally enforced," but this sentence sits inside Source A's "Missing Layer" section, which leads directly into AIGov Core and the terminal thesis. Use only the fragmentation diagnosis, not the "first-class engineering concern... primitives on which governance could be built" framing that follows it — that framing belongs to Article 3. |
| 11 | "Determining whether a deployment had been justified at the time it was made was often far more difficult than determining whether the decision complied with current policies. The necessary information was scattered across deployment records, evaluation results, prompts, external policy documents, approval workflows, and operational logs." | A §7 | Explicit | No | No | Yes — this is the direct AIGov Core origin anecdote | **High — dual-purpose sentence.** The "scattered across independent systems, no unified decision layer" reading supports Article 1. The "justified at the time it was made" / after-the-fact reconstruction reading is Article 2/3 territory. If quoted, excerpt only the scattering/fragmentation half. |
| 12 | AIGov Core "treats governance decisions themselves as engineering artifacts" | A §7 | Explicit | No | No | Yes — directly | **Low**, as an implementation-pattern illustration matching "evidence-gated decisions as first-class artifacts." Do not extend beyond what §7 states — no concrete API, schema, or enforcement mechanics are given in the source. |
| 13 | Source B claims the framework is "grounded in system design and supported by controlled failure experiments and an audit of real-world ML repositories, demonstrating systematic gaps in auditability and enforcement." | B, "About the topic" | Explicit **as a stated intention in a book proposal** | Yes — no results, data, or methodology are supplied anywhere in either source | Yes | No | **High.** This is a proposal-stage statement of intended future work, not completed empirical work. Must not be presented in the article as existing evidence or findings — if referenced at all, caveat explicitly that no audit/experiment results are available in the source material. |
| 14 | Market/regulatory framing: "AI adoption is rapidly increasing," "enterprise AI spending projected to grow significantly," regulatory pressure driving adoption, finance/healthcare/government emphasis | B, "Market size," marketing description | Explicit but unquantified | Yes — no figures or citations given | Yes, if used quantitatively | No | **High** if used as evidenced; safe only as light, qualitative motivating context ("as AI is deployed into settings where decisions carry real consequences...") — drop specific claims about growth rates or market size, since none are sourced. |

### Summary for drafting

Claims 3–8 and 12 are safe to state directly (conceptual/design claims,
consistent with the chapter themes Source B actually commits to). Claims 1,
2, 8, 13, and 14 must be softened from "fact" to "argued framing" or dropped
entirely — none of them are backed by data in either source, and Source B's
own claimed methodology (13) does not exist in the material available to
this topic. Claims 9, 10, and 11 are usable but require careful, partial
excerption to avoid pulling Article 2/3 material into Article 1 — see the
per-claim notes and cross-check against `spine.md`'s boundary column before
drafting prose.
