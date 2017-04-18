Table = {}
# Table[(i,c)] stores the output of Knapsack(i,c)

# Knapsack(i,c) computes the optimal value given Capacity c for items 0 to i.
def Knapsack(i, c):
	if (i,c) in Table:
		return Table[(i,c)]

	if i<0 or c<=0:
		output = 0
		Table[(i,c)] = output
		return output

	i_in_opt, i_not_in_opt = 0, 0

	if c >= Weights[i]:
		# 1. Item i is in the optimal solution
		# Knapsack(i,c) = Calories[i] + Knapsack(i-1,c-Weights[i])
		i_in_opt = Calories[i] + Knapsack(i-1,c-Weights[i])

	# 2. Item i is not in the optimal solution
	# Knapsack(i,c) = Knapsack(i-1,c)
	i_not_in_opt = Knapsack(i-1,c)
	output = max(i_in_opt, i_not_in_opt)
	Table[(i,c)] = output
	return output

# Knapsack2(c) returns the optimal value given capacity c.
def Knapsack2(c):
	if c <= 0:
		return 0
		
	# If item 0 is in optimal solution, Knapsack2(c) = Calories[0] + Knapsack2(c-Weights[0])
	# If item 1 is in optimal solution, Knapsack2(c) = Calories[1] + Knapsack2(c-Weights[1])
	possibilities = [0]
	for i in range(len(Calories)):
		if c <= Weights[i]:
			possibilities.append( Calories[i] + Knapsack2(c-Weights[i]))
	return max(possibilities)

Calories = [3000,1400,1600,900]
Weights = [6,3,4,2]
C = 12
print( Knapsack(len(Calories)-1, C) )

# import util
# import time

# for N in range(5,100):
# 	Weights = util.random_list(N, 10, 20)
# 	Calories = util.random_list(N, 2000, 3000)
# 	C = Weights[0] * len(Weights) * 0.4
# 	start = time.time()
# 	opt_val = Knapsack(len(Calories)-1, C)
# 	end = time.time()
# 	# print(Weights, Calories, C)
# 	print(N, opt_val, end-start)
