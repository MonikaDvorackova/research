# Technical investigation: What can replay reveal that interventions cannot?

**Status:** Research working note, 2026-11-05. The constructions below are independently checked elementary examples, **not** claims of mathematical novelty. This document records a concrete theoretical investigation, not a literature summary or manuscript.

## Question

Can two generative mechanisms be indistinguishable under *every independent intervention* and yet distinguishable if an observer can replay different interventions against **the same exogenous realization**? If yes, what exactly is the additional information, and does this furnish a nontrivial research direction for embedded observers?

## 1. Explicit one-shot mechanisms

Let A={0,1}, O={0,1}. Each experiment samples an unobserved fair bit U. The experimenter chooses action a and receives output Y. Consider two mechanisms:

- M_same: Y(a,U)=U for both a.
- M_flip: Y(a,U)=U XOR a.

For either mechanism, for either fixed action a, Y is a fair bit. Hence for **any** policy that chooses one action per independent episode, and receives only the resulting output, the transcript law is identical under the two mechanisms. Adaptive choice of actions across independent episodes does not help: conditioned on any past transcript, the next output is fair in both models.

Formal proof by induction on episodes: base case identical; conditional law of Y_k given past and chosen A_k is Bernoulli(1/2) in both, so the joint laws coincide for every finite number of independent episodes and every adaptive policy. Thus no unlimited independent-reset experiment distinguishes them.

Now grant a different oracle: in each round, sample **one** U and return the paired potential outcomes (Y(0,U),Y(1,U)) under the same U. Under M_same the pair is (0,0) or (1,1); under M_flip it is (0,1) or (1,0). One paired replay distinguishes them with zero error.

**Result A (elementary, proved):** equality of all single-world intervention distributions does not imply equality of the joint distribution of cross-world potential outcomes. This is an instance of the well-known distinction between interventions and counterfactuals (Pearl's causal hierarchy), not a new theorem.

## 2. Why the oracle matters

A 'reset' that independently resamples U is not the same as replay with the same U. Under independent reset, even if the observer chooses both actions on different episodes, it sees independent fair bits. Under same-U replay it observes a correlation that is otherwise hidden.

If the physical system permits a *persistent* U across multiple actions in a single trajectory, the difference may become observable without an external replay oracle. Conversely, if the environment always resamples U, a same-U oracle may not be physically realizable by an embedded observer. Therefore 'embedded' cannot be equated with a specific L0–L3 oracle hierarchy without a physical accessibility model.

## 3. A second construction: exact behavioural prediction does not recover implementation

Let M_1 be a one-state mechanism emitting iid Bernoulli(1/2) observations, and M_2 be a two-state mechanism with a hidden state that is independently resampled every step and with emission equal to that state. All finite observation histories have identical laws. The hidden-state cardinalities differ, but this is not an identifiable property without minimality assumptions. The correct inference target is a behavioural equivalence class, not a raw state count.

## 4. What these examples do and do not establish

They **do** establish, in a completely specified formal model, that the answer depends on the joint experimental oracle, not only on how many interventions the observer can execute. They show that an oracle granting cross-world coupling can reveal distinctions inaccessible even to unlimited independent interventions.

They **do not** establish a new result: causal inference has long studied cross-world counterfactual distributions and the limits of identification from observational/interventional data. The example should be treated as a sanity check for any proposed formalism, not as the paper's central discovery.

They **do not** demonstrate a way to detect a simulated universe. A hypothetical host that provides same-U replay is a stronger assumption about experimental access, not a consequence of being simulated.

## 5. Research direction that survives the example (still unverified)

Instead of the already-known abstract hierarchy, specify a **physically implementable embedded oracle**:

- Model observer O as a subsystem of a finite controlled stochastic host H, with an explicit observation channel and actuator channel.
- Require interventions to be realizable as host transitions by O, not external reset or rewinding.
- Allow O to allocate bounded memory and time as host resources, with accounting of how actions perturb the host.
- Define which **cross-world correlations**, if any, can be inferred through an internal proxy process (e.g. persistent noise memory, repeated natural recurrences, synchronizing sequences).

**Candidate research question:** Characterize the cross-world joint functionals identifiable from physically realizable *within-world* trajectories of a coupled observer–host process, as a function of recurrence and accessible state-control, without assuming an external counterfactual oracle.

Novelty is **unknown** and plausibly low: this overlaps causal inference with latent confounding, sequential experimentation, process tomography, controlled HMM identification, and active automata learning. The immediate next step is to find a property with a genuine new separation or bound *after* theorem-by-theorem comparison. Do not write another paper based solely on Result A.

## 6. Precise proof obligations for any candidate theorem

1. Give a fully specified class of coupled observer–host systems, including all observable sigma-algebras.
2. Define the physically permitted policy set, including whether natural resets and shared exogenous variables exist.
3. Define a target functional invariant under observer-visible equivalence; otherwise identification is impossible by definition.
4. Show a lower or upper bound that is not simply a restatement of interventional/counterfactual nonidentifiability.
5. Compare the exact statement against Pearl's hierarchy, dynamic SCM counterfactual identification, POMDP/controlled HMM identifiability, active automata learning, and computational inference-device limits.
6. Supply a proof, explicit counterexample, or carefully scoped conjecture, and clearly label which.
7. Obtain an external specialist check before asserting novelty.

## 7. Immediate scientific verdict

The original manuscript is premature as an original-research paper. The current contribution is a sharpened technical question and two verified elementary constructions, **not** a publishable discovery. The work should remain in the research phase. No experiments are authorized by this note.
