def isValid(S,i,j):
	if i<0:
		return False
	if S[i:j] in D:
		if i>0:
			return isValid(S,i-1,i)
		else:
			return True
	return isValid(S,i-1,j)

D={'apple','best','it','of','the','times','was'}
S='itwasthebestoftimes'
print(isValid(S,len(S)-1,len(S)))