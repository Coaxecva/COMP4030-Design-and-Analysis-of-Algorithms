'''
Q2.
T(n) = 2n + 9T(n/3)
T(n) is in Theta(n^2)

Q3.
T(n) = 4n^2 + 9T(n/3)
T(n) is in Theta(n^2 log n)

Q4.
T(n) = 4n + 4T(n/3)
T(n) is in Theta(n^(log_3 4))
'''

# Q1
# votes = ['C', 'C', 'T', 'T', 'C', 'T', 'C', 'C', 'T']

def majority_brute_force(L):
	for x in L:
		count = 0
		for i in range(len(L)):
			if x == L[i]:
				count += 1
		if count > len(L)/2:
			return x
	return None

# majority(L, i, j) returns the majority element from interval [i,j]
# T(n) : is the running time of majority(L, i, j). (n is the number of items in [i,j])
# The running of majority(L, 0, 100) is T(101)
# T(n) = 2*T(n/2) + n. T(n) is in Theta(n log n)
def majority(L, i, j):
	# 0. Handle smallest case(s)
	if i==j:
		return L[i]
	if i>j:
		return None

	# 1. find the majority elements in the left and right halves.
	middle = (i+j)//2
	# maj_left = majority_brute_force(L[i:middle+1])
	maj_left = majority(L, i, middle)   # majority(L, i, middle) returns maj ele from interval [i,middle]
	maj_right = majority(L, middle+1, j)

	# 2. determine the majority in [i,j] in O(n) time.
	count_left, count_right = 0, 0
	for k in range(i,j+1):
		if L[k] == maj_left:
			count_left += 1
		if L[k] == maj_right:
			count_right += 1
	if count_left > (j-i+1)/2:
		return maj_left
	if count_right > (j-i+1)/2:
		return maj_right
	return None

def rand_list(n=500):
	chars = 'abc'
	v = ''
	for i in range(n):
		rand_c = chars[ random.randint(0, len(chars)-1) ]
		v += rand_c
	return list(v)

import time
import random

for n in range(1000, 20000, 2000):
	votes = rand_list(n)
	
	start = time.time()
	print( majority_brute_force(votes) )
	end = time.time()
	print("Bruteforce", n, end-start)

	start = time.time()
	print( majority(votes, 0, len(votes)-1) )
	end = time.time()
	print("Quick", n, end-start)
