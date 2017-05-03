# COMP 4030/6030: Assignment 6
# Due date: 04/25/2016
# Email programming solutions to the TA (Quang Tran, qmtran@memphis.edu). Put "COMP 4030/6030 assignment 6" on the subject line.

# 1. Suppose that a text can be corrupted in such a way that all punctuations and spaces have been deleted. For example, if the original 
# text is "it was the best of times.", then the corrupted version is itwasthebestoftimes. Given a string S, it is desirable to know if S 
# is a corrupted text. To do this, we have to check if S is a concatenated sequence of valid words. Available to us is a dictionary D that 
# contains all valid words. To check if a word w is in the dictionary, you can do this in Python: w in D. If D contains w, the expression 
# will return True. For example, if the dictionary D is {apple, best, it, of, the, times, was} and S =itwasthebestoftimes, then the answer 
# is True. If given the same dictionary D, S =itwasthebe, then the answer is False.

# Hint:
# * You might want to define a function IsValid(S, i) that returns True if and only if the substring S[0:i+1] is a concatenated sequence 
# 		of valid words. With this function, the call IsValid(S, len(S)-1) gives the answer that you look for.
# * define IsValid(S, i) in terms of smaller subproblems (i.e. you will make recursive calls, specifically IsValid(S, j) for j to 0 
#		and i-1).
# * As an example, itwasthebest is a concatenated sequence of valid words because best is in the dictionary and itwasthe is a concatenate 
#		sequence of valid words. This example should help you define IsValid(S, i) correctly. 1

'''
Make Dictionary D with words to be detected
Make empty Table={}

for x in range(0,len(S)-1)
	if x in

'''
def StringCheck(S):
	'''
	for x in D:
		print(x, x in S)
	The above is the exact opposite if what the directions are asking.
	You are seeing if COMBINATIONS AND LENGTHS OF SUBSRINGS are in DICTIONARY;
	***NOT*** if ENTRIES IN DICTIONARY are in STRING
	'''
	for x in range(len(S)):
		print(isValid(S[0+x:],x))
	
def isValid(S,i): 
	print(S[0:i])
	pass
	#just pretend you have exactly what you need for this

D={"There","is", "no", "way", "here"}
S="Tereisnowayhere"
	
StringCheck(S)
'''
itwasthebestoftimes
twasthe
'''