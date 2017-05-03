from graph import Graph, DGraph

G = Graph()
'''
G.add(1,2)
G.add(1,3)
G.add(1,7)
G.add(2,4)
G.add(2,6)
G.add(2,7)
G.add(3,6)
G.add(4,5)
G.add(4,7)
'''

G.add(1,2)
G.add(1,3)
G.add(1,4)
G.add(1,6)

G.add(2,3)
G.add(2,5)
G.add(2,7)

G.add(3,4)
G.add(3,5)

G.add(4,5)
G.add(4,6)
G.add(4,7)

G.add(5,6)
G.add(5,7)

G.add(6,7)

MaxV = 1
MaxN = 0
for v in G.Vertices:
	if len(G.Neighbors[v]) > len(G.Neighbors[MaxV]):
		MaxV = v
		MaxN = len(G.Neighbors[v])

def Problem_1(i, edge_sum, count):
	if edge_sum == 0:
		return 0
	for n in G.Vertices:
		if Promising(n, count):
			G.delete_vertex(n)
			return 1 + Problem_1(1, edge_sum - count, count)
	return 0 + Problem_1(1, edge_sum, count-1)

def Promising(i, count):
	return len(G.Neighbors[i]) == count

edges = 0
for x in G.Vertices:
	edges += len(G.Neighbors[x])
edges = edges//2

print(Problem_1(1, edges, MaxN))

