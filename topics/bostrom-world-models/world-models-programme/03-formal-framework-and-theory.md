---
id: topic-bostrom-world-models-wm-theory
title: "Formal framework: embedded discovery of generative structure; hierarchy of inferences; propositions and counterexamples"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-05
tags: [theory, framework, hierarchy]
---

# 1. Framework
- **Generator class** 𝒢 (privileged): controlled stochastic processes with an implementation tag (e.g. real arithmetic, finite-precision lattice, adaptive resolution). **Interface** (𝒪, 𝒜, noise law): the only channel; **admissible interventions** Π ⊆ policies over 𝒜.
- **Observable object:** the interaction kernel on Π-reachable histories (Prop 1′). Everything an observer can ever learn is a functional of it.
- **Learned world model** m̂: a predictor of observations under actions (any architecture); **hypothesis system** ℋ: a family of structured explanations with likelihoods; **planner** chooses actions (objective: prediction, reward, or information about ℋ).
- **Discovery criterion** (for a class of properties 𝒫): the agent's decision about property π ∈ 𝒫 is correct with probability ≥ 1 − ε, under every generator in a stated family, using budget n and compute c. **Identifiability criterion:** the property is constant on interface-equivalence classes {g : P_g^π = P_{g′}^π ∀π ∈ Π}.
- **Epistemic justification** of an inference: the premises beyond the data it needs (law-class prior, observation interface, resets).

# 2. Five inference levels
L1 predictive adequacy (small expected loss on Π); L2 structural identification (the interaction kernel and its minimal realisation); L3 causal identification (interventional *and* counterfactual structure over latent variables); L4 computational-implementation inference (the generator lies in a computational class, e.g. finite precision); L5 simulation inference (created and run by an agent/civilisation).
**Proposition H (strictness; PROVED by example).** L1 ⇏ L2 ⇏ L3 ⇏ L4 ⇏ L5 in general.
(a) L1⇏L2: two kernels agree on the training policy class and differ elsewhere (Prop 3(b), Prop 1′); the Phase 6 diagnostic gives an exact example.
(b) L2⇏L3: interventional kernels equal, counterfactuals differ; this is the causal hierarchy theorem (Bareinboim et al.; search description only) — **known, not re-proved**.
(c) L3⇏L4: **explicit example (this phase).** quant(q) and stiff(q/2) are identical in law under every admissible control whenever the actuator reach is below the dead-zone threshold (Prop A below): same interventional and counterfactual behaviour, different implementation class.
(d) L4⇏L5: a computational generator can be base reality (Chalmers, read; Bostrom's premise (3) is a separate probabilistic claim). Not testable by data.
**What the hierarchy does not say:** that the implications fail *typically*; only that none follows without premises.

# 3. Propositions for the finite-precision case (system x' = x + dt(−kx + bu), observation y = x + N(0, σ²), x₀ = 0)
**Prop A (interface-limited equivalence; PROVED; elementary).** Let dt·b·u_max < δ. Then quant(q = 2δ), stiff(δ) (and every dead-zone hypothesis with threshold > dt·b·u_max) keep x ≡ 0 under every admissible control; their laws coincide, while cont does not (any constant u ≠ 0 moves it). *Proof:* at x = 0 the update is v = dt·b·u with |v| < δ; quantisation rounds |v| < q/2 = δ to 0; stiction blocks |v| < δ. ∎ Verified exactly in `tests/test_worldgen_pilot.py`.
**Prop B (exact discrimination map; PROVED; known form).** For deterministic-mean Gaussian models the per-episode KL between hypotheses h, h′ under program u is Σ_t (μ_t^h − μ_t^{h′})²/(2σ²); the Chernoff-optimal program maximises min_{h′} of it. At σ = 0.8: best-menu 11.5 vs random-large-control 0.37 nats (cont vs quant(0.2)), 0.40 vs 0.23 (quant(0.2) vs stiff(0.1)). So *KL scales as σ⁻²; the matched pair needs σ ≲ q/ (a few) for identification within tens of episodes.*
**Prop C (modified-equation equivalence; PROVED for linear systems; known in numerical analysis).** The Euler map x' = (I + hA)x equals the exact flow of Ã = h⁻¹ log(I + hA) sampled at step h whenever a real logarithm exists (e.g. A = [[0,1],[−1,0]], h = 0.1: det(I+hA) = 1 + h² > 1). So *discretisation of a conservative oscillator is observationally identical to a continuous non-conservative oscillator*: energy drift cannot be attributed to an integrator without a prior constraining Ã (e.g. conservation). Verified numerically (`test_modified_equation…`). Classification: **known** (backward error analysis; source not read).
**Prop D (nesting; restricted, trivial).** If an inner generator is a program executed by the outer world and the observer sees only outer observations, the composite is again a generator in the outer class; nesting changes identifiability only through an *observable resource channel* (runtime, memory exhaustion, latency). Without such a channel nested ≡ flat. Not tested; no experiment recommended until a channel is formalised.
**Corollary (Bostrom).** A detected finite-precision signature establishes at most L4 for a *restricted* family, relative to the interface (σ ≪ q), the law-class prior (no stiction) and the actuator reach; it never reaches L5 without premises about simulator behaviour (`05`, §5).

# 4. Counterexamples to purported signatures
1. *Finite precision always detectable:* false (Prop A; also σ ≳ q).
2. *Energy drift ⇒ discretisation:* false (Prop C).
3. *Lattice structure of observed values ⇒ finite precision:* true only if observation noise is below the lattice spacing; with σ ≥ q/2 the lattice is invisible and the quant/stiff pair becomes equivalent in practice (`05`, P1).

# 5. Status
All propositions are elementary or known. **No new theorem is claimed.** The only conceptual content is the explicit chain L1 ⇏ … ⇏ L5 with a concrete counterexample at each step that does not rely on a hidden-state toy, and its application to computational signatures.
