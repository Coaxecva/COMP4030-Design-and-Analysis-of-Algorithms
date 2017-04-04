# assingment 5

# 1a. look at all possible "intervals" and maintain the max sum.
# running time is <= c * n * n * n.  O(n^3)
def maxsum1a(L):
	# how to enumerate through all intervals of L?
	tmp_max = L[0]
	for i in range(len(L)):
		for j in range(i, len(L)):
			# t = sum of the current interval
			t = 0
			for k in range(i,j+1):
				t += L[k]
			if t > tmp_max:
				tmp_max = t
	return tmp_max

L = [10,-20,5,-3,7,8,-10,4]

# 1b. O(n^2)
def maxsum1b(L):
	# how to enumerate through all intervals of L?
	tmp_max = L[0]
	for i in range(len(L)):
		running_max = 0
		for j in range(i, len(L)):
			running_max += L[j]
			if tmp_max < running_max:
				tmp_max = running_max
	return tmp_max

# 1c. O(n log n)
# T(n) = n + 2*T(n/2).  Running time is Theta(n log n)
# 
def maxsum1c(L, left, right):
	if left==right:
		return L[left]
	mid = (left+right)//2
	left_sum = maxsum1c(L, left, mid)
	right_sum = maxsum1c(L, mid+1, right)
	middle_sum = left_mid_sum(L, left, mid-1) + right_mid_sum(L, mid, right)
	return max(left_sum, right_sum, middle_sum)

def right_mid_sum(L, mid, right):
	cur_max = L[mid]
	run_max = 0
	for i in range(mid, right+1):
		run_max += L[i]
		if cur_max < run_max:
			cur_max = run_max
	return cur_max

def left_mid_sum(L, left, mid_minus_one):
	if left == mid_minus_one:
		return L[left]

	cur_max = L[mid_minus_one]
	run_max = 0
	for i in range(mid_minus_one, left-1, -1):
		run_max += L[i]
		if cur_max < run_max:
			cur_max = run_max
	return cur_max


print( maxsum1b(L) )
print( maxsum1c(L, 0, len(L)-1) )

