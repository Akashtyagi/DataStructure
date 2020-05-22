#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:11:42 2020

@author: AkashTyagi
"""

'''
Find Shortest path from source to destination.

Concept:
-------
    Assume distance to every other vertex from start as INF.
    
    Now from start, follow the process.

    Process:
        Step 1
        ------
        From given vertex, find all directed vertex, and replace target vertex weight,
        if, given_vertex_weight + distance < directed_vertex_distance:
            directed_vertex_distance = given_vertex_weight + distance
        
        Step 2
        ------
        * Add given-vertex to visited-vertex.
        
        Step 3
        ------
        * Add given-vertex as parent of directed-vertex.
        
        Step 4
        ------
        * Find smallest value of distances other than visited-vertex, using heapQ.
        
        Step 5
        ------
        * Again follow the process.
'''

#  {'vertex' : {'directed-to-vertex':'edge-weight'} }

graph = {'a': {'b':50, 'c':45, 'd':10},
         'b': {'c':10},
         'c': {'e':30},
         'd': {'a':20, 'e':15},
         'e': {'b':20, 'c':35},
         'f': {'e':3}
         }

from heapq import heapify, heappush, heappop
# using heap to find the minimum distance. STEP - 4
min_distance_heap = []
heapify(min_distance_heap) 

def shortest_path(graph,start,end):
    inf = float('inf')
    parent_vertex = {}
    shortest_distance = {}
    path = []
    unseeen_node = graph
    visited_vertex = set()
    
    for node in unseeen_node:
        shortest_distance[node]  = inf
    shortest_distance[start] = 0
    
    min_dist_node = start # Start node has mininum distance of 0.
    
    while unseeen_node:
        
        if min_dist_node is None:
            '''
            Handles unreachable vertex.
            
            Suppose if vertex was not reached so its distance remain INF, so 
            not in heap also, in that case we have to define the min_dist_node explicitly.
            '''
            min_dist_node = next(iter(unseeen_node))
        
        # Finding shortest distance
        for directed_to_vertex, edge_weight in graph[min_dist_node ].items(): 
            # STEP - 1
            if edge_weight + shortest_distance[min_dist_node ] < shortest_distance[directed_to_vertex]:
                # Update new shortest distance
                shortest_distance[directed_to_vertex] = edge_weight + shortest_distance[min_dist_node ]
                # Adding new shortest distance to heap
                heappush(min_distance_heap,(shortest_distance[directed_to_vertex],directed_to_vertex))
                # STEP - 3
                parent_vertex[directed_to_vertex] = min_dist_node 
        # Remove current node from unseen_node as we have traversed through it.
        unseeen_node.pop(min_dist_node )
        # As traversed, add it to visited-vertex
        visited_vertex.add(min_dist_node)
        
        flag = True 
        min_dist_node = None # Reset it.
        while flag and min_distance_heap:
            min_dist_node = heappop(min_distance_heap)
            min_dist_node = min_dist_node[1]
            if min_dist_node in visited_vertex:
                # Heap can have redundant value of previous vertex
                min_dist_node = None
            else:
                flag = False
        
    # Find path from end-start
    curr_node = end
    while curr_node != start:
        try:
            # Add vertex to starting of path, as we go from last to first.
            path.insert(0,curr_node)
            # Find parent of current vertex.
            curr_node = parent_vertex[curr_node]
        except:
            print("No such path exist !")
            break
    # Adding the starting vertex to starting of Path.
    path.insert(0,start)
    
    if shortest_distance[end] != inf:
        print(f"Shortest distance from {start}-to-{end}: {shortest_distance[end]}")
        print(f"Path followed is {'-->'.join(path)}")

shortest_path(graph,'a','e')
        
