#Derico Walker
#04/18/17
#Homework 6
#Comp 4030

#Problem 1


#Problem 2
import networkx as nx
from math import *
import matplotlib.pylab as plt
import itertools as it

def draw_circle_around_clique(clique,coords):
    dist=0
    temp_dist=0
    center=[0 for i in range(2)]
    color=colors.next()
    for a in clique:
        for b in clique:
            temp_dist=(coords[a][0]-coords[b][0])**2+(coords[a][1]-coords[b][2])**2
            if temp_dist>dist:
                dist=temp_dist
                for i in range(2):
                    center[i]=(coords[a][i]+coords[b][i])/2
    rad=dist**0.5/2
    cir = plt.Circle((center[0],center[1]),   radius=rad*1.3,fill=False,color=color,hatch=hatches.next())
    plt.gca().add_patch(cir)
    plt.axis('scaled')
    # return color of the circle, to use it as the color for vertices of the cliques
    return color

global colors, hatches
colors=it.cycle('bgrcmyk')# blue, green, red, ...
hatches=it.cycle('/\|-+*')

# create a random graph
G=nx.gnp_random_graph(n=7,p=0.6)
# remember the coordinates of the vertices
coords=nx.spring_layout(G)

# remove "len(clique)>2" if you're interested in maxcliques with 2 edges
cliques=[clique for clique in nx.find_cliques(G) if len(clique)>2]

#draw the graph
nx.draw(G,pos=coords)
for clique in cliques:
    print "Clique to appear: ",clique
nx.draw_networkx_nodes(G,pos=coords,nodelist=clique,node_color=draw_circle_around_clique(clique,coords))

plt.show()

#Problem 3

def clique(A,k):
    C = clique(A, k-1)
    S = new list
    for tuple in C:
        for i in range(0 to n-1):
            //make sure the ith vertex is linked to each
            //vertex in tuple
            for j in tuple:
                if A[i,j] != 1:
                    break
            //This means that vertex i makes a clique
            if j is the last element:
                newtuple = (i | tuple) //make a new tuple with i added
                add newtuple to S
    //Return the list of k-cliques
    return S