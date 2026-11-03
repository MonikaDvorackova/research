---
id: topic-bostrom-world-models-review-mm
title: "Reviewer-style assessment for Minds and Machines (self-review, Phase 2)"
topic: bostrom-world-models
type: review
status: active
created: 2026-11-03
updated: 2026-11-03
tags: [review, journal-fit]
---

## Reviewer-style assessment

Written by the research team against its own material, as a deliberately critical referee. It has not been checked against *Minds and Machines* author guidelines (not retrieved this session), so fit judgements are provisional.

### Summary of the submission as it stands

The paper would argue that detecting a discrepancy, identifying a generative mechanism, and concluding "simulation" are three distinct inferences with distinct premises; support this with elementary formal propositions on distinguishability and evidential bounds; and illustrate it with a toy experiment in which an agent testing consistency with its own learned theory fails to detect a learned world model and falsely flags the true environment under out-of-distribution interventions.

### Strengths

1. The three-way separation, with explicit bridge premises (artifact, reference, bridge to ancestor simulations), is clear and usable, and it is tied to propositions rather than asserted.
2. Honest treatment of the negative result: the experiment does not show detection succeeding; it shows how the agent's own theory becomes the weak point.
3. Reproducible code, seeds, tests, an equivalent negative control that is not exploited, and a documented post-hoc control.

### Weaknesses (major)

1. **Mathematical contribution is thin.** Propositions 3–6 are short consequences of the definition of total variation, the chain rule, and a change of measure. A mathematically trained referee will see them as framing. The paper must say so and must not present them as theorems of independent interest. The one place with some substance, the tightness of the c^t factor in Proposition 3(a), is an open obligation.
2. **Philosophical novelty is unestablished.** Theses T1–T3 (fidelity-indexed testability; asymmetry of detection; insulation of Bostrom's argument) resemble familiar points about underdetermination, falsifiability and the sceptical structure of the argument (Birch 2013 and others). Prior statements may exist that I have not found: the philosophical literature was checked at title/abstract level, Chalmers's book and several neighbours were not read, and the citation analysis is partial. A referee familiar with this literature could judge T1–T3 not new. The contribution would then rest on the quantitative form (Propositions 4–5) and the learned-model illustration.
3. **The experiment is far from the philosophical target.** A fully observed 2-D toy system, a theory built from the reference, one architecture family, and no partial observability. The step from the toy result to any claim about embedded observers is made by argument, not evidence. The key empirical finding (false alarms up to 1.000 under out-of-distribution interventions, W looking more theory-like than reality) may be an artifact of Q and W sharing architecture and training distribution; this was not tested.
4. **Post-hoc control and exploratory status.** AltOOD was added after seeing v1. This is documented, but it limits what can be claimed.

### Weaknesses (minor)

- Bootstrap intervals over ten seeds ignore within-seed variance; no multiple-comparison handling across the many cells.
- "Active" experimentation is an uncertainty proxy, not exact expected information gain; the claim that active selection "does not help" applies to this proxy and this detector only.
- Detector uses a single statistic with no tuning; negative detector results are not general.
- Several bibliographic items remain unverified (see verification log).

### Questions a referee would ask

1. What does the toy result add that Propositions 3(b) and 6 do not already say?
2. Does the agent's theory need to be learned? A symbolic or analytically correct theory would remove the Q-misfit effect: would detection then work, making the finding a statement about estimation error rather than epistemology?
3. Where is the connection to the observer-selection part of Bostrom's argument, beyond the claim that high fidelity insulates it?
4. Is "simulation" in T1 defined so that a fidelity-indexed hypothesis is a hypothesis about simulation at all, rather than about a particular model of physics?

### Journal fit (provisional)

- *Minds and Machines*: plausible audience for the epistemological argument and the AI link, provided the philosophical thesis is shown to be new relative to the literature and the formal part is positioned as supporting analysis. Risk: referees may see the experiment as decoration.
- *Philosophy & Technology*: similar fit, possibly more tolerant of a shorter technical part.

### Verdict at this stage

**Not ready to write as a manuscript.** The defensible path is to (a) close the literature gaps, (b) test thesis novelty against the philosophical literature, (c) strengthen the experiment with the architecture and "correct theory" ablations that questions 2 and the weakness 3 point to, and then reassess.
