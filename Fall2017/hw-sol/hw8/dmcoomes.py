# Author: Damian Coomes
# COMP 4030
# Assignment 8

# 1
def is_restorable(s,D,i):
	if not s:
		return True

	u = s[0:i]
	v = s[i:]
	isV, isU = False, False

	for x in D:
		if s == x:
			return True
		if v == x:
			s = u
			i = len(u)
			isV = True
		if u == x:
			isU = True

	if isV and isU:
		return True
	if(len(u) == 1):
		return False
	return is_restorable(s,D,i-1)

s = "thisisacat"
t = "areiscatdog"
D = {"this", "that", "is", "are", "a", "cat", "dog"}

print(is_restorable(s,D,len(s)))

# 2
'''
It could fail in a situation where the dictionary contains words that share
a lot of the same characters. See example below:
'''
bad = "achatwithfriends"
A = {"a","chat", "hat", "with", "friends"}
print(is_restorable(bad,A,len(bad)))

# 3
'''
T(n) = confusing # len(s) is n; for loop is constant?
= c + T(n-1)
T(n) is in theta(n)
'''

# 4
def rev_is_restorable(s,D,i,L):
	if not s:
		return True

	u = s[0:i]
	v = s[i:]
	isV, isU = False, False

	for x in D:
		if s == x:
			return True
		if v == x:
			i = len(u)
			# we'll return to this word if u is never found
			L[i] = v
			L[len(s)] = s
			s = u
			isV = True
		if u == x:
			isU = True

	if isV and isU:
		return True
	if len(u) == 1:
		if len(L) == 0:
			return False
		else:	
			# retrieve the starting index of the last successful v
			index = min(L)
			# retrieve the full string again
			f_index = max(L)
			# s = original s
			s = L[f_index]
			# limit scope from index 0 to where the last v ends
			s = s[0:index+len(L[index])]
			L={}
			return rev_is_restorable(s,D,index-1,L)

	return rev_is_restorable(s,D,i-1,L)
	'''
def index(s,D,i,L):

	'''

print(rev_is_restorable(bad,A,len(bad),{}))

# 5
def it_is_restorable(text, D):
	R = [False] * len(text)
	for i in range(0, len(text)):
		isV, isU = False, False
		for j in range(0, i):
			u = text[0:j]
			v = text[j:i+1]
			for x in D:
				if v == x:
					isV = True
				if u == x:
					isU = True
			if isV and isU:
				R[i] = True
	return R[len(text)-1]

print(it_is_restorable(bad,A))