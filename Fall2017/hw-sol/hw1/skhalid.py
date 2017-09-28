#Sohail Khalid
#Comp 4030
#Assignment 1
import math

#coins = [ 2, 2, 2, 2, 2, 1.5, 2, 2, 2, 2, 2, 2]
#coins = [ 2, 2, 2, 2, 1, 2, 2, 2, 2]

import random

# define function to generate random coins
def generate_coins(n=27):
    coins = [2]*n
    coins[random.choice(range(n))] = 1
    return coins

# Iterative algorithm
def findFakeCoinInterative(coins):
    for i in range(len(coins) - 1):
        if coins[i] < coins[i+1]:
            return (i, coins[i]);

    return (len(coins)-1, coins[len(coins)-1])


# Recursive algorithm with two groups

def findFakeCoinRecursiveTwoGroups(coins, start, end):
    if start == end:
        return (start, coins[start])

    mid = ((start + end)//2)
    #print("Start", start, "End: ", end)
    a = findFakeCoinRecursiveTwoGroups(coins, start, mid)
    b = findFakeCoinRecursiveTwoGroups(coins, mid+1, end)
    if a[1] < b[1]:
        return a
    else:
        return b


# Recursive algorithm with three groups
def findFakeCoinRecursiveThreeGroups(coins, start, end):
    if end < start:
        return (end, coins[end])
    if start == end:
        return (start, coins[start])

    n = ((end - start) + 1)
    v = (n // 3)

    m = 0
    if n % 3 == 2:
        m = 1

    a = findFakeCoinRecursiveThreeGroups(coins, start, start + v)
    b = findFakeCoinRecursiveThreeGroups(coins, start + v+1, start + 2*v + m)
    c = findFakeCoinRecursiveThreeGroups(coins, start + 2*v + m + 1, end)
    if a[1] < b[1]:
        if a[1] < c[1]:
            return a
        elif a[1] > c[1]:
            return c
        else:
            return a
    elif a[1] > b[1]:
        if b[1] < c[1]:
            return b
        elif b[1] > c[1]:
            return c
        else:
            return b
    else:
        if b[1] < c[1]:
            return b
        elif b[1] > c[1]:
            return c
        else:
            return a

coins = generate_coins(5)
print(coins)

#Test Iterative Algorithm
result = findFakeCoinInterative(coins)
print("index: ", result[0], " weight:", result[1])


#Test Two split recursive algorithm
result = findFakeCoinRecursiveTwoGroups(coins, 0, len(coins)-1)
print("index: ", result[0], " weight:", result[1])

#Test Three split recursive algorithm
result = findFakeCoinRecursiveThreeGroups(coins, 0, len(coins)-1)
print("index: ", result[0], " weight:", result[1])
