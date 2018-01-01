'''
Michael Ciskowski
COMP 4030
Assignment 9
12/5/2017
'''

'''
Problem 1: 
This Python function (pal) is slow. 
Rewrite pal using a cache to speed it up.
'''
Table = {} #Table to store the cached values
def pal_cached(seq):
	#Check if the value has already been calculated
	if seq in Table:
		return Table[seq]
	if len(seq) <= 1:
		Table[seq] = len(seq)	#First cache location
		return Table[seq]
	if seq[0] == seq[-1]:
		Table[seq] = 2 + pal(seq[1:-1])	#Second cache location
		return Table[seq]
	else:
		Table[seq] = max(pal(seq[1:]), pal(seq[:-1]))#Final cache location
		return Table[seq]

#Original function for running time comparison
def pal(seq):
	if len(seq) <= 1:
		return len(seq)
	if seq[0] == seq[-1]:
		return 2 + pal(seq[1:-1])
	else:
		return max(pal(seq[1:]), pal(seq[:-1]))
#----------------------------------------------------------------
# Simple comparison of running time for problem 1
import random, time
def rand_str(n, chars):
	return ''.join([ random.choice(chars) for i in range(n) ])
test_input = rand_str(25, 'acgt')

start = time.time()
pal(test_input)
end = time.time()
print('Raw running time for original function with input ', test_input,': ', end - start, sep='')

start = time.time()
pal_cached(test_input)
end = time.time()
print('Raw running time for cached function with input ', test_input,': ', end - start, sep='')
#----------------------------------------------------------------
#-------------------------------------------------------------------
'''
Problem 2: Complete Strangers
'''
def sets(i, solution, graph):
	if i==len(solution)-1:
		if correct(solution, graph):#Function to check if the solution is complete strangers			
			print(solution)
	else:
		for item in graph.Neighbors:
			if item not in solution:
				solution[i+1] = item
				sets(i+1, solution, graph)

#Function to test if the solution is of complete strangers
def correct(solution, graph):
	for i in range(len(solution)):
		for j in range(len(solution)):
			if solution[i] in graph.Neighbors[solution[j]]:
				return False
	return True

import graph
g = graph.random_graph(5, 0.4, directed=False)
print(g.Neighbors)
sets(-1, [None, None, None, None, None], g)
#-------------------------------------------------------------------
'''
Problem 3: Largest group of strangers
'''
all_solutions = []
def largest_group(graph):
	global all_solutions
	#iterate through all possible solution sizes
	for i in range(2, len(graph.Neighbors)+1):
		all_sets(-1, [None]*i, graph)

	m = 0	#max size
	tmp = 0	#index of the max size
	for j in range(len(all_solutions)):
		if len(all_solutions[j]) > m:
			m = len(all_solutions[j])
			tmp = j
	if tmp == 0:#if there are no sets of complete strangers
		print('There is no group of complete strangers in the graph:', graph.Neighbors)
	else:
		print('Largest group of strangers is', m, ':', all_solutions[tmp])

#Function to find the complete stranger sets
def all_sets(i, solution, graph):
	if i < 0 or promising(i, solution, graph):
		if i==len(solution)-1:
			if correct(solution, graph):
				all_solutions.append(solution)
		else:
			for item in graph.Neighbors:
				if item not in solution:
					solution[i+1] = item
					all_sets(i+1, solution, graph)
#-------------------------------------------------------------------
#Problem 5: Promising solution pruning
def promising(i, solution, graph):
	for neighbors in graph.Neighbors[i]:
		if neighbors in solution[:i]:
			return False
	return True
#-------------------------------------------------------------------
largest_group(g)