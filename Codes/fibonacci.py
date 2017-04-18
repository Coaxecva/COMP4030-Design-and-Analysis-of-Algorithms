
Table = {}
# Use Table[x] to store the output of f(x)
# When we compute f(x), first before we do anything,
# check to see if x is in Table.
# 1. if x is in Table, simple return Table[x]
# 2. else, do whatever f does to compute f(x).  Before we return the output, store
# the output into Table[x].

# fib(0) = 0, fib(1) = 1, fib(n) = fib(n-1) + fib(n-2)
def fib(n):
	if n in Table:
		return Table[n]
	if n < 2:
		output = n
	else:
		output = fib(n-1) + fib(n-2)
	Table[n] = output
	return output

for i in range(1000):
	print(i, fib(i))

