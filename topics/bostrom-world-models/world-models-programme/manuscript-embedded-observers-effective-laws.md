> **RESEARCH STATUS — WITHDRAWN AS ORIGINAL-RESEARCH MANUSCRIPT (2026-11-05).** This text was drafted prematurely before establishing a novel research result. It is retained only as a background/conceptual working draft; it must not be submitted or described as a completed scientific contribution. Active research continues in `technical-investigation-counterfactual-coupling.md`. No new theorem or discovery is claimed.

# What Can an Embedded Observer Know? Behavioural Equivalence, World Models, and the Limits of Simulation Detection

**Manuscript draft — conceptual and formal analysis, 5 November 2026.**  
**Author:** Monika Dvořáčková  
**Status:** Full first manuscript; not peer reviewed, not submitted. All propositions below are explicitly identified as elementary consequences of definitions or established prior theory. No claim of a new theorem or empirical evidence for simulation is made.

## Abstract

Can an observer confined to a generative system infer the mechanism that produces its experienced world? The question is frequently conflated with whether an intelligent agent can learn an accurate predictive model and with whether the universe is computationally simulated. We distinguish three objects: the observable dynamics available to an observer, an internal model used to predict those dynamics, and the implementation or substrate realizing them. For controlled stochastic systems, we formalize the observer's epistemic access by an interface specifying admissible policies, observations, resets, and resources. This yields a hierarchy of questions about behavioural equivalence, identifiability of properties, statistical discrimination, and computational feasibility. We show, as elementary consequences of behavioural equivalence, that claims about implementation are inaccessible whenever they vary within an observational equivalence class. We give explicit finite-state examples separating predictive success from hidden structural recovery and one-trajectory from resettable access; neither example is presented as novel. We then examine what learned world models can and cannot add: they can improve approximation and planning within an interface, but cannot overcome an information-theoretic equivalence relation defined by that interface. Applied to the simulation argument, this framework separates Bostrom's probabilistic trilemma from empirically discriminating hypotheses about particular simulators. The contribution is an integrated conceptual taxonomy and a set of criteria for evaluating claims of world-model-based scientific discovery and simulation detection, rather than a new impossibility theorem.

**Keywords:** epistemic identifiability; embedded observers; simulation argument; predictive state representations; causal inference; world models; observational equivalence; underdetermination.

## 1. Introduction

An observer may construct a model that predicts every event it can measure without thereby learning how its environment is implemented. This difference is often blurred in discussions of artificial intelligence and scientific discovery. Predictive models are routinely described as learning the world's rules; conversely, the possibility that reality is simulated is sometimes treated as a hypothesis that sufficiently advanced prediction or anomaly detection could settle. Neither inference follows without specifying what observations and interventions distinguish competing mechanisms.

The issue is especially sharp for an observer *inside* the system of interest. The observer does not choose arbitrary initial conditions for the universe, inspect its entire state, or necessarily rerun a physical history. Its measurements and interventions are themselves events in the system. This is not, by itself, a novel limitation: system identification, automata learning, causal inference, and philosophy of science have developed different accounts of observational equivalence, experimental control, and underdetermination. A useful synthesis must state precisely which question each account answers.

This paper asks: **What can an observer infer about a generative system from an explicitly specified observational and interventional interface, and what remains unknowable even when the observer possesses an accurate learned world model?** The intended answer is deliberately conditional. We do not assume that our universe is simulated, that a particular neural architecture approximates its laws, or that the internal representation of a predictive model uniquely matches physical structure.

The paper makes three contributions of exposition and analysis. First, it separates effective behavioural laws, representational structure, and implementing substrate. Second, it uses an interface-relative formalism to connect established results on predictive representations and statistical distinguishability to the limitations of embedded inference. Third, it derives methodological criteria for assessing simulation-detection claims and world-model experiments. These are conceptual contributions, not claims of priority for behavioural equivalence, information-theoretic impossibility, or reset advantages.

## 2. Three distinct targets of inference

We distinguish:

