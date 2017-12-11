
#----------------------------------------------------------
# Problem 1.  Theta(n^2)
def max_sum_iterative(L):
	# Idea: look at all possible "intervals"
	cur_max = L[0]
	for b in range(0, len(L)):
		for e in range(b, len(L)):
			s = 0
			for k in range(b, e+1):
				s += L[k]
			if s > cur_max:
				cur_max = s
	return cur_max

#----------------------------------------------------------
# Problem 2.  Running time: Theta(n)
def MaxSumFromStart(B):
	cur_sum = 0
	cur_max = B[0]
	for i in range(0, len(B)):
		cur_sum += B[i]
		if cur_max < cur_sum:
			cur_max = cur_sum
	return(cur_max)
#----------------------------------------------------------
# Problem 3.  Running time: Theta(n)
def MaxSumFromEnd(B):
	cur_sum = 0
	cur_max = B[len(B)-1]
	for i in range(len(B)-1, -1, -1):
		cur_sum += B[i]
		if cur_max < cur_sum:
			cur_max = cur_sum
	return(cur_max)
#----------------------------------------------------------
# Problem 4:
def MaxSum(A):													# T(n)
	if len(A)==1:
		return A[0]
	mid = len(A)//2
	B = A[0: mid]												# n/2
	C = A[mid : len(A)]											# n/2
	max_in_B = MaxSum(B)										# T(n/2)
	max_in_C = MaxSum(C)										# T(n/2)
	max_in_overlap = MaxSumFromEnd(B) + MaxSumFromStart(C)		# n
	return max( max_in_B, max_in_C, max_in_overlap )			# c

#----------------------------------------------------------
# Problem 5: Running time of MaxSum:
# T(n) = c*n + 2T(n/2)
# Compare 1 versus log2(2)
# T(n) is in Theta(n*log(n))
#----------------------------------------------------------
A =  [10, -50, 40, 20, -10, 20, -10, 5]
print(MaxSum(A))
