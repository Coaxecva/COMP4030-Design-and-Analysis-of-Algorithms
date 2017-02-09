
def reverse(L):
	# have a temp list
	# for each item of L from left to right:
	# 	prepend item to temp
	# return temp
	temp = []
	for item in L:
		# temp.insert(0,item)
		temp = [item] + temp
	return temp

def is_palindrome(s):
	# lower case everything
	# have a counter start at len(s) - 1, another starts at 0
	# check first last characters equal, if yes move the counters
	# first, last = 0, len(s)-1
	# while last > first:
	# 	if s[first] == s[last]:
	# 		first += 1
	# 		last -= 1
	# 	else:
	# 		return False
	# return True

	# set a to False
	# if input is the same as reverse(input): yes then change a to True
	# return a
	# r = s[::-1]
	# if s == r:
	# 	return True
	# else:
	# 	return False				
	return reverse(s) == list(s)

# a = "Racecar"
# print(reverse(a), a)
print(is_palindrome("racecar"))
print(is_palindrome("race car"))
print(is_palindrome("ra ar"))


'''
Question 3
T(n) = n^2 + 2n is in O(n^2). Why?  n^2 + 2n <= n^2 + 2n^2 = 3n^2, for n > 1.
So, T(n) <= 3n^2, for n > 1.  c = 3.

T(n) = 5n^3 + 1 <= 5n^3 + n^3 <= 6n^3, for all n > 1.  c = 6.

T(n) = 10n+3n^2+10 <= 10n^2 + 3n^2 + 10n^2 = 23n^2 for n > 1.
T(n) <= 23n^2 for all n > 1.  We find c to be 23.

Is T(n) = 5n^2 - 20n in Omega(n)?  Yes.
Why?  because T(n) = 5n^2 - 20n >= n, for n > 5.
5n^2 >= 21n
n >= 21/5
Question 4
def foo(L):
	sum = 0
	for x in L:
		sum += x*x
	return sum

Running time is in O(n)


T(n) = 2n^2 + 2 is in Theta(n^2). Why?
Because 2n^2 + 2 >= n^2 when n>1.  (in Omega(n^2))
and 2n^2 + 2 <= 2n^2 + 2n^2 = 4n^2 when n>1  (in O(n^2))


Question 5:
def bar(L):
	sum = 0
	for x in L:
		for y in L:
			sum += x*x + y*y
	for z in L+L:
		sum += z*z*z
	return sum

Running time is in O(n^2 + 2n)
Running time is in O(n^2)
'''

def foo(L):
	if len(L) <= 1:
		return True
	else:
		return L[0]==L[-1] and foo(L[1:-1])

'''
Hypothesis: foo returns True if L is a palindrome.
Is foo correct for smallest cases?  Yes because if L has zero or 1 element,
the correct answer is True.

Let's say L has k items.
Assume that foo is correct on lists with fewer than k items.
Then, foo(L[1:-1]) is true only if the sublist of L starting from index 1 and -1 
is a palindrome.  Then, the answer is correct only if first and last items are the same
and the sublist is a palindrome.

'''
print( foo([1,2,3,4]) )