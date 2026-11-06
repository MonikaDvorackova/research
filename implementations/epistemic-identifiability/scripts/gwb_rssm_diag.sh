#!/bin/zsh
# Controlled diagnostics for the RSSM-vs-GRU predictive gap (gwb benchmark, dev seed 200, 2000 steps, identical data).
cd "$(dirname "$0")/.."; PY=$HOME/.venvs/eid/bin/python; R=results/gwb_dev/rssm_diag; mkdir -p $R
run(){ PYTHONPATH=src $PY -m eid.gwb.train --seed 200 --steps 2000 --budget_s 1500 --threads 3 --out $R/$1 "${@:2}" > $R/$1.stdout 2>&1 }
run V0_rssm_current --model rssm &
run V1_decode_from_h_only --model rssm --dec_h_only 1 &
run V2_dreamer_free1_bal.5.1 --model rssm --free_bits 1.0 --bal 0.5 0.1 &
run V3_no_prior_loss --model rssm --no_prior_loss 1 &
wait
run V4_beta5 --model rssm --beta 5.0 &
run V5_det_gru --model det &
run V6_rssm_H256 --model rssm --H 256 &
run V7_rssm_dec_h_free1 --model rssm --dec_h_only 1 --free_bits 1.0 --bal 0.5 0.1 &
wait
