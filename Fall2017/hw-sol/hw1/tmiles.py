# *censored* Comp 4030 Assignment 1

import random

#------------------------------------------------
def get_list(n):
	L = list(range(n))
	for i in range (len(L)):
		L[i]=2
	L[randint(0, n-1)]=1.5
	print('The array is:')
	print(L)
	print('The number of items is '+str(len(L))+'.')
	return L

#------------------------------------------------
def iterative(L):
 if len(L)==1:
 	return 0
 for k in range (len(L)-1):
 	left=L[k]
 	right=L[k+1]
 	if left<right:
 		return k
 return k+1
 #------------------------------------------------
print('Iterative Set')
from random import *
x=randint(1, 100)
test=get_list(x)
z=iterative(test)
print('The value of the fake item at array location ' +str(z)+' is: '+str(test[z])+'.')
test1=get_list(1)
z=iterative(test1)
print('The value of the fake item at array location ' +str(z)+' is:'+str(test1[z])+'.')
test2=get_list(100)
z=iterative(test2)
print('The value of the fake item at array location ' +str(z)+' is:'+str(test2[z])+'.')
test3=get_list(20)
z=iterative(test3)
print('The value of the fake item at array location ' +str(z)+' is:'+str(test3[z])+'.')
test4=get_list(33)
z=iterative(test4)
print('The value of the fake item at array location ' +str(z)+' is:'+str(test4[z])+'.')
print('Iterative Set End')

#------------------------------------------------
def bytwo(L, first, last):
	middle=(first+last)//2
	left=L[0:middle]
	right=L[middle:middle*2]
	if sum(left)<sum(right):
		if len(L)==2:
			return left[0]
		else:
			return bytwo(left, 0, len(left))
	elif sum(left)>sum(right):
		if len(L)==2:
			return right[0]
		return bytwo(right, 0, len(right))
	elif sum(left)==sum(right):
		remainder=L[last-1]
		print('Returning Remainder')
		return remainder
 #------------------------------------------------
print('By 2 Set')
from random import *
test0=get_list(4)
z=bytwo(test0, 0, len(test0))
print('The value of the fake item is: '+str(z)+'.')
x=randint(1, 100)
test=get_list(x)
z=bytwo(test, 0, len(test))
print('The value of the fake item is: '+str(z)+'.')
test1=get_list(1)
z=bytwo(test1, 0, len(test1))
print('The value of the fake item is: '+str(z)+'.')
test2=get_list(100)
z=bytwo(test2, 0, len(test2))
print('The value of the fake item is: '+str(z)+'.')
test3=get_list(20)
z=bytwo(test3, 0, len(test3))
print('The value of the fake item is: '+str(z)+'.')
test4=get_list(33)
z=bytwo(test4, 0, len(test4))
print('The value of the fake item is: '+str(z)+'.')
print('By 2 Set End')

#------------------------------------------------
def bythree(L, first, last):
	thirding=len(L)//3
	left=L[0:thirding]
	middle=L[thirding:thirding*2]
	right=L[thirding*2:thirding*3]
	if sum(left)<sum(right) and sum(left)<sum(middle):
		if len(left)==1:
			return left[0]
		return bythree(left, 0, len(left))
	elif sum(right)<sum(left) and sum(right)<sum(middle):
		if len(right)==1:
			return right[0]
		return bythree(right, 0, len(right))
	elif sum(middle)<sum(right) and sum(middle)<sum(left):
		if len(middle)==1:
			return middle[0]
		return bythree(middle, 0, len(middle))
	elif sum(left)==sum(right)==sum(middle):
		remainder=len(L)%3
		if remainder==1:
			return L[last-1]
		if remainder ==2:
			if L[last-2]<L[last-1]:
				return L[last-2]
			else:
				return L[last-1]

 #------------------------------------------------
print('By 3 Set')
from random import *
test0=get_list(4)
z=bythree(test0, 0, len(test0))
print('The value of the fake item is: '+str(z)+'.')
x=randint(1, 100)
test=get_list(x)
z=bythree(test, 0, len(test))
print('The value of the fake item is: '+str(z)+'.')
test1=get_list(1)
z=bythree(test1, 0, len(test1))
print('The value of the fake item is: '+str(z)+'.')
test2=get_list(100)
z=bythree(test2, 0, len(test2))
print('The value of the fake item is: '+str(z)+'.')
test3=get_list(20)
z=bythree(test3, 0, len(test3))
print('The value of the fake item is: '+str(z)+'.')
test4=get_list(33)
z=bythree(test4, 0, len(test4))
print('The value of the fake item is: '+str(z)+'.')
print('By 3 Set End')
