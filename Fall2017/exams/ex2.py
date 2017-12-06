# 7
# Cache.  key=input, value=output
# Table[seq] stores the value/output of kinda_slow(seq)
# (i) There are 3 places where the function returns (output).  Cache at those places.
# (ii) Check the cache first before you compute.

Table = {}

def  kinda_slow(seq):				# seq is a string
	if seq in Table:
		return Table[seq]

	if len(seq) <= 1:
		Table[seq] = len(seq)
		# return len(seq)
		return Table[seq]

	if seq[0] == seq[len(seq)-1]:
		Table[seq] = 1 + kinda_slow(seq[0 : len(seq)-1])
		# return 1 + kinda_slow(seq[0 : len(seq)-1])
		return Table[seq]

	a = kinda_slow(seq[0 : len(seq)-1])
	b = kinda_slow(seq[1: len(seq)])
	Table[seq] = max(a,b)
	# return max(a, b)
	return Table[seq]

###########################################
# 8
# •	Pair up the elements in the list arbitrarily.
# •	Look at each pair.  If two elements are different, discard both of them.  If they are the same, keep just one of them.
# •	Use the same strategy for the remaining elements.

def majority(L):
	if len(L)==0:
		return None
	if len(L)==1:
		return L[0]
	if len(L)%2 == 1:
		odd_item = L.pop()

	count = 0
	for x in L:
		if x==odd_item:
			count++
	if count > len(>)/2:
		return odd_item

	A = []
	# pair items i and i+1.
	for i in range(0, len(L), 2):
		if L[i] == L[i+1]:
			A.append(L[i])
	m = majority(A)
	return m