**Effective laws.** The family of conditional distributions governing observable histories under the interventions available to an observer. These are operationally defined: two worlds have the same effective laws for an interface if no permitted experiment changes the distribution of its recorded outcomes.

**Representational structure.** A graph, state-space model, equation system, program, or latent vector chosen to express effective laws. Distinct representations can realize the same behaviour. Hidden-state labels, redundant latent variables, and nonminimal state spaces are simple examples.

**Implementing substrate.** The physical or computational arrangement in which a mechanism is realized. The same observable dynamics might, as a logical possibility, be implemented by distinct devices or substrates. A claim about a substrate requires a causal route from substrate properties to accessible outcomes.

This separation matters because a representation is not automatically an ontology. Predictive state representations (PSRs), for example, describe dynamical systems through predictions of observable experiments rather than through privileged hidden-state variables [Singh et al., 2004]. Their significance here is methodological: the observable system-dynamics function can be the object of inference even when no particular hidden realization is privileged.

The philosophical literature on underdetermination likewise warns that empirical adequacy and uniqueness of theoretical description are different questions [Stanford Encyclopedia of Philosophy, *Underdetermination of Scientific Theory*]. The framework below makes the scope of adequacy explicit by fixing an observer's interface.

## 3. Formal framework

### 3.1 Mechanisms and interfaces

