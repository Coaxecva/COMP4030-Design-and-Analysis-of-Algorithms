#Problem 1
def restorable(string, dictionary):
	if len(string) == 0:
		return True
	if string in dictionary:
		return True
	for i in range(len(string),-1,-1):
		u = string[0:i]
		v = string[i:len(string)]
		if v in dictionary:
			for j in range(len(u),-1,-1):
				y = u[j:len(u)]
				x = u[0:j]
				if x in dictionary or y in dictionary:
					return True
	return False

myDictionary = {"this", "that", "is", "are", "a", "cat", "dog"}

#Problem 2
# "thisandacat" is an example of a string that will 
#print(restorable("thisandcat",myDictionary))

#Problem 3
# T(n) = (1/2)(n^2)
# Theta(n) = n^2

#Problem 4
def restorable_recur(string, dictionary):
	if len(string) == 0:
		return True
	if string in dictionary:
		return True
	for i in range(len(string), -1, -1):
		u = string[0:i]
		v = string[i:len(string)]
		if v in dictionary:
			return restorable_recur(u, dictionary)
	return False

#Problem 5
def is_restorable(text,D):
	if len(text) == 0:
		return True
	R = [False] * len(text)
	foundIt = 0
	for i in range(0,len(text)):
		for j in range(0,i+1):
			u = text[0:j]
			v = text[j:i+1]
			if v in D:
				if i-foundIt <= len(v):
					R[i] = True
					foundIt = i
	return R[len(text)-1]


print(myDictionary)
borked = "thisandcat"
good = "thisisthatcat"
print("Testing...")
print("Problem 1")
print(borked, restorable(borked,myDictionary))
print(good, restorable(good,myDictionary))
print("Problem 4")
print(borked, restorable_recur(borked,myDictionary))
print(good, restorable_recur(good,myDictionary))
print("Problem 5")
print(borked, is_restorable(borked,myDictionary))
print(good, is_restorable(good,myDictionary))
