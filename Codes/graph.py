import random
INFINITY = float("inf")

def random_graph(n,p,seed=None):
	random.seed(seed)
	g = Graph()
	for i in range(n):
		for j in range(i,n):
			if random.random() < p:
				g.add(i,j)
	return g

class Node(object):
	def __init__(self, id):
		self.id = id

	def __str__(self):
		return str(self.id)

class Graph(object):
	def __init__(self, *vertex_attrs):
		self.Edges = {}
		self.Vertices = {}
		self.Neighbors = {}
		self.vertex_attrs = vertex_attrs

	def add_vertex(self, i):
		if i not in self.Vertices:
			self.Vertices[i] = Node(i)
			for a in self.vertex_attrs:
				setattr(self.Vertices[i], a, None)
			self.Neighbors[i] = set()

	def delete_vertex(self, i):
		if i in self.Vertices:
			del self.Vertices[i]
			for j in self.Neighbors[i]:
				del self.Edges[i,j]
				del self.Edges[j,i]
				self.Neighbors[j].remove(i)
			del self.Neighbors[i]

	def add(self, i,j, w=None):
		self.Edges[i,j] = w
		self.add_vertex(i)
		self.Neighbors[i].add(j)
		self.Edges[j,i] = w
		self.add_vertex(j)
		self.Neighbors[j].add(i)

	def __getitem__(self, thing):
		if isinstance(thing, tuple):
			if thing not in self.Edges:
				return None
			return self.Edges[thing]
		else:
			if thing not in self.Vertices:
				return None
			return self.Vertices[thing]

	def __contains__(self, thing):
		if isinstance(thing, int):
			return thing in self.Vertices
		else:
			return thing in self.Edges


class DGraph(object):
	def __init__(self, *vertex_attrs):
		self.Edges = {}
		self.Vertices = {}
		self.In = {}
		self.Out = {}
		self.vertex_attrs = vertex_attrs

	def add_vertex(self, i):
		if i not in self.Vertices:
			self.Vertices[i] = Node(i)
			for a in self.vertex_attrs:
				setattr(self.Vertices[i], a, None)
			self.Out[i] = set()
			self.In[i] = set()

	def delete_vertex(self, i):
		if i in self.Vertices:
			del self.Vertices[i]
			OUT = [j for j in self.Out[i]]
			for j in OUT:
				del self.Edges[i,j]
				self.Out[i].remove(j)
				self.In[j].remove(i)
			del self.Out[i]
			IN = [j for j in self.In[i]]
			for j in IN:
				del self.Edges[j,i]
				self.Out[j].remove(i)
			del self.In[i]

	def add(self, i,j, w=None):
		self.Edges[i,j] = w
		self.add_vertex(i)
		self.Out[i].add(j)
		self.add_vertex(j)
		self.In[j].add(i)

	def __getitem__(self, thing):
		if isinstance(thing, tuple):
			if thing not in self.Edges:
				return None
			return self.Edges[thing]
		else:
			if thing not in self.Vertices:
				return None
			return self.Vertices[thing]

	def __contains__(self, thing):
		if isinstance(thing, int):
			return thing in self.Vertices
		else:
			return thing in self.Edges
