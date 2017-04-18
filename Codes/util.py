import random

def random_list(n, Min, Max):
	return [ random.randint(Min,Max) for i in range(n) ]

def random_str(n, s):
	choices = list(s)
	return ''.join([ choices[random.randint(0,len(choices)-1)] for i in range(n) ])

if __name__ == '__main__':
	for i in range(10):
		print(random_str(10, 'ACGT'))