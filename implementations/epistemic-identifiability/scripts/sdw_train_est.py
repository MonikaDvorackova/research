"""Train the learned state estimator (known families only).  usage: sdw_train_est.py SEED"""
import sys, os, time, torch
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from eid.sdw import rep
seed = int(sys.argv[1]); out = os.path.join(os.path.dirname(__file__), "..", "results", "sdw_dev", "est")
torch.set_num_threads(2); t0 = time.time(); f = open(f"{out}/est_s{seed}.log", "w")
log = lambda s: (f.write(s + "\n"), f.flush())
m = rep.train(seed, log=log); torch.save(m.state_dict(), f"{out}/est_s{seed}.pt"); log(f"done {time.time()-t0:.0f}s")
