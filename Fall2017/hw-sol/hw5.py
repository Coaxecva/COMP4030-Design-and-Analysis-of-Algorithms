'''
1. T(n) = 4n + T(n/4)
Compare 1 versus log4(1)
T(n) is in Theta(n)

2. T(n) = 4n + 4T(n/4)
Compare 1 vs log4(4)
T(n) is in Theta(n * log(n))

3. T(n) = 4n + 5T(n/4)
Compare 1 < log4(5) = 1.16
T(n) is in Theta(n^log4(5)) = Theta(n^1.16)

5.
n is the number of items between L and R.
T(n) = c*n.  Theta(n). Linear time.
S(n) = c.	Theta(1). Constant space.
'''
my_list = [1,2,3,4,5,6,7,8]
#--------------------------------------------
# 4.  Foo splits A in place.
import random
def split(A, L, R):
	pivot = A[ L ]
	i, j = L, R
	while True:
		while A[i] <= pivot and i<R:
			i = i + 1
		while A[j] > pivot and j>L:
			j = j - 1
		if i >= j:
			A[L], A[j] = A[j], A[L]
			return j
		A[i], A[j] = A[j], A[i]
#--------------------------------------------
# 6. Use this split to sort lists.
def qsort(A, L, R):				# S(n)
	if L < R:
		p = split(A, L, R)		# c
		qsort(A, L, p-1)		# S(n/2)
		qsort(A, p+1, R)		# S(n/2)

# S(n) = c + 2S(n/2)
# Compare 0 vs log2(2) = 1.  S(n) is in Theta(n)

# S(n) = n + 2S(n/2)
# Compare 1 vs log2(2).  S(n) is in Theta(n log(n))

#--------------------------------------------
print(my_list)
split(my_list, 0, len(my_list)-1)
print(my_list)
qsort(my_list, 0, len(my_list)-1)
print(my_list)
