# epistemic-abstention results — development only
* `epi_dev/runs/cond_s{1,2,3}/` class-conditional simulator bank (weights, logs); `epi_dev/dev_smoke_ns11000.json` debugging smoke run (n≈40/category).
* `epi_final/epi_main_ns11200.json` (+ `epi_main_summary.txt`), `leak_audit.json`, `budget_curve.json`.
* Reproduce: `scripts/epi_train_cond.py --seed {1,2,3}`; `scripts/epi_run.py --ns 11200 --calns 11100 --scale 1.0 --wm <det_pred_s1..3> --cond <cond_s1..3> --out …`; `scripts/epi_report.py`; `scripts/epi_leak_audit.py`; `scripts/epi_budget_curve.py` (≈2.5 min + 1 min on CPU).
* Interpretation: `topics/bostrom-world-models/world-models-programme/11-…`, `12-…`.
