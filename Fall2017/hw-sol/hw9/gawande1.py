
#Anuja Gawande
#               COMP 4030 
#                           Assignment 9

import graph
import datetime
import random
import time

#pal without cache
def palOld(seq):
    if len(seq)<= 1:
        return len(seq)
    if seq[0] == seq[-1]:
        return 2 + palOld(seq[1:-1])
    else:
        return max(palOld(seq[1:]), palOld(seq[:-1]))

#method to generate random strings 
import random
def rand_str(n, chars):
    return "".join([random.choice(chars) for i in range(n)])


#print(palOld("abcbbaababacbacbaabbbcbbcabaccacccb"))

pal_cache = {}
def pal(seq):
    if seq in pal_cache:
        return pal_cache[seq]
    
    if len(seq)<= 1:
        pal_cache[seq] = len(seq)
        return pal_cache[seq]

    if seq[0] == seq[-1]:
        pal_cache[seq] = 2 + pal(seq[1:-1])
        return pal_cache[seq]

    else:
        pal_cache[seq] = max(pal(seq[1:]), pal(seq[:-1]))
        return pal_cache[seq]
    


str =""
str = rand_str(35,'abcd')
str2 = rand_str(1,'t')
str3 = ''
str4 = rand_str(10000,'uio')

#print(str)
a1 = datetime.datetime.now()
pal(str)
b1 = datetime.datetime.now()
timetaken = b1 - a1
print("Time taken by cached pal")
print (timetaken)


str =""
str = rand_str(35,'abcd')
#print(str)
#takes a few minutes..........
a = datetime.datetime.now()
palOld(str)
b = datetime.datetime.now()
timetaken1 = b - a
print("Time taken by pal")
print (timetaken1)

#----------------------------------------------------------------------------------------------
#2. All sets of complete strangers.
def getSet(L):
    return [i for i in range(len(L)) if L[i]]

def checkVertices(L, g):
    if len(L) > 1:
        for i in range(len(L)):
            for j in range(1, len(L)):
                if (L[i] != L[j]):
                    return g.__contains__( (L[i],L[j]) )
    return True

def listCompleteStrangers(i, solution, g):
    L = getSet(solution)
    if i == len(solution) - 1:
        if not checkVertices(L, g):
            print(L)
    else:
        for item in [False, True]:
            solution[i+1] = item
            listCompleteStrangers(i+1, solution, g)

#------------------------------------------------------------------------------------------------
#3. Largest group of complete strangers.
def listLargestCompleteStrangerGroup(i, solution, g):
    L = getSet(solution)
    if i == len(solution) - 1:
        if not checkVertices(L, g):
            global largest_group
            if len(L) > len(largest_group):
                largest_group = L
    else:
        for item in [False, True]:
            solution[i+1] = item
            listLargestCompleteStrangerGroup(i+1, solution, g)

def promising(L, B):
    if len(getSet(B)) > len(L):
        return False
    return True

#-----------------------------------------------------------------------------------------------------------
#4. Largest group of complete strangers with pruning.
def listCompleteStrangersPruning(i, solution, g, cur_L, cur_best):
    L = getSet(solution)
    if promising(cur_L, cur_best):
        if i == len(solution) - 1:
            if not checkVertices(L, g):
                cur_best = L
                print(L)
        else:
            for item in [False, True]:
                solution[i+1] = item
                listCompleteStrangersPruning(i+1, solution, g, L, cur_best)

'''
Graph such that:
0----1----2
     |
     3
'''
g = graph.Graph()
g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add(0,1)
g.add(1,2)
g.add(1,3)
print("List of strangers:")
listCompleteStrangers(-1, [None]*len(g.Vertices), g)
print("--------------------------")

largest_group = []
listLargestCompleteStrangerGroup(-1, [None]*len(g.Vertices), g)
print("Largest group of strangers:")
print(largest_group)

print("--------------------------")
print("List of strangers by pruning:")
listCompleteStrangersPruning(-1, [None]*len(g.Vertices), g, [None]*len(g.Vertices), [None]*len(g.Vertices))