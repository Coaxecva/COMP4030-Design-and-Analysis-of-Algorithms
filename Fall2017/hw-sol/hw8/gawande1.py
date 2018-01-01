#Assignment 8
#				COMP 4030
#							Anuja Gawande
#----------------------------------------------------------------------------------------------------
# 1. Determines if the given text can be decomposed into a sequence of words in the given dictionary.
#	 Doesn't work for all cases.

def restore_text(text,D):
	if text == '':
		return True

	if text in D:
		return True

	for i in range(len(text)-1, -1, -1):
		if text[i:] in D:
			return restore_text(text[0:i], D)
	return False

'''
text = 'thisisacat'
text2= ''
text3 = 'dogthis'
D = {'this','that','is','are','a','cat','dog'}
print(restore_text(text,D))
print(restore_text(text2,D))
'''

#--------------------------------------------------------------------------------------
#2. Example of an input text for which the previous algorithm does not work correctly.

text3 = 'dogthis'
D = {'this','that','is','are','a','cat','dog'}
#print(restore_text(text3,D))


#---------------------------------------------------------------------------------------
# 3. T(n,m) = c + n*T(n-d,m)
#	 T(n,m) is in Theta(n^2)

#------------------------------------------------------------

#4.

def restore_text2(text,D):
	if text == '':
		return True

	if text in D:
		return True
	for i in range(len(text)-1, -1, -1):
		if text[i:] in D and restore_text(text[0:i], D) == True:
			return True
	return False


text3 = 'cataisthisdo'
D = {'this','that','is','are','a','cat','dog'}
print(restore_text2(text3,D))


#-------------------------------------------------------------
#5. Solving problem #4 iteratively.
def is_restorable(text,D):
	R = [False] * len(text)
	for i in range(0,len(text)):
		for j in range(i+1,):
			u = text[i:]
			v = text[0:i+1]
			
			if v in D:
				if u[j:] in D:
					R[i] = True
			
	return R[len(text)-1]
	

text = 'is'
D = {'this','that','is','are','a','cat','dog'}
print(is_restorable(text,D))

