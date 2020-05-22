#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:43:14 2020

@author: AkashTyagi
"""

# n_houses = 4
# n_pipes = 2

# # connections = [[source-house, destination-house, pip-diameter]]
# connections = [[1, 2, 60],
#                [3, 4, 50]]
def house_connection(n_houses, n_pipes, connections):
    house_conn = {house_n:{"parent":0,
                           "child":0,
                           "pipe_dia": 0} for house_n in range(1,n_houses+1)}
    
    for conn in connections:
        parent = conn[0]
        child = conn[1]
        pipe = conn[2]
        # house_conn[parent]['parent'] = parent
        house_conn[parent]['child'] = child
        house_conn[child]['parent'] = parent
        house_conn[child]['pipe_dia'] = pipe
        # index+=1
        
    
    max_req_connections = n_houses-n_pipes
    
    tanks = 0
    taps = 0
    pairs = []
    
    for house_no,house in house_conn.items():
        if house['parent'] == 0 and house['child'] != 0:
            # Means No incoming pipe
            gets_tank = house_no
            tanks+=1
            neighbour_house = house['child']
            pipe_dia = house_conn[neighbour_house]['pipe_dia']
            # child_parent = house_no
            while house_conn[neighbour_house]['child']!=0:
                neighbour_house = house_conn[neighbour_house]['child']
                new_pipe_dia = house_conn[neighbour_house]['pipe_dia']
                if new_pipe_dia < pipe_dia:
                    pipe_dia = new_pipe_dia
                # child_parent = neighbour_house
            taps+=1
            gets_tap = neighbour_house
            pairs.append([gets_tank, gets_tap, pipe_dia])
    for i in pairs:
        print(i)
        
        
# =============================================================================
# Take input
# =============================================================================
s = '''9 6
7 4 98
5 9 72
4 6 10
2 8 22
9 7 17
3 1 66'''

# s = '''15 10
# 4 9 44
# 5 10 50
# 6 4 100
# 3 15 41
# 1 7 37
# 13 6 19
# 15 2 99
# 11 8 3
# 4 12 35
# 14 11 65'''
inputs = s.split("\n")
n_houses = int(inputs[0].split()[0])
n_pipes = int(inputs[0].split()[1])
connections = []
for i in range(1,n_pipes+1):
    connections.append([int(n) for n in inputs[i].split()])
house_connection(n_houses, n_pipes, connections)    