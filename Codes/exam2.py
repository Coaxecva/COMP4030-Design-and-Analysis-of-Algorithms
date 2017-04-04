
def majority(L):
	if len(L)==0:
		return None
	if len(L)==1:
		return L[0]
	M = []
	y = None
	if len(L)%2 == 1:
		y = L.pop()
		M.append(y)
	for i in range(0, len(L), 2):
		if L[i]==L[i+1]:
			M.append(L[i])
	m1 = majority(M)

	# If L has a majority element, then it must be m1.
	# If not, m1 might not be the majority element of L, must double check.
	count = 0
	for x in L:
		if m1 == x:
			count += 1
	if (count > len(L)/2) or (y!=None and count >= len(L)/2 and m1==y):
		return m1
	
	return None


L = list('cctactc')
print(majority(L))
