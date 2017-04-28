
W = [2,5,11]

def packable(i, c):
	if c == 0:
		return True
	if i < 0:
		return False
	i_not_selected = packable(i-1, c)
	if W[i] <= c:
		i_selected = packable(i-1, c - W[i])
	else:
		i_selected = False
	return i_not_selected or i_selected

for i in range(30):
	print(i, packable(len(W)-1, i))
