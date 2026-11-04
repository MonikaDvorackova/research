# MDW (active discovery) results - development only
* `mdw_dev/runs/{wm_s1-3 (v1), wm2_s1-3 (v2), reg_s1-2}` trained models (weights + logs); `mdw_dev/mdw_main_ns23000.json` (+summary), `mdw_wm1_ns23500*`, `mdw_wm2_*`, `unseen_v{1,2}_ns23500.json`, `wm_imagination_diagnostic.txt`, `sysid_lambda_selection.txt`, `dev_smoke_ns22100.json`.
* Reproduce: `scripts/mdw_train.py --kind wm|reg --seed S [--steps 12000 --H 192 --ss 0.8 --wlast 4]`; `scripts/mdw_eval.py --ns 23000 --n 40 --lam 0.1 --wm <dirs> --reg <dirs> --out ...`; `scripts/mdw_unseen.py`; `scripts/mdw_report.py`.
* Interpretation: `topics/bostrom-world-models/world-models-programme/16`, `17`.
