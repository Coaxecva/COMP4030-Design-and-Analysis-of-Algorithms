items = [10,0,50,7,60,8,9,10,3,50,40,100,0]
'''
Example of a subsequence: 60,8,9,10;  10,50,60,100; 8; 10,3,100; ...
increasing subsquence: 10,50,60,100.
length of longest increasing subsequence. 0,7,8,9,10,50,100. Length is 7.
Given items, find the length of the longest increasing subsequence of "items"
'''

Table = {}
# LIS(L, i) returns length of longest increasing subsequence
# of L[0:i+1].  This must include the element L[i].
def LIS(L, i):
	if i not in Table:
		if i == 0:
			Table[i] = 1
		m = 1
		for j in range(i):
			if (L[j] < L[i]) and (m < LIS(L,j)+1):
				m = LIS(L,j)+1
		Table[i] = m
	return Table[i]


def longest_increasing_subseq(L):
	return max([ LIS(L, i) for i in range(len(L)) ])

# T[i] == Table{i} == LIS(L,i)
def iLIS(L):
	T = [1] * len(L)
	for i in range(len(L)):
		for j in range(i):
			if (L[j]<L[i]) and (T[i] < T[j]+1):
				T[i] = T[j]+1
	return max(T)

import util
for n in range(20, 1000, 10):
	items = util.random_list(n, 0, 100)
	Table = {}
	print(len(items), longest_increasing_subseq(items), iLIS(items))


