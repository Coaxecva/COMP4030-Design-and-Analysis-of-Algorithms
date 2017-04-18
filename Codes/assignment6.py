
import graph


def get_set(s):
	return [ i for i in range(len(s)) if s[i] == True]

# CameraCoverage(i) assumes Solution has been set at indices 0, 1, ..., i
# CameraCoverage(i) prints all Solutions having this particular configuration.
def CameraCoverage(i):
	global optimal

	if promising1(i):
		if i==N-1:
			if len(get_set(Solution)) < len(optimal):
				optimal = get_set(Solution)
		else:
			Solution[i+1] = False
			CameraCoverage(i+1)
			Solution[i+1] = True
			CameraCoverage(i+1)

def promising1(i):
	if i < N-1:
		return True
	else:
		for e in G.Edges:
			u, v = e[0], e[1]
			# print(N,u,v,Solution)
			if Solution[u]==False and Solution[v]==False:
				return False
		return True

# N = 4
# G = graph.random_graph(N, 0.5)
# Solution = [-1]*N
# optimal = [ i for i in range(N) ]

# CameraCoverage(-1)
# for e in G.Edges:
# 	print(e, e[0], e[1])
# print("Optimal solution", optimal)

def largest_clique(i):
	global optimal
	if promising2(i):
		if i==N-1:
			# print(get_set(Solution))
			if len(optimal) < len(get_set(Solution)):
				optimal = get_set(Solution)
		else:
			Solution[i+1] = False
			largest_clique(i+1)
			Solution[i+1] = True
			largest_clique(i+1)

def promising2(i):
	if Solution[i]==False:
		return True
	for j in range(i+1):
		if i!=j and Solution[j]==True and (i,j) not in G:
			return False
	return True

# N = 5
# G = graph.random_graph(N, 0.5)
# Solution = [-1]*N
# optimal = []
# largest_clique(-1)
# print("G:")
# for e in G.Edges:
# 	print(e)
# print("Optimal", optimal)


def k_clique(i):
	if promising3(i):
		if i==N-1:
			print(get_set(Solution))
		else:
			Solution[i+1] = False
			k_clique(i+1)
			Solution[i+1] = True
			k_clique(i+1)

def promising3(i):
	if i < N-1:
		return True
	if len([j for j in range(N) if Solution[j] == True]) < K:
		return False
	for j in range(N):
		for k in range(j+1,N):
			# print(j,k, (j,k) not in G)
			if j!=k and Solution[k]==True and Solution[j]==True and (j,k) not in G:
				return False
	return True

N = 4
K = 2
G = graph.random_graph(N, 0.5)
Solution = [-1]*N
k_clique(-1)
print("G:")
for e in G.Edges:
	print(e)
