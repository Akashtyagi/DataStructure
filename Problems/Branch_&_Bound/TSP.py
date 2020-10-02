#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 01:20:33 2020

@author: AkashTyagi
"""

# =============================================================================
# Travelling Salesman Problem
# =============================================================================
from collections import deque
from copy import deepcopy

graph= [
 [float("inf"), 20, 30, 10, 11],
 [15, float("inf"), 16, 4, 2],
 [3, 5, float("inf"), 2, 4],
 [19, 6, 18, float("inf"), 3],
 [16, 4, 7, 16, float("inf")]
 ]

def reduce_matrix(graph):
    reduction_cost = 0
    
    # Rows
    for i in range(len(graph)):
        if not 0 in graph[i] and any(j!=float("inf") for j in graph[i]):
            minn = min(graph[i])
            reduction_cost+= minn
            for j in range(len(graph[i])):
                graph[i][j]-=minn
    
    # Columns
    arr= []
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            arr.append(graph[j][i])
        if not 0 in arr and any(i!=float("inf") for i in arr):
            minn = min(arr)
            reduction_cost+=minn
            for q in range(len(graph[0])):
                graph[q][i]-=minn
        arr = []
    
    return reduction_cost

# Main code
cost_dic = {}
node_queue = [] # Node == different city salesman has to cover
node_number = 1

minimum_cost_possible = reduce_matrix(graph)
cost_dic[node_number] = minimum_cost_possible
refernce_graph = deepcopy(graph)

for i in range(len(graph[0])):
    route = graph[0][i]
    if route!=float("inf"):
        node_queue.append([0,i,node_number])

points = []        
# while node_queue:
    row, col, parent_node_num = node_queue.pop(0)
    node_number+=1
    for j in range(len(graph[col])):
        if graph[row][j]!= float("inf"):
            points.append(j)
    for i in range(len(graph)):
        graph[row][i] = float("inf")
        graph[i][col] = float("inf")
    graph[col][row] = float("inf")
    cost_dic[node_number] = refernce_graph[row][col] + cost_dic[parent_node_num] + reduce_matrix(graph)
    # if node_queue:
    #     node_queue.sort(key=lambda x:x[0])
    
    




         
            