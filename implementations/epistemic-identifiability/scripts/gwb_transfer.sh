#!/bin/zsh
cd "$(dirname "$0")/.."; R=results/gwb_final/runs; PY=$HOME/.venvs/eid/bin/python
for F in A B; do
PYTHONPATH=src $PY scripts/gwb_eval.py --ns 9200 --threads 6 --conds uniform sweep --family $F \
 --groups trainedAonly_pred=$R/det_pred_onlyA_s1 trainedAonly_ici=$R/det_ici_onlyA_s1 trainedBonly_pred=$R/det_pred_onlyB_s1 trainedBonly_ici=$R/det_ici_onlyB_s1 trainedBoth_pred=$R/det_pred_s1 trainedBoth_ici=$R/det_ici_s1 untrained=$R/det_untrained_s1 \
 --out results/gwb_final/eval_transfer_probe${F}_ns9200.json > results/gwb_final/eval_t$F.stdout 2>&1 &
done
wait
