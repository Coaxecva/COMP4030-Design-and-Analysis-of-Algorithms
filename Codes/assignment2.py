
'''
Q3. Explain why 
(i) 10n + 2n^2 is in O(n^2)

[By definition, this means: 10n + 2n^2 <= c*n^2 for all large values of n.]
Answer:
10n + 2n^2 <= 10n^2 + 2n^2 = 12n^2 for n>1.
Therefore, we found c to be 12.

(ii) 10n + 2n^2 is in Omega(n^2)
[By definition, this means: 10n + 2n^2 >= c*n^2 for all large values of n.]
Answer:
10n + 2n^2 >= n^2 for n>1.  c is 1.

Q4. Answer: 
n log n.  FALSE.
c * n log n.  CORRECT   
O(n + log n).  FALSE
O(n^2).  CORRECT
O(n log n).  CORRECT (better than the others)
Theta(n log n).  

Q5. 
(1) Smallest input size is when L has 0 element.  The program is correct if L
has 0 element. (first two lines)
(2) Let's say L has k elements. Then, L[1:] has k-1 elements.
So, if we assume the function add is correct for fewer than k elements,
then add(L[1:]) returns the sum of all elements starting from the second element.
Then, add is correct if L has k elements because L[0] + (sum of all elements starting
from the second) is the sum of all elements.

Q6.
Let you do this at home.

'''

# Q2
A = [1,3,4,5,8,20]
B = [0,15,30,40]    # [0] + 
def rec_merge(A,B):
	# smallest input sizes
	if len(A)==0:
		return B
	if len(B)==0:
		return A
	# A and B are not empty
	if A[0] > B[0]:
		return [B[0]] + rec_merge(A, B[1:])
	else:
		return [A[0]] + rec_merge(A[1:], B)

# Q1
def iter_merge2(A,B):
	C = A + B
	return sorted(C)

# Time complexity: O(n+m), Omega(n+m), Theta(n+m)
# Space complexity: Theta(n+m)
def iter_merge(A,B):
	C = []
	a, b = 0, 0
	while a < len(A) and b < len(B):
		if A[a] < B[b]:
			C.append(A[a])
			a += 1
		else:
			C.append(B[b])
			b += 1
	if a==len(A):
		C = C + B[b:]
	else:
		C = C + A[a:]
	return C


# Running time: T(n) = c + T(n-1) # T(n) is the running time of add when L has n elements. 
# When L has n-1 elements, the running time is T(n-1) 
def add(L):
	if len(L)==0:         
		return 0     
	return L[0] + add(L[1:])
