'''
David Reddick
Comp 4030
Assignment 8
'''

def restore_text_1(t,lib):
	restore_flag = False
	index_start = len(t)-1
	index_end = len(t)
	test = t[index_start:index_end]
	while index_start >= 0:
		try:
			lib.index(test)
			index_end = index_start
			index_start -= 1
			test = t[index_start:index_end]
			restore_flag = True
		except ValueError:
			index_start -= 1
			test = t[index_start:index_end]
			restore_flag = False

	return restore_flag

def test_1(T,key):
	if restore_text_1(T, key):
		print("restorable")
	else:
		print("not restorable")

def restore_text_4(t,lib,index_start,index_end,good_start):
	restore_flag = False
	test = t[index_start:index_end]
	try:
		lib.index(test)
		good_start = index_start
		if good_start == 0:
			restore_flag = True
			return restore_flag
		if index_end-max_element_len < index_start:
			index_start =  index_end-max_element_len
		elif index_end-max_element_len < 0:
			index_start = 0
		restore_flag = restore_text_4(t,lib,index_start,index_end,good_start)
	except ValueError:
		if index_start != index_end-max_element_len:
			index_start -= 1
			test = t[index_start:index_end]
			restore_flag = restore_text_4(t,lib,index_start,index_end,good_start)
		else:
			if good_start >= index_end:
				return False
			index_end = good_start
			index_start = index_end-1;
			restore_flag = restore_text_4(t,lib,index_start,index_end,good_start)

	return restore_flag

def test_4(T,key):
	start = len(T)-1
	end = len(T)
	good_start = start
	if restore_text_4(T, key, start, end, good_start):
		print("restorable")
	else:
		print("not restorable")

def is_restorable(t,lib):
	R = [False]*len(t)
	true_i = 0
	for i in range(0,len(t)):
		for j in range(0,i+1):
			u = t[0:j+true_i]
			v = t[j+true_i:i+1]
			try:
				lib.index(v)
				if i-true_i <= len(v):
					R[i] = True
					true_i = i
			except ValueError:
				R[i]=R[i]
	if R[len(t)-1]:
		return True
	else:
		return False


def test_5(T,key):
	if is_restorable(T, key):
		print("restorable")
	else:
		print("not restorable")

# Question 1
# examples that work
T_restorable = 'thatisacatdo'
T_not_restorable = 'thatwasacat'
key = ['this', 'that', 'is', 'are', 'a', 'cat', 'dog']
print("Working for Question 1")
test_1(T_restorable,key)
test_1(T_not_restorable,key)

# Question 2
# example that fails because key="this" ends with key="is"
print("Exception for Question 1 that does not work")
T_messed_up = 'thisisacat'
test_1(T_messed_up,key)

'''
Question 3:
T(n) = cn => Theta(n) for text string of length n
'''

# Question 4
# example that failed in question 1 because key="this" ended with key="is"
print("Exception from Question 1 that now works in Question 4")
max_element_len = len(max(key, key=len))
test_4(T_messed_up,key)
print("String from Question 1 that was not restorable now in Question 4")
test_4(T_not_restorable,key)

# Question 5
print("Implimentation of Question 5 for both restorable and not restorable")
test_5(T_restorable,key)
test_5(T_not_restorable,key)