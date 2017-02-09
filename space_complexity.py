# T(n) - running time complexity
# S(n) - space complexity (RAM)

# T(n) = c*n + b
# T(n) is in O(n), Omega(n), Theta(n)
# S(n) = c.  S(n) is O(1)
def foo(L):
	s = 0
	for x in L:
		s += x*x
	return s


foo([1,2,3,4,5])