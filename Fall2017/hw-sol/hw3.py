'''
3.

'''
def h(L):
	n = len(L)
	i = n-1
	sum = 0
	while i>=0:
		i = i-1
		j = 1
		while j<n:
			j = j*2
			sum = sum + L[i] + L[j]

# Question: T(n) is in O(n^2)?
# because lines 12-15 takes at most c*n steps.
# T(n) is in Ω(n)?
# c1 * n ≤ T(n) ≤ c2 * n^2
#
# Unroll inner loop
'''
For each iteration i:
	after 0 step: j = 1
	after 1 step: j = 2
	after 2 steps: j = 4 = 2^2
	after 3 steps: j = 8 = 2^3
	after 4 steps: j = 2^4
	.
	.
	.
	after k steps: j = 2^k

	In the last step: j=2^k = n
	So, k = log2(n)

For each iteration i, inner loop takes c*log2(n)
T(n) = c*n*log2(n) is in O(n log n)
T(n) is in Ω(n log n)
T(n) is in Theta(n log n)
'''

def g(L):
	n, sum = len(L), 0
	for i in range(n):
		for j in range(n*n):
			for k in range(j):
				sum = i+j+L[i]

'''
Loop 1:  takes n iterations.
Loop 2:  takes n^2 iterations.
Loop 3:  takes at most n^2 (O(n^2))
T(n) takes at most n*n^2*n^2 = n^5
T(n) is in O(n^5)
T(n) is in Ω(n^3)

'''

def bar(L):
	n, sum = len(L), 0
	for i in range(n):
		sum += L[i]
	value = 1
	for j in range(n*n):
		value *= j
		foo(sum, value)

'''
lines 62-64: T(n) = c*n + d
The number of iterations of the loop is n^2
Each iteration takes n*log(n)
So, the r.t. of the loop is: n^3*log(n)

lines 62-67:
T(n) = c*n + d + e*n^3*log(n)
	≤ cn^3log(n) + dn^3log(n) + en^3log(n)
	≤ (c+d+e) * n^3 log(n)

Therefore, T(n) is in O(n^3 log n)
constant is c+d+e
T(n) is in Ω(n^3 log n)
T(n) is in Theta(n^3 log n)

T(n) = c*n + d + e*n^3*log(n) ≥ 1*n^3log(n)
Therefore T(n) is in Ω(n^3 log n), with c=1.

'''




