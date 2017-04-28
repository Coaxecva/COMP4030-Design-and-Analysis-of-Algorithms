###########################################################
#
coins = [4,5,13,17]
X = 11

# make_change(L, value) returns True if and only if it is possible to make
# change for value dollars using coins in L.
# make_change(L, value) = OR{ make_change(L, value-coin) for some coin in L }
# Table[value] stores the value of make_change(L, value)
def make_change(L, value):
	if value in Table:
		return Table[value]

	if value < 0:
		Table[value] = False
		return False

	for coin in L:
		if make_change(L, value-coin) == True:
			Table[value] = True
			return True

	Table[value] = False
	return False
	# return any([make_change(L,value-coin) for coin in L])

# value = 100,
# make_change(coins, 100) is True if and only if
# make_change(coins, 96) is True, or
# make_change(coins, 95) is True, or
# make_change(coins, 87) is True, or
# make_change(coins, 83) is True


###########################################################
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



