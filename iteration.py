# 3. write a python function that takes a list as input
# and returns the list containing only even numbers.
import time
start_time = time.time()

def is_odd(x):
	return x%2 == 1

def is_even(x):
	return x%2 == 0

def filter(L, criterion):
	selected = []
	# select items in L
	for item in L:
		if criterion(item) == True:
			selected.append(item)
	return selected

print( filter([1,2,3,4,5,6,7], is_odd) )
print( filter([1,2,3,4,5,6,7], is_even) )
print( filter([1,2,3,4,5,6,7], lambda x: x%5==0) )

divisible_by_5 = lambda x: x%5 == 0
print( filter([1,2,3,4,5,6,7], divisible_by_5) )

# exercise: write a function that takes a list L as input, and returns
# another list consisting of numbers in L multiplied by 2.

def double(L):
	selected = []
	for item in L:
		selected.append(item*2)
	return selected


# print( double([1,2,3,4,5]) )


# exercise: write a function that takes a list L and a function f as inputs
# and returns a list that applies f to each element of L.

def map(L, f):
	s = []
	for item in L:
		s.append(f(item))
	return s


print( "double", map([1,2,3,4,5], lambda x: x*2) )   # output: [2,4,6,8,10]
print( "increment", map([1,2,3,4,5], lambda x: x+1) )   # output: [2,3,4,5,6]


A = [ "the cat runs.", "dogs are nicer.", "cats!", "I like chicken."]

# exercise: write a function that takes a list of strings and returns a list
# that contains the number of characters in strings that have "cat" in them.

def find_cats(L):
	s = []
	for item in L:
		if "cat" in item:
			s.append(len(item))
	return s

print( find_cats(A) )   # output: [13, 15]
print( map(filter(A, lambda item: "cat" in item), lambda item: (item.capitalize(), len(item))) )
time.sleep(2.2)
print("running time", time.time() - start_time)