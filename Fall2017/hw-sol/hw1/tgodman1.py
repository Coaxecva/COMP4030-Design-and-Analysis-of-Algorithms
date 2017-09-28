'''
*censored*
Assignment 1
Go to line 46 to see my code for the assignment.
Test cases will be shown if this script is executed.
'''

import random

#----------------------------------------------------------
# What does this function do?
#----------------------------------------------------------
def generate_coins(n=27):
	coins = [2]*n
	coins[ random.choice(range(n)) ] = 1
	return coins

#----------------------------------------------------------
# What does this function do?
# Input: A, B are lists
# Output: 0 if A and B have the same weight.
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

def simple_detection(C):
	# print out all pairs of coins in C
	for i in range(0, len(C)):
		for j in range(i+1, len(C)):
			A = [C[i]]
			B = [C[j]]
			#print(scale(A,B))
			if scale(A,B) == 1:
				print(C[j], 'is fake at index', j)
				return
			elif scale(A,B) == -1:
				print(C[i], 'is fake at index', i)
				return

#----------------------------------------------------------
'''
*censored*
Assignment 1

Test cases will be shown if this script is executed.

        Problem 1:
        simple_detection (shown directly above) is code from the whiteboard
                in class, which the students were told would be accaptable
                as an answer.

        Problem 2:
        detection_rec_two is my solution to Assignment 1, problem 2

        Problem 3:
        detection_rec_three is my solution to Assignemnt 1, problem 3
'''
def detection_rec_two(inlist, refpoint=0):
        #The line immediately below this comment does a recursive split
        tosplit = split_main_two(inlist)
        #The rest of this recursively searches the output of split_main for fake coins
        while len(tosplit) > 1:
                temp = 0
                for i in range(0,len(tosplit)-1):
                        for j in range(len(tosplit[i])):
                                temp+=1
                #Give the next instance of this function a portion to work on, recursively.
                detection_rec_two(tosplit.pop(),temp)
                                
        if len(tosplit) == 1:
                for i in range(0, len(tosplit[0])):
                        for j in range(i+1, len(tosplit[0])):
                                A = [tosplit[0][i]]
                                B = [tosplit[0][j]]
                                if scale(A,B) == 1:
                                        print(tosplit[0][j], 'is fake at index', refpoint+j)
                                        return
                                elif scale(A,B) == -1:
                                        print(tosplit[0][i], 'is fake at index', refpoint+i)
                                        return

def detection_rec_three(inlist, refpoint=0):
        #The line immediately below this comment does a recursive split of the input list.
        tosplit = split_main_three(inlist)
        #The rest of this recursively searches the output of split_main for fake coins.
        while len(tosplit) > 1:
                temp = 0
                for i in range(0,len(tosplit)-1):
                        for j in range(len(tosplit[i])):
                                temp+=1
                #Give the next instance of this function a portion to work on, recursively.
                detection_rec_three(tosplit.pop(),temp)

        #Once all of the other recursions of this function have started, search for fake coins.                        
        if len(tosplit) == 1:
                for i in range(0, len(tosplit[0])):
                        for j in range(i+1, len(tosplit[0])):
                                A = [tosplit[0][i]]
                                B = [tosplit[0][j]]
                                if scale(A,B) == 1:
                                        print(tosplit[0][j], 'is fake at index', refpoint+j)
                                        return
                                elif scale(A,B) == -1:
                                        print(tosplit[0][i], 'is fake at index', refpoint+i)
                                        return

'''
The functions below are helper functions.
split_main_two & split_main_three recursively split a list into two or three parts, respectively.
'''
                
def split_main_two(temp):
        #A recursive splitting algorithm
        parts=[]
        if len(temp) > 3:
                #Split input into a list of 2 smaller lists
                parts = split_init(temp,2)
                for i in reversed(range(len(parts))):
                        if len(parts[i]) > 3:
                                #recurse
                                temp2 = split_main_two(parts.pop(i))
                                insertions = 0
                                #Insert the split lists back where they belong
                                for j in range(len(temp2)):
                                        parts.insert(i+insertions,temp2[j])
                                        insertions+=1
        else:
                parts.append(temp)
                                        
        return parts

def split_main_three(temp):
        #A recursive splitting algorithm
        parts=[]
        if len(temp) > 5:
                #Split input into a list of 3 smaller lists
                parts = split_init(temp,3)
                for i in reversed(range(len(parts))):
                        if len(parts[i]) > 5:
                                #recurse
                                temp2 = split_main_three(parts.pop(i))
                                insertions = 0
                                #Insert the split lists back where they belong
                                for j in range(len(temp2)):
                                        parts.insert(i+insertions,temp2[j])
                                        insertions+=1
        else:
                parts.append(temp)
                                        
        return parts

def split_init(list_full, size):
        #Split a list into 2 or 3 smaller lists
        length = int(len(list_full)/size)
                
        out1 = []
        out2 = []
        out3 = []
        result = []
        
        for i in range(0,length):
                out1.append(list_full[i])
        result.append(out1)
        if size == 3:
                for i in range(length,2*length):
                        out2.append(list_full[i])
                for i in range(2*length,len(list_full)):
                        out3.append(list_full[i])
                result.append(out2)
                result.append(out3)
        if size == 2:
                for i in range(length,len(list_full)):
                        out2.append(list_full[i])
                result.append(out2)
        return result

'''
Test cases
'''


coins = generate_coins(10)
print(coins)

simple_detection(coins)
detection_rec_two(coins)
detection_rec_three(coins)
