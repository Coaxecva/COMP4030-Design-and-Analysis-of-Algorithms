# Question 1
T = {}
#-----------------------------------
# T[seq] stores value of pal(seq)
#-----------------------------------
def pal(seq):
	if len(seq) <= 1:
		T[seq] = len(seq)
		return T[seq]
	if seq[0] == seq[-1]:
		T[seq] = 2 + pal(seq[1:-1])
		return T[seq]
	else:
		T[seq] = max(pal(seq[1:]), pal(seq[:-1]))
		return T[seq]

#-----------------------------------

import random
def rand_str(n, chars):
	return ''.join([ random.choice(chars) for i in range(n) ])


#-----------------------------------

# Question 2
import graph
G = graph.random_graph(10, 0.15, False, seed=42)
G.draw(prog='neato')
'''
{}, {1}, {2}, {0}, ...... {5}
{0,5}, {0,1}, ....
'''
#-----------------------------------
def get_set(s):
	return [ i for i,x in enumerate(s) if x==True ]

def count(s):
	return sum([1 for x in s if x==True])

#-----------------------------------
def strangers_sets(i, solution, g):
	global largest
	if promising(i, solution, g):
		if i==len(solution)-1:
			if count(largest) < count(solution):
				largest = solution.copy()
				print(get_set(solution))
		else:
			for choice in [False, True]:
				solution[i+1] = choice
				strangers_sets(i+1, solution, g)

#-----------------------------------------------------
# checks if latest choice (solution[i]) still makes solution
# promising.  In this case, solution[0:i+1] still a set of
# strangers.
#-----------------------------------------------------
def promising(i, solution, g):
	global largest

	# Check if the latest choice (solution[i]) is a valid choice
	if solution[i] == False: # vertex i not slected.
		return True

	for j in range(0,i):
		# check for connection between vertex i and vertex j.
		if solution[j]==True and (i,j) in g:
			return False

	# look at largest and solution[0:i+1]
	if count(solution[0:i+1]) + (len(g.Vertices)-i) < count(largest):
		return False

	return True

#-----------------------------------
largest = []
strangers_sets(-1, [None]*len(G.Vertices), G)
print('Largest', get_set(largest))





