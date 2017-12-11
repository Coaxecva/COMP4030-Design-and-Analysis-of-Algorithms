
import random
#-------------------------------------------------
def generate_coins(n=27, seed=None):
	if seed is not None:
		random.seed(seed)
	coins = [2]*n
	coins[ random.choice(range(n)) ] = 1.9
	return coins
#-------------------------------------------------
def scale(A, B):
	if sum(A)==sum(B):
		return 0
	elif sum(A) < sum(B):
		return -1
	else:
		return 1
#-------------------------------------------------
# 1.
def simple(coins):
	if len(coins) > 1:
		for i in range(1, len(coins)):
			if scale([coins[i-1]], [coins[i]]) == -1:
				return coins[i-1]
			elif scale([coins[i-1]], [coins[i]]) == 1:
				return coins[i]
	print('There is no fake coin.')
	return None
#-------------------------------------------------
# 2. detect the fake coin by dividing L into 2 groups
#-------------------------------------------------
def two_group(L):
	if len(L)==1:
		return L[0]
	if len(L)%2 == 0:
		# even
		first = L[0 : len(L)//2]
		second = L[len(L)//2 : len(L)]
		if scale(first, second) == -1:
			# fake coin is in first
			return two_group(first)
		else:
			# fake coin is in second
			return two_group(second)
	else:
		# odd
		first = L[0 : len(L)//2]
		second = L[len(L)//2 : len(L)-1]
		last = L[-1]
		if scale(first, second) == 0:
			return last
		if scale(first, second) == -1:
			# fake coin is in first
			return two_group(first)
		else:
			# fake coin is in second
			return two_group(second)

#-------------------------------------------------
for i in range(10, 100, 5):
	L = generate_coins(i)
	print(i, two_group(L))

