
# input: sorted list of numbers L, x is a number.
# output: True if x is in L, False if x is not in L
# T(n) = c + T(n/2) + n/2, is in Theta(n).
def Search(L, x):
	# compare x to the middle element.  If they're the same, return True
	# If x < middle element, SOLVE SAME PROBLEM on the left half.
	# Else, SOLVE SAME PROBLEM on the right half.
	if len(L)<1:
		return False
	if x == L[len(L)//2]:
		return True
	if x < L[len(L)//2]:
		return Search(L[0:len(L)//2], x)
	else:
		return Search(L[len(L)//2 + 1:], x)

# Running time: T(n) = c + T(n/2).  So, T(n) is in Theta(log n)
def Search2(L, x, left, right):
	if left > right:
		return False
	middle = (left+right)//2
	if x == L[middle]:
		return True
	if x < L[middle]:
		return Search2(L, x, left, middle-1)
	else:
		return Search2(L, x, middle+1, right)




print( Search([1,3,5,7,9,11,13,15,21,100], 1) )
L=[1,3,5,7,9,11,13,15,21,100]
print( Search2(L, 1, 0, len(L)-1) )

