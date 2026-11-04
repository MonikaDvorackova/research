# gwb (learned world models) results — development only

* `gwb_dev/` model-selection and failed-version records (namespace 9300; first RSSM version kept as `…FIRST…`, `runs/failed_v1/`).
* `gwb_final/` final-development grid: `runs/<model>_<obj>_s<seed>/{config.json,log.jsonl,final.pt}`, `eval_main_ns9200.json` (+ `_summary.txt`), `eval_transfer_probe{A,B}_ns9200.*`.
* Optimizer checkpoints (`ckpt.pt`) of finished runs were deleted to save ~25 MB; weights (`final.pt`) are kept. Resume support is covered by a test.
* Reproduce: `scripts/gwb_run_grid.sh` (≈35 min CPU, 4 concurrent jobs), `scripts/gwb_classifier.py --seed 1`, then `scripts/gwb_eval.py --groups … --ns 9200` (see `gwb_final/eval_main.stdout`), `scripts/gwb_transfer.sh`, `scripts/gwb_aggregate.py`. Python env: `uv venv` + `uv pip install torch numpy scipy scikit-learn pyyaml pytest matplotlib` (torch 2.15, CPU).
* Summary: `topics/bostrom-world-models/world-models-programme/09-…`.
