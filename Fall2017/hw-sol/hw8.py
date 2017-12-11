
def greedy_restorable(text, D):
	if text == '':
		return True
	for i in range(len(text)-1, -1, -1):
		if text[i:] in D:
			# print(text[i:])
			return greedy_restorable(text[0:i], D)
	return False

#-----------------------------------------
def is_restorable(text, D):
	R = [False] * len(text)
	for i in range(0, len(text)):
		print(i)
		for j in range(0, i+1):
			u = text[0:j]
			v = text[j:i+1]
			if (u=='' or R[j-1]) and v in D:
				R[i] = True
			print("\t",j,u,v,R[i])
	print(R)

#-----------------------------------------




