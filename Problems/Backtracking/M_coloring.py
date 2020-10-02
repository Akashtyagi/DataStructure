#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 20:42:41 2020

@author: AkashTyagi
"""
graph = [[3],[2,4],[1],[0,4],[1,3]]
x = [[0]*len(graph) for i in graph]

for row in range(len(graph)):
    for i in graph[row]:
        x[row][i]=1
graph = x
# graph = [[0, 1, 0, 1], 
#          [1, 0, 1, 0], 
#          [0, 1, 0, 1], 
#          [1, 0, 1, 0]] 
colors = 2

color_matrix = [0]*len(graph)

color_matrix[0] = 1 # First color

def fillcolor(node,graph,color_matrix,colors):
    if node==len(graph):
        return True,color_matrix
    adjacents = graph[node]
    possible = False
    for new_color in range(1,colors+1):
        color_matrix[node] = new_color
        if checkColor(new_color,adjacents,color_matrix):
            possible = True
            possible,color_matrix = fillcolor(node+1,graph,color_matrix,colors)
            if possible:
                return True,color_matrix
            else:
                color_matrix[node] = 0
        else:
            color_matrix[node] = 0
    return possible,color_matrix
                
        
def checkColor(new_color,adjacents,color_matrix):
    possible = True
    for node in range(len(adjacents)):
        if adjacents[node]==1 and color_matrix[node] == new_color:
            possible = False
            return possible
    return possible
    

result,color_matrix = fillcolor(1,graph,color_matrix,colors)
if result:
    print(color_matrix)
else:
    print("Not Possible")