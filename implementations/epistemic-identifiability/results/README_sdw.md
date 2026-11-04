# SDW (structural discovery world) results - development only
* `sdw_dev/main_ns25000.pkl` (+ `_report.md/.json`, `.log`): primary evaluation, 360 instances x all agents/baselines x B in {3,5,8}.
* `sdw_dev/calib_ns27000.pkl`, `test_ns28000.pkl`, `calibrated_criticism_ns28000_report.{md,json}`: calibration follow-up (doc 19 addendum B).
* `sdw_dev/tuned_config_ns24200.json`, `tuning_median_rmse_ns24200.json`: baseline tuning on known families only.
* `sdw_dev/proposal_kalman_ns25000.json`: post-hoc Kalman-smoother proposal comparison. `sdw_dev/est/`: learned state-estimator weights (3 seeds) and logs.
* Reproduce (venv with torch, numpy, scipy, scikit-learn, pysindy 2.1.0): `scripts/sdw_train_est.py S` (S=1,2,3); `scripts/sdw_tune.py`; `scripts/sdw_run.py --ns 25000 --n 40 --out results/sdw_dev/main_ns25000.pkl`; `scripts/sdw_report.py main.pkl report.md`; calibration: `sdw_run.py --ns 27000 --n 20 --fams lin,sat,delay --variants falsify,sweepB ...`, `sdw_run.py --ns 28000 --n 30 --variants falsify,sweepB ...`, `sdw_calib_report.py`; `scripts/sdw_kalman_proposal.py`.
* Interpretation: `topics/bostrom-world-models/world-models-programme/18`-`21`. Namespaces exposed: 24100-24103, 24200, 24500, 25000-25360+, 26000+, 27000+, 28000+.
