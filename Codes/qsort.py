def quicksort(items):
	if len(items) <= 1:
		return items
	else:
		pivot = items[0]
		lesser = [x for x in items[1:] if x < pivot]
		greater = [x for x in items[1:] if x > pivot]
		return quicksort(lesser) + [pivot] + quicksort(greater)

L = [-1, 10, 2, 5, 4, -2, -9, 0, 4, 23, 64]
print(quicksort(L))