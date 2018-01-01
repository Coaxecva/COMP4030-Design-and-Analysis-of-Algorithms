'''
Kieu Do
Comp 4030
Assignment 8
'''
#-----------------------------------------
#prob: 1
#-----------------------------------------
def isRestorable (text, D):
	if len(text) == 0:				# smallest case
		return False
	if len(D) == 0: 				# smallest case
		return False

	d = list(D)				 		# make a copy of the list
	u = text    					# set u as the current text

	for index in range(len(text)-1, -1, -1): 
									# start from the end of u index
		v = u[index:len(u)] 		# v is the text from current index to last index

		if v in d:					# check if word is in dict
			d.remove(v) 			# if word is in dict then remove the text from the list
			u = u[0:index]  		# set new text starting at index 0 to current index in for loop
			if index == 0:  		# if the last word is in dict 
				return True 		# return true

	return False
#-----------------------------------------
	'''
	Logic behind function:

	u = thisisacat
	d = { "this", "that", "is", "are", "a", "cat", "dog" }

		(1)
			v = u[9:] => t
			v = u[8:] => at
			v = u[7:] => cat 
		(2) remove "cat" in d
				d = { "this", "that", "is", "are", "a", "dog" }
		(3) set u = u[0:7] => thisisa
		-----------------
		(1)
			v = u[6:] => a
		(2) remove "a" in d
				d = { "this", "that", "is", "are", "cat", "dog" }
		(3) set u = u[0:6] => thisis
		-----------------
		(1)
			v = u[5:] => s
			v = u[4:] => is
		(2) remove "is" in d
				d = { "this", "that", "are", "cat", "dog" }
		(3) set u = u[0:4] => this
		-----------------
		(1) 
			v = u[3:] => s
			v = u[2:] => is
			v = u[1:] => his
			v = u[0:] => this
		(2) remove "this" in d
				d = {"that", "are", "cat", "dog" }
		(3) if index = 0 and v = u[0:] in d then return true
 	'''
#-----------------------------------------
#prob: 2 
#-----------------------------------------
'''
test case: "this is a cat"
test case: "thisthisisacat"
'''
#-----------------------------------------
#prob: 3 running time
'''
def isRestorable (text, D):						T(n)
	if len(text) == 0:							d
		return False							d
	if len(D) == 0: 							d
		return False							d

	d = list(D) 								n
	u = text   									d	

	for index in range(len(text)-1, -1, -1): 	n - 1
												
		v = u[index:len(u)] 					n - m 

		if v in d:								c
			d.remove(v) 						n
			u = u[0:index] 						m - 0  	
			if index == 0:  					c	
				return True 					c

	return False								d
	
T(n) = n + c*((n-1)*(n-m)*(m)) + d
	 = n + c*((n^2 - m - n)*(m)) + d
	 = n + c*(n^2m - m^2 - nm) + d
T(n) is in Theta(n^2)
'''
#-----------------------------------------
#prob: 4 
#-----------------------------------------
def isRestorable_recursive (text, D):
	if len(text) == 0:				# smallest case
		return False
	if len(D) == 0: 				# smallest case
		return False

	if text in D:					#check if the current text is in dictionary
		return True

	for i in range(len(text)-1, -1, -1):
									# start from the end index of text
		v = text[i:]				# v is the text from current index to last index
		if v in D:					# check if v is in dict
			u = text[0:i] 			# if v in dict, 
									# set u to be new text from index 0 
									# up to current index in for loop

			return isRestorable_recursive(u, D) # recursively call u and D 

	return False
#-----------------------------------------
#prob: 5
#-----------------------------------------
def isRestorable_iterative(text, D):
	if len(text) == 0:				# smallest case
		return False
	if len(D) == 0: 				# smallest case
		return False

	R = [False] * (len(text)+1)		# new list, setting all False	
	R[0] = True                     # set first index 0 to be True

	for i in range(0, len(text)):	# go through all indices in text
		for j in range(i, -1, -1):	# start from the end of i index and go backward
			u = R[j]				# u is the current boolean in R
			v = text[j:i+1]			# v is the new text from j index to index i + 1
			if v in D:				# check if v text is in dict
				R[i+1] = True		# if True, mark it True on R	

	return R[len(text)]				# return the boolean for the last index
#-----------------------------------------
	'''
	Logic behind function:

R [False, False, False, False, False, False, False, False, False, False, False, False]

i: 0, j:0
i: 1, j:1,0
i: 2, j:2,1,0
i: 3, j:3...
i: 4, j:4...
i: 5, j:5...
i: 6, j:6... 
i: 7, j:7...
i: 8, j:8...
i: 9, j:9...
		v => R[0] - > True
		v => t | R[1] - > False
		v => th | R[2] - > False
		v => thi | R[3] -> False
		v => "this" | R[4] -> True
		v => i | R[5] -> False
		v => "is" | R[6] -> True
		v => a | R[7] -> True 
		v => c | R]8] -> False
		v => c"a"| R[9] -> True
		v => "cat" ->| R[10] - True

R = [True, False, False, False, True, False, True, True, False, True, True]

*Case where this function fails, if last word is True, 
and there's a word not in dictionary.*
	Like: "thisiszacat" (z is not in dictionary)
	Outout: True (instead of False)
	'''
#-----------------------------------------

text = "thisisacat"
dictionary = { "this", "that", "is", "are", "a", "cat", "dog" }

#---------------------------------------------
#prob: 1

print(isRestorable(text, dictionary))
#Output: True

#---------------------------------------------
#prob: 2

#T(n) in Theta (n^2)
#---------------------------------------------
#prob: 3

#having space between each word results in the wrong answer
text_notWork = "this is a cat"
print(isRestorable(text_notWork, dictionary))
#Output: False

#if the word repeats itself
text_notWork2 = "thisthisisacat"
print(isRestorable(text_notWork2, dictionary))
#Output: False

#---------------------------------------------
#prob: 4

print(isRestorable_recursive(text, dictionary))
#Output: True

#---------------------------------------------
#prob: 5

print(isRestorable_iterative(text,dictionary))
#Output: True

#---------------------------------------------
