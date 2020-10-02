#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 03:19:30 2020

@author: AkashTyagi
"""
floor = 6
egg = 2


t = [[0]*(floor+1) for i in range(egg+1)]

c = 0

for i in range(floor+1):
    t[1][i] = i
    
for e in range(2,egg+1):
    for f in range(1,floor+1):
        t[e][f] = float('inf')
        
        for k in range(1,f+1):
            c= 1+max(t[e-1][k-1],
                     t[e][f-k])
            
            if c<t[e][f]:
                t[e][f] = c
        
print(t[egg][floor])
    



