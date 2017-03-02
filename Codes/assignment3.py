'''

4. Explain why n^5 + 2n^2 is in Theta(n^5).
We have to show this function is both in O(n^5) and Omega(n^5).
n^5 + 2n^2 <= n^5 + 2n^5 = 3n^5 for all n > 1.  (c = 3).  Function is in O(n^5).
n^5 + 2n^2 >= n^5 for all n > 1.  Function is in Omega(n^5).

5. 
def find_cats(L, idx, output):
	if idx < len(L):
		if "cat" in L[idx]:
			output.append(L[idx])
			find_cats(L, idx+1, output)
		else:
			find_cats(L, idx+1, output)

A = []
find_cats(L, 0, A)

Why is it that after these executions A is a list of all strings that contain "cats".

Answer:
(1) If L is empty (irreducible case), then A is empty. This is correct behavior.
Function is correct for the base case/irreducible case.

(2) 
Let's say L has k items.  (Not useful.)
Let k be the number of items between idx and the last item.  (More accurate)
Two cases:
(i)  If "cats" is L[idx], the function appends L[idx] to output.  There are k-1 items
between idx+1 and the rest.  So if find_cats returns the correct answer (it correctly 
appends all strings containing "cats" from idx+1) with idx+1, the the function is correct.

(ii)  If "cats" is not L[idx], then if find_cats returns the correct answer (it correctly 
appends all strings containing "cats" from idx+1) with idx+1, the the function is correct.
'''


# Q1
# Q3. r.t. complexity is in Theta(n). Space complexity is in Theta(n).
def Split(A):
	left, right = [], []
	first = A.pop(0)   # r.t is Theta(1)
	for item in A:
		if item <= first:
			left.append(item)
		else:
			right.append(item)
	return left, first, right

print(Split([10, 7, 20, 3, 0, 9, 15, 7, 18, 50]))   # output: [7,3,0,9,7,10,20,15,18,50]

# Q2
def Split2():
	pass

def qsort(A):
	if len(A) <= 1:
		return A
	# [10, 7, 20, 3, 0, 9, 15, 7, 18, 50] ---> [7,3,0,9,7],10,[20,15,18,50]
	left, first, right = Split(A)
	return qsort(left) + [first] + qsort(right)


def qsort2(A, left, right):
	if left < right:
		i = Split2(A)
		qsort2(A, left, i-1)
		qsort2(A, i+1, right)


L = [10, 7, 20, 3, 0, 9, 15, 7, 18, 50]
qsort2(L, 0, len(L)-1) 




