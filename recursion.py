
# what does this program do?
def foo(L):
	s = []
	for x in L:
		if x%2 == 0:
			s = s + [x]
	return s

# Claim: bar returns the number of items of L.
def bar(L):
	if len(L) == 0:   # smallest input size, bar is obviously correct.
		return 0
	return 1 + bar(L[1:])  
	# if assume bar's correct for input size k-1, then return value is 1 + (k-1). 
	# So, bar is correct for input size k because k is the number of items in L.

# Testing
print(bar([0,1,2,3,4,5,6,7]) == 8)
print(bar([]) == 0)

# Tracing
bar([0,1,2,3,4,5])
1 + bar([1,2,3,4,5])
1 + 1 + bar([2,3,4,5])
1 + 1 + 1 + bar([3,4,5])
1 + 1 + 1 + 1 + bar([4,5])
1 + 1 + 1 + 1 + 1 + bar([5])
1 + 1 + 1 + 1 + 1 + 1 + bar([])
1 + 1 + 1 + 1 + 1 + 1 + 0 
6

# Induction
'''
(1) Verify correctness of the function with smallest (irreducible) inputs.
(2) [Let's say input size is k]
Assume the program works correctly with input sizes less than k.
Use this assumption and the logic of the program to show/argue that it also works for input size k.

In discrete math,
To prove f is correct. (1) prove f(0) is correct, (2) assume f(0), f(1), ..., f(k-1) are correct.
then prove f(k) is correct.

Prove that f(n) = 1 + 2 + ... + n = n(n+1)/2

(1) f(1)= 1 = 1*2/2.  The formula is correct for smallest case (n=1).
(2) Given this: 1 + 2 + ... + (k-1) + k
If we assume that f(k-1) is correct, then 1+2 + ... + (k-1) = (k-1)*k/2
This means f(k) = 1+2+...+(k-1)+k = (k-1)*k/2 + 2*k/2 = k*(k-1+2)/2 = k(k+1)/2
And this means f(k) is also correct.

Conclusion:  formula f is correct for all values of n >= 1.
Logic:  After we go through these 2 steps:
Is f(1) correct? Yes.
Is f(2) correct? Yes because assume f(1) is correct, 
we actually used this assumption to prove that f(2) is correct.
Is f(3) correct? Yes because if f(2) is correct, 
then we prove (lines 46-48) that f(3) is also correct.
'''
# c returns ?
def c(L):
	if len(L) == 0:
		return 0
	else:
		return L[0] + c(L[1:])
# L has k items.  Line 66 returns "L[0] plus the sum of the rest of the items of L".
# Therefore, c is correct for input size k, 
# based on the assumption it is correct for input size less than k.

print(c[0,1,2,3,4,5,6])



