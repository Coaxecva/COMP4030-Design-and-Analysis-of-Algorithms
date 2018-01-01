###
# Austin Henley
# COMP 8901
# Assignment 9
###


###
# Problem 1
### 

def pal(seq):
	if len(seq) <= 1:
		return len(seq)
	if seq[0] == seq[-1]:
		return 2 + pal(seq[1:-1])
	else:
		return max(pal(seq[1:]), pal(seq[:-1]))


T = {}
def pal_cached(seq):
	if seq in T:
		return T[seq]

	tmp = 0
	if len(seq) <= 1:
		tmp = len(seq)
	elif seq[0] == seq[-1]:
		tmp = 2 + pal_cached(seq[1:-1])
	else:
		tmp =  max(pal_cached(seq[1:]), pal_cached(seq[:-1]))

	T[seq] = tmp
	return tmp

import random
def rand_str(n, chars):
	return ''.join([ random.choice(chars) for i in range(n) ])

def generateTestSet(k, n, chars):
	A = []
	for i in range(k):
		A.append(rand_str(random.randint(0, n), chars))
	return A

###
# Measure time for Problem #1
###

import datetime
A = generateTestSet(50, 20, "acgt") # 50 strings of length 0 to 20

t1 = datetime.datetime.now()
for a in A:
	pal(a)
t2 = datetime.datetime.now()
d1 = (t2-t1).microseconds # elapsed time of pal()

t1 = datetime.datetime.now()
for a in A:
	pal_cached(a)
	T = {}
t2 = datetime.datetime.now()
d2 = (t2-t1).microseconds # elapsed time of pal_cached()

print("pal took %d, pal_cached took %d" % (d1, d2))


###
# Problem 2, 3, and 4
# Problem 2 already says to do pruning 
# so its the same as #4 (and #3) but also keep track of largest
### 

import graph

def areNeighbors(G, v1, v2):
	if v1 in G.Neighbors[v2]:
		return True
	return False

largest = []
def strangers(G, i, solution):
	global largest
	if i==len(solution)-1:
		print(solution)
		# check if largest
		if sum(solution) > sum(largest):
			largest = solution[:] # copy by value
	else:
		for item in [False, True]:
			solution[i+1] = item
			
			# pruning
			# only continue if its True and has no neighbors
			for v in range(i):
				if solution[v] and solution[i+1]:
					if areNeighbors(G, v, i+1):
						return
			strangers(G, i+1, solution)

Gd = graph.random_graph(3, 1.0, directed=False)
# True/False represents whether the node at that index
# is included or not. Start with all False.
strangers(Gd, -1, [False]*3)
print("The largest: ", largest) # if there are ties, it just prints the first



