# Austin Henley
# COMP 4030
# Assignment 8

def IsTextRestorable_Problem1(string, dict):
	if len(string) == 0:
		return True
	for i in range(len(string)-1, -1, -1):
		print(i, string[i:])
		if string[i:] in dict:
			return IsTextRestorable_Problem1(string[:i], dict)
	return False

def IsTextRestorable_Problem4(string, dict):
	if len(string) == 0:
		return True
	possible = False
	for i in range(len(string)-1, -1, -1):
		print(i, string[i:])
		if string[i:] in dict:
			if IsTextRestorable_Problem4(string[:i], dict):
				possible = True
	return possible

def is_restorable(text, D):
	R = [False] * len(text)
	for i in range(0, len(text)):
		for j in range(i+1, len(text)):
			if text[i:j] in D:
				R[j] = True
			if j == len(text)-1 and R[j] == True:
				return True
	return False

T = {"this", "that", "is", "are", "a", "cat", "dog"}
print(IsTextRestorable_Problem4("thisisacat", T))

###
# 2. T={"that", "hat", "not", "cat"} string="nothat"
# This greedy approach won't work.
###

###
# 3. T(n) is in O(n)
###