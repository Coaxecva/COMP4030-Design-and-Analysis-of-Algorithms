#James Hopkins
#COMP6030 Homework 6

from graph import Graph, DGraph

#Graph for Question 1
GA = DGraph()
GA.add(0,1,2)       						
GA.add(0,2,2)       						
GA.add(1,3,2)
GA.add(2,3,2)
GA.add(0,3,2)
GA.add(1,2,2)
GA.add(3,4,2)
GA.add(4,5,2)  
GA.add(5,6,2)      						
GA.add(5,7,2)       						
GA.add(6,8,2)
GA.add(7,8,2)
GA.add(5,8,2)
GA.add(6,7,2)

#Question 1:
def min_cameras(i, c):
	global num_cameras
	if i == N-1:
		b = get_set(Solution)
		c = cameras(b)
		if len(c) < num_cameras:
			if len(c) > 0:
				num_cameras = len(c)
				if c not in Answers:
					Answers.append(c)
	else: 
		Solution[i+1] = True
		min_cameras(i+1, c)
		Solution[i+1] = False
		min_cameras(i+1, c)

	return len(Answers)

def get_set(s):
	sol = []
	for i in range(len(s)):
		if s[i] == True: 
			sol.append(i)
	return sol

def cameras(s):
	clique = []

	for j in s:
		for o in GA.Out[j]:
			for i in s:
				if i == o:
					if j not in clique:
						clique.append(j)
				
	return clique


Answers = []
N = 9
Solution = [-1]*N
num_cameras = N
print(min_cameras(-1, num_cameras))

#Graph for Questions 2 and 3
G = Graph()
G.add(0,1)       						
G.add(0,2)       						
G.add(1,3)
G.add(2,3)
G.add(0,3)
G.add(1,2)
G.add(3,4)
G.add(4,5)  
G.add(5,6)      						
G.add(5,7)       						
G.add(6,8)
G.add(7,8)
G.add(5,8)
G.add(6,7)

#Question 2:

def max_clique(i, c):
	global max_clique_value
	if i == N-1:
		b = get_set(Solution)
		c = valid_clique(b)
		if len(c) >= max_clique_value:
			max_clique_value = len(c)
			if c not in Answers:
				Answers.append(c)
	else: 
		Solution[i+1] = True
		max_clique(i+1, c)
		Solution[i+1] = False
		max_clique(i+1, c)

	return Answers

def get_set(s):
	sol = []
	for i in range(len(s)):
		if s[i] == True: 
			sol.append(i)
	return sol

def valid_clique(s):
	clique = []

	for j in s:
		for e in G.Edges:
			for i in s:		
				if (j,i) in [e]:
					if i not in clique:
						clique.append(i)
					if j not in clique:
						clique.append(j)			
		else:
			break
				
	return clique

max_clique_value = -1
Answers = []
N = 9
Solution = [-1]*N
print(max_clique(-1, max_clique_value))


#Question 3:
def clique_k(i, k):
	
	if i == N-1:
		b = get_set(Solution)
		c = valid_clique(b)

	else: 
		Solution[i+1] = True
		clique_k(i+1, k)
		Solution[i+1] = False
		clique_k(i+1, k)

	return Answers

def get_set(s):
	sol = []
	for i in range(len(s)):
		if s[i] == True: 
			sol.append(i)
	return sol

def valid_clique(s):
	clique = []

	for j in s:
		for e in G.Edges:
			for i in s:		
				if (j,i) in [e]:
					if i not in clique:
						clique.append(i)
					if j not in clique:
						clique.append(j)	
		else:
			break
				
	if len(clique) >= k:
		if clique not in Answers:
			Answers.append(clique)
		return Answers

Answers = []
k = 4
N = 9
Solution = [-1]*N
print(clique_k(-1, k))
