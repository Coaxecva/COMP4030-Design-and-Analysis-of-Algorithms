#Daniel Linn
#COMP 4030
#Assignment 9

#problem 1
import time
import random

def rand_str(n, chars):
	return ''.join([ random.choice(chars) for i in range(n) ])

def pal(seq):
	if len(seq) <= 1:
		return len(seq)
	if seq[0] == seq[-1]:
		return 2 + pal(seq[1:-1])
	else:
		return max(pal(seq[1:]), pal(seq[:-1]))

def fast_pal(seq):
		Table[seq] = len(seq)
	if seq in Table: return Table[seq] if len(seq) <= 1:
		return Table[seq]
	if seq[0] == seq[-1]:
		Table[seq] = 2 + fast_pal(seq[1:-1])
		return Table[seq]
	else:
		Table[seq] = max(fast_pal(seq[1:]), fast_pal(seq[:-1]))
		return Table[seq]


Table = {}
string = rand_str(35, 'acgt')
#string = rand_str(31, 'acgt')
#string = rand_str(27, 'acgt')
#string = rand_str(21, 'acgt')
print(string)

t0 = time.time()
print(pal(string))
print(time.time()-t0)

t1 = time.time()
print(fast_pal(string))
print(time.time()-t1)
