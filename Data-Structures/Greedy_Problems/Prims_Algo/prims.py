#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 13:59:16 2020

@author: AkashTyagi
"""

'''
Prims Algo can be used when we want to connect a graph with minimum overall cost.
'''


from queue import PriorityQueue

q = PriorityQueue()


'''
Defining Graph
    using dictionary
    
    {
      "vertex" : [ (ajc-vrtx, weight) ]
      "vertex2": [ (ajc-vrtx, weight) ]
    }
'''

#graph = {
#            1: [ (2,28), (6,10)],
#            2: [ (1,28), (7,14), (3,16)],
#            3: [ (2,16), (4,12)],
#            4: [ (3,12), (7,18), (5,22)],
#            5: [ (4,22), (7,24), (6,25)],
#            6: [ (5,25), (1,10)],
#            7: [ (5,24), (4,18), (2,14)]
#            
#        }
#
#values = {x:float("inf") for x in range(1,8)}
#total_vertex = [1,2,3,4,5,6,7]
#minMST = set()


graph = {
            0: [ (1,4), (7,8) ],
            1: [ (0,4), (7,11) ],
            2: [ (1,8), (8,2), (5,4), (3,7) ],
            3: [ (2,7), (5,14), (4,9) ],
            4: [ (3,9), (5,10) ],
            5: [ (4,10), (3,14), (2,4) ],
            6: [ (5,2), (8,6), (7,1) ],
            7: [ (0,8), (1,11), (8,7), (6,1) ],
            8: [ (2,2), (7,7), (6,6) ]
        }
values = {x:float("inf") for x in range(0,9)}
total_vertex = [0,1,2,3,4,5,6,7,8]


minMST = set()
vertex = 1
values[vertex] = 0
#minMST.add(vertex) # Add 'u' to minMST
q.put([0,1]) #(value,edge)

while len(minMST)!=len(graph):
    
    if q.qsize()==0:
        flag = True
        while flag:
            vertex = total_vertex[0]
            total_vertex.pop(0) # We have covered this edge
            if vertex not in minMST:
                q.put([values[vertex],vertex])  #(value,edge)
                flag = False
            
    else:
        flag = True
        while flag:
            v = q.get()
            vertex = v[1]
            if vertex not in minMST:
                minMST.add(vertex)
                flag = False
        
    
    for vtx_wgh in graph[vertex]:
        adj_vtx = vtx_wgh[0]
        edge_wgh = vtx_wgh[1]
        if adj_vtx not in minMST:
            if edge_wgh < values[adj_vtx]:
                values[adj_vtx] = edge_wgh
                q.put([edge_wgh,adj_vtx])
        
    
mincost = sum([i for i in values.values()])
print("Minimum cost of the tree: ",mincost)        