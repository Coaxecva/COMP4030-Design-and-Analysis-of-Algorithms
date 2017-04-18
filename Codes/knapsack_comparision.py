import util
import time
import knapsack_backtracking

for N in range(15,25):
	W = util.random_list(N, 10, 20)
	C = util.random_list(N, 2000, 3000)
	Cap = W[0] * len(W) * 0.4
	start_time = time.time()
	knapsack_backtracking.Calories = C
	knapsack_backtracking.Weights = W
	knapsack_backtracking.C = Cap
	
	knapsack_backtracking.knapsack_bt()
	end_time = time.time()
	