Let a controlled stochastic mechanism be
[
M=(S,A,O,b_0,T,Omega),
]
where (S) is a hidden state space, (A) the action alphabet, (O) the observation alphabet, (b_0) the initial-state distribution, (T(s'\mid s,a)) a transition kernel, and (Omega(o\mid s,a)) an observation kernel. Finite alphabets suffice for the examples, though the conceptual distinctions do not depend on finiteness.

An observer's **interface** (I) specifies the admissible policy class (Pi_I), which actions can be taken, what observations are returned, and which experimental operations are available. Operations must be defined rather than named informally: a reset to the initial distribution, a reset to a previously observed hidden state, and replay with the same exogenous random variables are different oracles.

For each policy (piinPi_I), the mechanism induces a probability law (P_M^pi) on observable action–observation histories. Define the interface behaviour
[
eta_I(M)=ig(P_M^piig)_{piinPi_I}.
]

**Definition 1 (interface-relative equivalence).**
[
Mequiv_I N
quadLongleftrightarrowquad
P_M^pi=P_N^pi;	ext{for every }piinPi_I.
]
This is an operational equivalence, not an assertion that (M) and (N) share hidden states or substrates.

### 3.2 What properties can be identified?

Let (arphi:mathcal M	o V) be a property of candidate mechanisms.

**Proposition 1 (necessary invariance; elementary).** If (arphi(M)
earphi(N)) for some (Mequiv_I N), then no procedure using only interface (I) can identify (arphi) correctly for both (M) and (N) with certainty.

**Reason.** Every permitted adaptive procedure has the same distribution of observable transcripts under (M) and (N). Its output therefore has the same distribution in both worlds and cannot be almost surely equal to two different values.

This statement is an immediate consequence of the definition; it is **not a new theorem**. Its utility is as a discipline for claims about discovering hidden causes. Before evaluating an algorithm, one must establish that the target property is constant on the equivalence classes induced by the available experiments.

If (Pi_IsubseteqPi_J), then (Mequiv_J N) implies (Mequiv_I N). More experiments can refine equivalence classes, but need not do so strictly for every mechanism family. This observation does not imply that resets always change asymptotic identifiability; they may change only the sample or computational cost of identifying a property.

### 3.3 Three notions that must remain separate

**Behavioural identifiability** concerns whether a property is invariant on (equiv_I)-classes. It is a necessary condition for recovery.

**Statistical learnability** concerns the existence of an estimator that recovers an identifiable target at a specified error level from finite or growing data. For two fixed candidate laws (P) and (Q), the total variation distance of the induced transcript distributions constrains binary testing error. If (mathrm{TV}(P,Q)=0), no test can distinguish them; if the distance is small at a given budget, even an information-theoretically identifiable distinction may be practically inaccessible. For infinite model classes, pointwise distinguishability is not sufficient to establish a uniformly consistent learner.

**Computational learnability** additionally constrains time, memory, or query complexity. Computational indistinguishability can persist when unbounded statistical discrimination is possible; cryptographic pseudorandom functions supply standard examples [Aaronson, 2013]. An asymptotic notion such as negligible distinguishing advantage requires a security parameter and a family of problems. It must not be asserted as a literal equivalence relation for arbitrary fixed finite systems without a chosen tolerance or asymptotic convention.

These distinctions prevent an otherwise common equivocation: 'possible in principle', 'possible with enough observations', and 'feasible for an embedded agent' are not interchangeable.

## 4. Two elementary examples

### 4.1 Predictive adequacy without unique hidden structure

Consider a system emitting an independent fair binary observation at each step, irrespective of the observer's actions. A one-state hidden model can generate these observations. A two-state hidden model with transitions independent of emissions can generate exactly the same observable law, as can infinitely many redundant hidden-state realizations.

The models differ structurally but satisfy (Mequiv_I N) for any interface limited to those actions and observations. No learner can determine the true number of hidden states from those data. The example illustrates nonminimal realization, not an unusual failure of a particular neural model.

Even when a minimal behavioural realization is uniquely characterized up to an appropriate equivalence, its state coordinates or physical implementation need not be uniquely determined. The distinction between behavioural dimension and hidden-state interpretation is central to the PSR literature [Singh et al., 2004].

### 4.2 One trajectory versus independent resets

Let (bin{1/3,2/3}). A mechanism begins in state (s_0), produces one Bernoulli((b)) observation, then transitions irreversibly to an absorbing state (s_1), from which it emits only zero. Actions have no effect.

An observer confined to a single uninterrupted trajectory receives only one informative Bernoulli sample, regardless of how long it waits. Under equal priors on the two candidates, the optimal Bayes classification error is
[
rac12left(1-mathrm{TV}(mathrm{Bern}(1/3),mathrm{Bern}(2/3))ight)
=rac13.
]
A resettable observer who independently restarts the mechanism from (s_0) receives arbitrarily many independent Bernoulli samples and can classify consistently by their empirical mean.

The separation is elementary and relies on an absorbing, nonrecurrent state. It does not demonstrate a new reset hierarchy. In recurrent or mixing systems, the relationship between reset access and learnability changes; existing automata-learning and POMDP literature addresses precisely such restrictions. The lesson is that 'embedded' must be translated into exact restrictions on trajectories, reachability, and experimental control.

## 5. What learned world models add

A learned world model is a procedure for constructing a representation (Q) of the system from histories and possibly using (Q) for prediction, counterfactual approximation, or action selection. Its epistemic reach is limited by the interface used to collect data.

If (Mequiv_I N), no training procedure using only (I) can decide between them reliably. This remains true whether the model is a recurrent network, a latent state-space model, a transformer, a symbolic expression, or an exact Bayesian learner. Architecture cannot manufacture missing distinguishing information.

A useful learned model may nonetheless make inference *tractable* in large systems, compress histories, generalize across related tasks, or plan interventions. These are substantive engineering and learning-theoretic contributions, but they require matched baselines and clearly defined resource constraints. They do not, by themselves, imply recovery of the implementing substrate.

An additional complication arises when predictive evaluation is confined to a policy class (Pi_{mathrm{test}}). Good prediction under that class need not imply accuracy under interventions outside it. A learned representation may discard features irrelevant under training policies but essential under novel interventions. This connects world-model evaluation to predictive sufficiency, causal abstraction, and out-of-distribution intervention support [Beckers and Halpern, 2019; von Kügelgen et al., 2023].

Thus three evaluations should be reported separately: predictive calibration on supported histories; interventional generalization to specified new policies; and recovery of a *well-defined identifiable* property. A high score on the first cannot substitute for the third.

## 6. The simulation argument is not a detection algorithm

Bostrom's simulation argument presents a probabilistic trilemma concerning posthuman civilization, ancestor simulations, and the fraction of observers living in simulations [Bostrom, 2003]. It is not a theorem asserting that an embedded observer can infer a simulator from observed regularities. Nor does its trilemma assign an experimentally measured probability to the simulation hypothesis.

To make a simulation hypothesis testable, one must specify at least two candidate mechanisms whose induced accessible distributions differ. A hypothesis of a behaviourally faithful simulation and a non-simulation yielding the same (P_M^pi) for all permitted policies are observationally equivalent. By Proposition 1, no interface-limited procedure can discriminate them.

This is a conditional epistemic point, not a proof that our universe is or is not simulated. A particular simulator may introduce artifacts: anisotropy, discretization effects, finite-resolution signatures, or other deviations from an alternative physical model. Such effects are testable only if the simulator hypothesis actually entails them and they enter the observer's accessible outcomes. Beane, Davoudi, and Savage [2014] analyze constraints on a specific lattice-simulation model; their conditional physical analysis is not a generic prediction of all conceivable simulations.

The Bayesian problem is equally sensitive to the hypothesis class. Posterior odds require priors and likelihoods. If two broad hypotheses induce the same likelihood for every possible observation, no observation changes their Bayes factor; posterior odds remain driven by prior assumptions. A claim of empirical evidence must therefore identify a likelihood difference, not merely point to the logical possibility of simulation.

Wolpert's results on physical inference devices establish independent impossibility statements about inference inside a universe [Wolpert, 2008]. They reinforce the need for limits, but do not imply that every scientific prediction is impossible, nor do they automatically prove an impossibility theorem about all simulation-detection schemes. The assumptions and targets of each result must be kept distinct.

## 7. Methodological implications for autonomous scientific discovery

The interface perspective suggests a practical evaluation protocol for systems described as discovering the rules of an environment.

**First, define the target before choosing the model.** Is success prediction, identification of an effective behavioural class, recovery of a minimal realization, or reconstruction of a physical implementation? The latter targets need stronger assumptions.

**Second, verify distinguishability.** Specify an intervention policy or test distribution that separates the competing claims. If none exists, the evaluation is measuring preference among representations, not recovery of an identifiable truth.

**Third, avoid benchmark–hypothesis circularity.** If a grammar of candidate mechanisms is built from the same vocabulary as the data generator, success may demonstrate search over a preselected closure rather than open-ended scientific discovery. Holdout generators and alternative representations are necessary, though not sufficient, controls.

**Fourth, separate model criticism from explanation correctness.** A model may predict within noise while employing an incorrect internal structure. Residual tests cannot reject an alternative that is observationally indistinguishable at the chosen precision and intervention budget.

**Fifth, compare information access and computation fairly.** A baseline with oracle access to hidden states, resets, or a richer action space answers a different question. Likewise, an agent that consumes substantially more compute cannot claim architectural superiority on predictive performance alone.

**Sixth, state the epistemic status of negative results.** A failed recurrent network is not evidence that identification is impossible; a proof of equivalence is not evidence that a particular trained model is optimal. Negative benchmark results should be retained when reproducible, but not promoted into universal impossibility claims.

These criteria are applicable beyond simulation debates, including learned dynamics, causal discovery, model-based reinforcement learning, and autonomous research agents.

## 8. Objections and limitations

**Objection: the account is tautological.** Behavioural equivalence and the resulting nonidentifiability are indeed established. The contribution claimed here is not a new impossibility theorem, but the disciplined application of these distinctions to three debates that frequently conflate them: world-model learning, embedded scientific inference, and simulation detection. The value of this synthesis is conceptual clarity, and its novelty must be assessed as such.

**Objection: physical laws are more than distributions of observations.** Agreed. Operational equivalence is not a metaphysical theory of laws. It identifies what a specified observer can infer; it does not decide which ontology is correct or whether realism is warranted.

**Objection: interventions may reveal hidden structure.** Yes, when competing mechanisms induce different interventional distributions and the observer can execute sufficiently informative interventions. The formalism accommodates this by changing (Pi_I). It does not claim universal underdetermination.

**Objection: an observer can reason beyond observed data.** It can use prior knowledge, simplicity principles, symmetries, or theoretical commitments. Such assumptions may rationally select among empirically equivalent models. They do not turn the resulting choice into an identification from the interface alone.

**Objection: finite-state models are too limited for cosmology.** The examples are diagnostic, not cosmological models. No extrapolation from finite-state counterexamples to the actual universe is justified without additional assumptions. The conceptual distinction between observable behaviour and implementation is more general than the toy models, but formal theorems about physical cosmology would require a different model class.

**Objection: the observer's embeddedness is not fully formalized.** Correct. Resource constraints, self-reference, causal access, and absence of reset are different notions. A complete physical theory of embedded observers would need to couple the observer's dynamics to the environment explicitly. This paper supplies an interface-level abstraction, not a universal theory of self-locating inference.

## 9. Conclusion

The central question is not whether an intelligent observer can learn a model of its world. It is which properties of that world remain invariant across all mechanisms compatible with the observations and interventions available to the observer. Effective behavioural laws, learned representations, and implementing substrates answer different questions. Prediction can be excellent while structure remains underdetermined; additional interventions can refine the accessible distinctions; computational constraints can render an information-theoretically possible distinction infeasible.

These observations are grounded in established theory, not new discoveries. Their relevance to the simulation argument is principally negative and methodological: Bostrom's probabilistic trilemma does not provide a universal empirical signature of simulation, and an accurate world model cannot identify an inaccessible substrate. Any purported detection method must name the simulator class, derive an observable difference, and justify its statistical and computational detectability.

The strongest defensible conclusion is therefore conditional. An embedded observer can learn properties of the effective world only to the extent that those properties are distinguishable through its interface and learnable under its resources and assumptions. The remaining gap between an operational account of the world and an account of what realizes it is a limit on inference, not evidence for a particular metaphysics.

## References

Aaronson, S. (2013). Why philosophers should care about computational complexity. In *Computability: Turing, Gödel, Church, and Beyond*. Preprint: https://arxiv.org/abs/1108.1791

Beane, S. R., Davoudi, Z., & Savage, M. J. (2014). Constraints on the universe as a numerical simulation. *European Physical Journal A*, 50, 148. https://arxiv.org/abs/1210.1847

Beckers, S., & Halpern, J. Y. (2019). Abstracting causal models. *Proceedings of AAAI*. https://arxiv.org/abs/1812.03789

Bostrom, N. (2003). Are you living in a computer simulation? *The Philosophical Quarterly*, 53(211), 243–255. https://doi.org/10.1111/1467-9213.00309

Groz, R., Simao, A., Petrenko, A., & Oriat, C. (2015). Inferring finite state machines without reset using state identification sequences. https://doi.org/10.1007/978-3-319-25945-1_10

Singh, S., James, M. R., & Rudary, M. R. (2004). Predictive state representations: A new theory for modeling dynamical systems. *Proceedings of UAI*. https://arxiv.org/abs/1207.4167

Stanford Encyclopedia of Philosophy. Underdetermination of scientific theory. https://plato.stanford.edu/entries/scientific-underdetermination/

von Kügelgen, J., et al. (2023). Nonparametric identifiability of causal representations from unknown interventions. *NeurIPS*. https://arxiv.org/abs/2306.00542

Wolpert, D. H. (2008). Physical limits of inference. *Physica D*, 237(9), 1257–1281. https://doi.org/10.1016/j.physd.2008.03.040

---

**Submission readiness:** This is a coherent full first draft, not a submission-certified paper. Before submission: verify each reference against primary text, choose an appropriate philosophy-of-science/interdisciplinary venue, adapt length and citation style, and obtain an external subject-matter review. The article does not claim a novel mathematical theorem or new experiment.
