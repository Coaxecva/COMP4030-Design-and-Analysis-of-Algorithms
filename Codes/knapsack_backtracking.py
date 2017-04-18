# Generate all sets with N elements.

# N=4, {0,3}.  Solution = [True, False, False, True]
'''
Given N, how many possible sets are there with N items? 2^N
N=3, {}, {0}, {1}, {2}, {0,1}, {0,2}, {1,2}, {0,1,2}
We can represent a set as a boolean vector.  Example, {0,2} --> [True,False,True] = Solution
Solution[i] represents whether or not item i is in the set.
This is how we can have 2^N possible sets with N items.
'''

# Goal: use backtracking to enumerate all possible sets with N items


'''
What does Sets(i) assume about Solution?  It assumes that Solution has some values at
	indices 0, 1, ..., i.
What does Sets(i) do?  print out all sets that have this specific partial configurations.

Example:
N=5
Solution = [False,True,False,-1,-1]
Sets(2) prints:
[False,True,False,False,False] -> {1}
[False,True,False,True,True] -> {1, 3, 4}
[False,True,False,False,True] -> {1, 4}
[False,True,False,True,False] -> {1, 3}

'''
def get_set(s):
	sol = []
	for i in range(len(s)):
		if s[i]==True:
			sol.append(i)
	return sol

def Sets(i):
	if i==N-1:
		print(get_set(Solution))
	else:
		Solution[i+1] = False
		Sets(i+1)
		Solution[i+1] = True
		Sets(i+1)
N=5
Solution = [-1] * N
# Sets(-1)


'''
item		weight				calories			cal/wt
0				6					3000				500
1				3					1400				467
2				4					1600				400
3				2					900					450

Cap = 10.	{0, 1} --> [ T, T, F, F]
1. What are all possible valid solutions? 
	{0,1,2,3} is not valid.
2. What is a valid solution with maximum calories? 
	{0,2} or [True,False,True,False] has 4600 calories.
'''

'''
Goal#1: find all possible valid solutions.
(a) how do we represent solutions?   A list of boolean values.
(b) what are the inputs?  
	Calories - a list of N numbers
	Weights - a list of N numbers
	C - capacity of the bag
'''


def show_bag(s):
	calories, weight = 0, 0
	for i in range(len(s)):
		if s[i]:
			calories += Calories[i]
			weight += Weights[i]
	return "Calories: %d, Weight: %d" % (calories, weight)

def Knapsack1(i):
	if promising(i):
		if i==N-1:
			print(show_bag(Solution), get_set(Solution))
		else:
			Solution[i+1] = False
			Knapsack1(i+1)
			Solution[i+1] = True
			Knapsack1(i+1)

def promising(i):
	total_weight = 0
	for j in range(i+1):
		if Solution[j] == True:
			total_weight += Weights[j]
	return total_weight<=C


# Goal#2: find valid solution with maximum calories.

def get_calories(s):
	calories, weight = 0, 0
	for i in range(len(s)):
		if s[i]:
			calories += Calories[i]
			weight += Weights[i]
	return calories

def Knapsack2(i):
	global maximum_calories, optimal_solution
	if promising(i):
		if i==N-1:
			# print(show_bag(Solution), get_set(Solution))
			if maximum_calories < get_calories(Solution):
				maximum_calories = get_calories(Solution)
				optimal_solution = get_set(list(Solution))
				# print("best so far:", maximum_calories, Solution)
		else:
			Solution[i+1] = False
			Knapsack2(i+1)
			Solution[i+1] = True
			Knapsack2(i+1)

Calories = [3000,1400,1600,900]
Weights = [6,3,4,2]
C = 10
N = len(Calories)
Solution = [-1] * N
maximum_calories = 0
optimal_solution = []

def knapsack_bt():
	maximum_calories = 0
	optimal_solution = []
	Knapsack2(-1)
	print("maximum calories:", maximum_calories)
	print("optimal solution:", optimal_solution)


knapsack_bt()