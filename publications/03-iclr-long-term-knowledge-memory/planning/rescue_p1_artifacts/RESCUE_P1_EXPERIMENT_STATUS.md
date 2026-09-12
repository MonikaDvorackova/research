# Rescue P1 experiment status (labelled NEW)

**Do not mix with Option A freeze.**

## rescue_p1_h4_gold_sanity

- Regenerated H4 subset (seed 100; first 6 worlds per tier) with gold answers via `evaluate_predictions`.
- n_worlds=18, n_bundles=192, n_queries=1260
- Acc=1.0
- BCR=1.0
- ConsAcc_strict=1.0
- n_violations=0

Interpretation: BCR=1 on gold H4 answers means the Qwen BCR=0 floor is not an unsatisfiable constraint suite on the H4 subset.


## rescue_p1_alt_seed_symbolic_mini

Symbolic B3/B4 at k=8; worlds_per_tier=6; seeds 100/101/102.

- seed 100: B3 Acc=0.5667 BCR=0.0625 Gap=0.5042; B4 Acc=0.9317 BCR=0.5938 Gap=0.338 (7.09s)
- seed 101: B3 Acc=0.5667 BCR=0.0625 Gap=0.5042; B4 Acc=0.9302 BCR=0.5938 Gap=0.3364 (6.37s)
- seed 102: B3 Acc=0.5667 BCR=0.0625 Gap=0.5042; B4 Acc=0.9302 BCR=0.5938 Gap=0.3364 (6.21s)

Interpretation: Acc–BCR gaps remain large across seeds under this downsampled protocol; do not overwrite frozen seed-100 full-scale tables.
