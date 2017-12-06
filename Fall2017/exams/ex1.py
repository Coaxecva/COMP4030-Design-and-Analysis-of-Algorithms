
# Problem 2
def even_numbers(L):
	output = []
	for x in L:
		if x%2==0:
			output.append(x)
	return output

# Problem 3
# Running time is in O(n), where n is length of L.

# Problem 4
def is_even(L):
	if L==[]:
		return True
	else:
		first = L[0]
		rest_of_L = L[1:]
		return not is_even(rest_of_L):

# Problem 5
# Running time of is_even is in O(n).

# Problem 6
def depth(node):
	if node==None:
		return 0
	left = node.LeftTree
	right = node.RightTree
	return 1 + max(depth(left), depth(right))

# Problem 7
'''
T(1) = 1          <------ SMALLEST INPUT SIZE.
T(n) = n + 4T(n/4)
T(n) = n + 4(n/4 + 4T(n/4^2)) = 2n + 4^2T(n/4^2)
T(n) = 2n + 4^2 * (n/4^2 + 4T(n/4^3))
T(n) = 3n + 4^3*T(n/4^3)

After k steps:
T(n) = kn + 4^k * T(n/4^k)

We stop when n/4^k is 1.  (Line 35)

n/4^k = 1 --> n = 4^k --> k = log_4(n)

T(n) = n * log_4(n) + T(1)
Therefore, T(n) is in Theta(n log n)
'''





