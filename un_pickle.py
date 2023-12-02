import numpy as np

metrics = np.load("results/test_FFTransformer_Wind_ftM_sl64_ll48_pl6_0/metrics.npy")
pred = np.load("results/test_FFTransformer_Wind_ftM_sl64_ll48_pl6_0/pred.npy")
pred_un = np.load("results/test_FFTransformer_Wind_ftM_sl64_ll48_pl6_0/pred_un.npy")
true = np.load("results/test_FFTransformer_Wind_ftM_sl64_ll48_pl6_0/true.npy")
true_un = np.load("results/test_FFTransformer_Wind_ftM_sl64_ll48_pl6_0/true_un.npy")

print("finished reading in")