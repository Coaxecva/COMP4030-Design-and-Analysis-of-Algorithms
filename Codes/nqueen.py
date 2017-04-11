
N = 5
# Solution[i] = j means a Q is placed at column j on row i.
Solution = [-1] * N

'''
When Permutations(i) is called, it is assumed that Solution[0], Solution[1], ..., Solution[i]
have been configured.   Then, Permutations(i) will print all possible permutations having this
partial configuration.

Example:  Solution[0] = 3, Solution[1] = 0.
Permutations(1) prints out [3,0,1,2], [3,0,2,1]
'''
def Permutations(i):
	if i==N-1:
		print(Solution)
	else:
		for j in range(N):
			if j not in Solution[0:i+1]:
				Solution[i+1] = j
				Permutations(i+1)


# Permutations(-1)

def NQueens(i):
	if promising(i):  # then keep exploring the search tree
		if i==N-1:
			print(Solution)
		else:
			for j in range(N):
				if j not in Solution[0:i+1]:
					Solution[i+1] = j
					NQueens(i+1)

def promising(i):
	for k in range(i):
		if i-k == abs(Solution[i]-Solution[k]):
			return False
	return True

# NQueens(-1)
