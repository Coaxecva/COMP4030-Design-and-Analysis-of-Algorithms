'''
Michael Ciskowski
Assignment 1
COMP 4030
9/7/2017
'''

import random

#----------------------------------------------------------
# What does this function do?
#----------------------------------------------------------
#default value of 27, will use value of n if passed in
def generate_coins(n=27):
	#List of n number of value [x]
	coins = [2]*n

	#select random index and set element at index to 1
	coins[ random.choice(range(n)) ] = 1.5
	return coins

#----------------------------------------------------------
# What does this function do?
# Input: A, B are lists
# Output: 00 if A and B have the same weight
# -1 if B is heavier than A
# 1 otherwise.
#----------------------------------------------------------
def scale(A, B):
	if sum(A)==sum(B):
		return 0
	elif sum(A) < sum(B):
		return -1
	else:
		return 1


#----------------------------------------------------------
# 1. Iterative algorithm to find the fake coin
#----------------------------------------------------------
def iterative(C):
	# Check if there is only one coin
	if len(C) == 1:
		return C[0]
	# Iterate over the array C
	for i in range(1, len(C)):
		# A starts at index 0, increments by 1
		# is compared to B which starts at index 1, increments by 1
		A = [C[i - 1]]
		B = [C[i]]

		# If the left index is heavier
		if scale(A,B) == 1:
			#print('Iterative found fake coin at index', i)
			return C[i]
		# If the right index is heavier
		elif scale(A,B) == -1:
			#print('Iterative found fake coin at index', i-1)
			return C[i-1]


#----------------------------------------------------------
# Helper for recursive methods
# Splits the array in half if 2 is a param, or thirds
# if 3 is a param
#----------------------------------------------------------
def split(list, split):
	# Splits the array into two, equal-sized arrays
	if split == 2:
		half = len(list)/2
		return list[:int(half)], list[int(half):]
	# Splits the array into three, equal-sized arrays
	elif split == 3:
		first_third = len(list)/3
		second_third = 2*len(list)/3
		return list[:int(first_third)], list[int(first_third):int(second_third)], list[int(second_third):]


#----------------------------------------------------------
# 2. Recursive algorithm by dividing into two groups
#----------------------------------------------------------
def recursive_half(coinList):

	# If the list is even length, split it in half
	if len(coinList)%2 == 0:
		A = split(coinList, 2)[0]
		B = split(coinList, 2)[1]

	# Odd length lists have last element removed before being split
	else:
		oddCoin = coinList[len(coinList)-1]
		coinList = coinList[:len(coinList)-1]
		A = split(coinList, 2)[0]
		B = split(coinList, 2)[1]
		
	# check if removed item is the fake coin
	if scale(A,B) == 0:
		return oddCoin

	# If A is lighter than B
	elif scale(A,B) == -1:
		return recursive_half(A)	

	# If B is lighter than A
	elif scale(A,B) == 1:
		return recursive_half(B)


#----------------------------------------------------------
# 3. Recursive algorithm by dividing into three groups
# First if-elif block determines if the size of the list is 
# divisible by 3.
# If the size%3 = 1, remove the last coin for balance,
# if the size%3 = 2, remove the last two coins for balance.
#----------------------------------------------------------
def recursive_third(coinList):

	#If the size of the list is divisible by 3, split the list into thirds
	if len(coinList)%3 == 0:
		A = split(coinList, 3)[0]
		B = split(coinList, 3)[1]
		C = split(coinList, 3)[2]

	#If the size%3 = 1, remove the last coin for balance and split into thirds
	elif len(coinList)%3 == 1:
		oddCoin = coinList[len(coinList)-1]
		coinList = coinList[:len(coinList)-1]
		A = split(coinList, 3)[0]
		B = split(coinList, 3)[1]
		C = split(coinList, 3)[2]
	
	# If the size%3 = 2, remove the last two coins for balance,
	# compare those two coins, and split into thirds if neither
	# oddcoin is fake
	elif len(coinList)%3 == 2:
		oddCoinOne = [coinList[len(coinList)-1]]
		oddCoinTwo = [coinList[len(coinList)-2]]
		if scale(oddCoinOne, oddCoinTwo) == -1:
			return oddCoinOne[0]
		elif scale(oddCoinOne, oddCoinTwo) == 1:
			return oddCoinTwo[0]

		coinList = coinList[:len(coinList)-2]
		A = split(coinList, 3)[0]
		B = split(coinList, 3)[1]
		C = split(coinList, 3)[2]
		
	# If all three lists are the same weight
	if scale(A,B) == 0 and scale(A,C) == 0:
		return oddCoin

	# If A and B are the same weight, C is lightest
	elif scale(A,B) == 0:
		return recursive_third(C)

	# If A is lighter than B=C
	elif scale(A,B) == -1:
		return recursive_third(A)

	# If B is lighter than A=C
	elif scale(A,B) == 1:
		return recursive_third(B)
