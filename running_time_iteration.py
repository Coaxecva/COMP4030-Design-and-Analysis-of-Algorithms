'''
1. Running time of a program is *proportional* to the number of steps the program takes.
	exact number of steps depends on inputs (different paths of executions).
	worst case, average case running time.
2. Input size or problem size.  Running time of a program depends on *size* of the input(s).
	Running time of a program is a function of input size.
	Ex: T(n) = 2*n + 5
3. Abstracting "steps" into *constants*.

'''

# input size is number of items in L.  Call this n.
# running time is proportional to n.
# assume criterion(item) takes exactly 1 step.  Assume each statement takes exactly 1 *step*.
# input size (n) = length of the list L
# Worst case: T(n) = 4n + 3
def filter(L, criterion):
	selected = []
	count = 0
	for item in L:
		# print(count)
		count += 1
		if criterion(item) == True:
			selected.append(item)
	return selected

filter([1,2,3,4,5,6,7], lambda x: x%5==0) 

# input size (n) : length of L
# T(n) = n^2 + 2
def foo(L):
	s = 0
	for i in L:
		for j in L:
			s = s + i + j
	return s

# running time of this block of code is n*m
def bar(n,m):
	steps = 0
	for i in range(n):
		for j in range(m):
			print(i,j, steps)
			steps += 1
	print("steps", steps)

# L is a list of numbers.
# n = length of L
# T(n) = c*n^2 + b
def f(L):
	s, i, j = 0, 0, 0
	while i < len(L):
		s = s + i
		i += 1
		j = 0
		while j < len(L):
			j += 1
			s = s * j
	return s

# T(n) = cn^2 + b
def g(L):
	s, i, j = 0, 0, 0
	while i < len(L):
		s = s + i
		i += 1
		j = 0
		while j < len(L):
			j += 3
			s = s * j
	return s

# T(n) = c*n*log2(n) + b
def h(L):
	s, i, j = 0, 0, 0
	while i < len(L):
		s = s + i
		i += 1
		j = 1
		while j < len(L):
			j = j * 2
			s = s * j
	return s



# T(N) = log2(N)
N, j, steps = 1000000, 1, 0
while j < N:
	print(j, steps)
	j = j * 2
	steps += 1

'''
steps		j  (j = j * 2)
0			1  	= 2^0
1			2	= 2^1
2			4	= 2^2
3			8	= 2^3
4			16	= 2^4
.
.
.
k			N 	= 2^k   Therefore, k = log2(N)
'''

# T(n) = c*n*log`(n) + b
def h(L):
	s, i, j = 0, 0, 0
	while i < len(L):
		s = s + i
		i += 1
		j = 1
		while j < len(L):
			j = j * 10
			s = s * j
	return s


# n = input size = # of items in the list L
# T(n) = c*log(n) + b
# T(n) is in O(n). T
# T(n) is in O(log n)
def k(L):
	s, i, j = 0, 1, 1
	while i < len(L):
		i = i * 2
		s = s + i*i
	return s

# len(L) = 1000 = n
# n^2 = 1000000
'''
i 		steps (k)
1		0
2^1		1
2^2		2
2^3		3
2^4		4
.
.
.
2^k=n	k  (when while loop stops)

2^k = n, or k = log2(n)
'''

# T(n) = c*log2(n)*log4(n) + b
# Is T(n) in O(n^2)?
def bar(L):
	s, i, j = 0, 1, 1
	while i < len(L):
		i = i * 2
		s = s + i*i
		j = 1
		while j < len(L):
			j = j * 4
			s = s + j*j
	return s

