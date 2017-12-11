# depth first traversal; decrease and conquer

import graph

#------------------------------------------------
def explore_d(G, v):
	v.marked = True
	neighbors = G.Out[v.id]
	for uid in neighbors:
		if G[uid].marked == False:
			explore_d(G, G[uid])
#------------------------------------------------
def explore(G, v):
	v.marked = True
	neighbors = G.Neighbors[v.id]
	for uid in neighbors:
		if G[uid].marked == False:
			explore(G, G[uid])
#------------------------------------------------
def status(G):
	for vid in G.Vertices:
		print(G[vid])
#------------------------------------------------
# problem 1.
#------------------------------------------------
def reachable(G, uid, vid):
	u, v = G[uid], G[vid]
	for w in G.Vertices:
		G[w].marked = False
	explore_d(G, u)
	if v.marked == False:
		return False
	for w in G.Vertices:
		G[w].marked = False
	explore_d(G, v)
	if u.marked == False:
		return False
	return True

#------------------------------------------------
# problem 2
#------------------------------------------------
def num_of_communities(G):
	count = 0
	# Init
	for vid in network.Vertices:
		network[vid].marked = False

	# For each unvisited vertex:
	#    Explore G starting from it
	for vid in network.Vertices:
		if network[vid].marked == False:
			count += 1
			explore(G, network[vid])

	return count

#------------------------------------------------
network = graph.random_graph(15,0.15,directed=False)
# print( reachable(network, 0, 1) )
print(num_of_communities(network))
network.draw()
status(network)


