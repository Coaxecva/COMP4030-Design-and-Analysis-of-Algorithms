
# finding (length of a) longest increasing subsequence.
# lis = [0,7,8,9,10,50,100], length = 7

# most important step to do backtracking:
# Solution = [-1] * N
# def LIS(i):
# 	pass

# DP
# LIS(L, i) returns the length of the longest increasing subsequece of L[0:i+1]
# and this LIS must end at index i.
Table = {}   # Table[i] stores LIS(L,i)

def LIS(L, i):
	if i in Table:
		return Table[i]

	# What's the smallest case?
	if i<0:
		output = 0
		Table[i] = output
		return output

	# How do we compute LIS(L,i) in terms of LIS(L, j) for j's less than i.
	# Fact: LIS(L, i) = LIS(L, j) + 1 for some j<i and L[j]<L[i].
	# Check all values of j less than i and select the best possibility
	longest = 1
	# longest = LIS(L, i) = max_j { LIS(L, j) + 1 : j<i and L[j]<L[i]  }
	for j in range(i):
		if j<i and L[j]<L[i]:
			if longest < LIS(L,j) + 1:
				longest = LIS(L, j) + 1
	# longest = LIS(L, i) = max_j { LIS(L, j) + 1 : j<i and L[j]<L[i]  }
	Table[i] = longest
	return longest

def longest_increasing_sub(L):
	# m = LIS(L, 0)
	# for i in range(len(L)):
	# 	if m < LIS(L, i):
	# 		m = LIS(L, i)
	# return m
	values = [ LIS(L,i) for i in range(len(L)) ]
	print(values)
	return max(values)

###########################################################
import util
import time

# items = [10,0,50,7,60,8,9,10,3,50,40,100,0]
# # print( "the answer is:", LIS(items, len(items)-1) )
# print( "the answer is:", longest_increasing_sub(items))

N = 500
items = util.random_list(N,0,10*N)
start = time.time()
print( "the answer is:", longest_increasing_sub(items))
end = time.time()
print("Running time", end-start)

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

