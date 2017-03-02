'''
- trominoes
- length
- count even
- select strings containing searched keywords in a list of strings
- merge sort
- binary search
- quick sort
- find kth best items
- integer multiplication

- running time analysis of recursive function.
'''

# returns length of a list L
def length(L):
	if L==[]:
		return 0
	# strategy: 1 + length of the same list starting from the second element.
	return 1 + length(L[1:])

def length2(L, idx):
	if idx == len(L):
		return 0
	return 1 + length2(L, idx+1)
	# strategy: 1 + length of the same list starting from idx + 1
	# irreducible case: when idx == len(L)


# print( length2([1,2,34,302,3029], 0))

# returns the sum of all even numbers in L
def sum_even(L):
	if L==[]:
		return 0
	# strategy:
	# if first item is even: L[0] + sum of all even numbers starting from second item.
	# else (first item is odd):  sum of all even numbers starting from second item.
	if L[0]%2==1:
		return sum_even(L[1:])
	else:
		return L[0] + sum_even(L[1:])


# problem: find all strings containing a keyword K in a list of strings L.
# what are the inputs? L, K, idx
# what is the strategy?

def find_keywords(L, K, idx, output):
	if idx < len(L):
		# strategy: analyze L[idx]
		if K in L[idx]:
			output.append(L[idx])
			find_keywords(L, K, idx+1, output)
		else:
			find_keywords(L, K, idx+1, output)


# output = []
# find_keywords(['the cat is cute', 'the cat is lazy.', 'I am dog.'], 'cat', 0, output)
# print(output)

def merge(A,B):
	C = []
	a, b = 0, 0
	while a < len(A) and b < len(B):
		if A[a] < B[b]:
			C.append(A[a])
			a += 1
		else:
			C.append(B[b])
			b += 1
	if a==len(A):
		C = C + B[b:]
	else:
		C = C + A[a:]
	return C

# print( merge([1,10,20], [5,7,15,30]))

# return a sorted list based on unsorted list L
def sort(L):
	# if L is irreducible, then simply return it.
	if len(L) <= 1:
		return L
	# divide L into 2 halves
	middle_idx = len(L)//2
	left_half, right_half = L[0:middle_idx], L[middle_idx:]

	# sort left and right halves using the same function we are defining
	sorted_left_half = sort(left_half)
	sorted_right_half = sort(right_half)

	# call merge(left_half, right_half)
	return merge(sorted_left_half, sorted_right_half)

# If L has 1000 numbers, the running of sorting L is T(1000).
# What is the running of sort when input size is n/2? Answer: T(n/2) !!!!
# What is the running of sort when input size is n?  Answer: T(n).
# Running time: T(n) = c*n + 2*T(n/2)

# print(sort([39,20,10,20,3,5,0,4980,230]))
