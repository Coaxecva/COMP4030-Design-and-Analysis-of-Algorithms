
'''
Task: cook dinner
'''

def cook_dinner(chicken, beans, veggies):
	'''
	cut up the chicken
	wash veggies
	cut and sate the chicken
	boil water
	...
	'''
	pass

'''
Sort numbers, len(L) = n
Running time: T(n) is in Theta(n^2)
Space: S(n) is in Theta(n)
'''
def sort1(L):
	'''
	1.find the smallest number
	2.add it to an empty list 
	3.remove the smallest number from the original list
	4.repeat that process
	'''
	S = []
	while len(L) > 0:					# Theta(n^2)
		smallest = L[0]					# O(1),  c1
		for item in L:					# O(n),  c2*n
			if item < smallest:
				smallest = item
		S.append(smallest)  			# O(1),  c3
		L.remove(smallest)				# O(n),  c4*n

										# total complexity in each iteration: (c2+c4)*n + c1+c3, Theta(n) 
	return S

'''
Sort numbers, len(L) = n
Running time: T(n) is in Theta(n^2)
Space: S(n) is in Theta(1)
'''
def sort2(L):
	'''
	0.do nothing if L empty.
	1.find the smallest number
	2.add it to an empty list (don't do this to reduce space.  Instead move it to front.)
	3.repeat that process (with fewer items in L)
	'''
	for j in range(len(L)):
		smallest_idx = j
		for i in range(j, len(L)):
			if L[i] < L[smallest_idx]:
				smallest_idx = i
		L[j], L[smallest_idx] = L[smallest_idx], L[j]


def sort3(L):
	if len(L) == 0:
		return L
	'''
	1. Find smallest
	2. Remove it from list L
	3. Solve subproblem
	'''
	smallest = L[0]
	for item in L:
		if smallest > item:
			smallest = item
	L.remove(smallest)
	return [smallest] + sort3(L)


L = [9,30,2,10,29,-39,57]
print(sort3(L))