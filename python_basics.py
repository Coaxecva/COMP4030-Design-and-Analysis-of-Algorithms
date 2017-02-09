# variables, assignment
# dynamic typing
x = 20

# if-then-else
if x < 5:
	x = x + 1
	print("this is x:", x)
elif x < 15:
	x = x + 1
	print(x, "is less than 15")
else:
	x = x + 1
	print(x, "is greater than 15.")

# for loop
for i in range(10):
	x = x + i
	# print(i, x)

# function def with default argument, z is a tuple of arguments
def foo(a, b=10, *z):
	c = a + b
	print("z:",z)
	return c


# print("test foo", foo(1,5))
# print("test foo", foo(1))

x = 3.14
print(x, type(x))

# lists and enumeration of lists
y = [1,2,3,"hello"]
# for item in y:
# 	print(item)

# for i, item in enumerate(y):
# 	print(i, item, y[i])

print("length of y is", len(y))
print("range of len(y)", range(len(y)), list(range(len(y))))
for i in range(len(y)):
	print(i, y[i])


# strings
x = 'hello'
for c in x:
	print(c)

# dictionaries
numbers = {}
numbers["john"] = 2783
numbers["mary"] = 3892

print(numbers)
print(numbers["john"])