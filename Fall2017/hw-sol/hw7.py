
#-----------------------------------------------------------
# Input: A, j
# Output: max sum of consecutive numbers, ending at index j
#-----------------------------------------------------------
Table = {}
# Table[j] = the output of maxsum_ending_at_j(A, j)
def maxsum_ending_at_j(A, j):
	if j in Table:
		return Table[j]

	if j==0:
		Table[j] = A[0]
		return Table[j]

	Table[j] = max(A[j],  A[j]+maxsum_ending_at_j(A, j-1))
	return Table[j]

# Q2.  T(x) = c + T(x-1)
# T(n) = c + T(n-1)
# T(n) = c + (c + T(n-2)) = 2c + T(n-2)
# T(n) = 3c + T(n-3) = ..... = n*c + T(0).
# T(n) is in Theta(n)

#-----------------------------------------------------------
def maxsum(A):
	# max sum of consec. numbers in A must end at some j.
	m = maxsum_ending_at_j(A, 0)
	for j in range(1, len(A)):
		tmp = maxsum_ending_at_j(A, j)
		if m < tmp:
			m = tmp
	return m
	# or using list comprehension
	# return max([ maxsum_ending_at_j(A, j) for j in range(len(A)) ])

# Q4:
# T(n) = n * G(n) = n * n = n^2
# T(n) = n * c
#
#-----------------------------------------------------------
def maxsum_iter(A):
	# Table[j] has same value as maxsum_endind_at_j(A,j)
	Table = [0] * len(A)
	Table[0] = A[0]
	for j in range(1, len(A)):
		Table[j] = max(A[j],  A[j]+Table[j-1])
		# Table[j-1] has same value as maxsum_endind_at_j(A,j-1)
		# Table[j] = max(A[j],  A[j]+maxsum_ending_at_j(A, j-1))
	return max(Table)

#-----------------------------------------------------------
L = [-20,50,-30,40,10,5,-50]

# for j in range(len(L)):
# 	print(j, maxsum_ending_at_j(L, j))
print(maxsum(L))
print(maxsum_iter(L))

