'''
Michael Ciskowski
COMP 4030
Assignment 8
11/14/2017
'''

'''
Problem 1:
Implement the following strategy in Python: 
Find the first word (starting from the end of the input text) 
that is in the dictionary, and repeat the process.
'''
def restorable(D, text):
	if text == [] or text in D:
		return True	

	for i in range(len(text)-1, -1, -1):
		if text[i:len(text)] in D:
			return restorable(D, text[0:i])
		
	return False

dictionary = {'this', 'that', 'is', 'are', 'a', 'cat', 'dog'}
text = 'thisisacatdog'
print('Problem 1: Text, dictionary:', text, ',', dictionary, '\nResult:', restorable(dictionary, text))
'''
Problem 2:
Show an example of an input text for which the previous algorithm does not work
correctly.

This example will not work since the word 'thesis' contains the word 'is' at the
end. Calling restorable on the substring 'thethes' will return false since there
are no longer recognized words in the dictionary.
'''
#text = 'isthethesis'
#dictionary = {'is','thesis', 'the'}
print('Problem 2: Text, dictionary:', text, ',', dictionary, '\nResult:', restorable(dictionary, text))

'''
Problem 3:
Write the running time equation of the function in problem 1. What is the running time
in terms of Theta?
'''
def revised_restorable(D, text):
	if text == [] or text in D:
		return True

	for i in range(len(text)-1, -1, -1):
		u = text[:i]
		v = text[i:]
		if revised_restorable(D,u) and revised_restorable(D,v):
			return True
	return False
		
print('Problem 4: Text, dictionary:', text, ',', dictionary, '\nResult:', revised_restorable(dictionary, text))

'''
Problem 5:
'''
def is_restorable(text, D):
	R = [False] * len(text)
	for i in range(0, len(text)):
		for j in range(i, len(text)):
			u = text[:i]
			v = text[i:j]
			
			if u in D:
				R[i-1] = True

			if v in D:
				R[j] = True
				if i == 0:
					R[-1] = True
				
	return R[-1]

text = 'isthethesis'
dictionary = {'is','thesis', 'the'}
print('Problem 5: Text, dictionary:', text, ',', dictionary, '\nResult:', is_restorable(text, dictionary))
