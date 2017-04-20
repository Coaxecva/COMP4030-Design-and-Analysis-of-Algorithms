coins = [4,5,13,17]

Table = {}
def make_change(Coins, x):
	if x in Table:
		return Table[x]
	if x == 0:
		Table[x] = True
	elif x < 0:
		Table[x] = False
	else:
		Table[x] = any([ make_change(Coins, x-c) for c in Coins ])
	return Table[x]

for i in range(1000):
	Table = {}
	print(i, make_change(coins, i))

