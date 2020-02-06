#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 18:45:42 2019

@author: AkashTyagi
"""

# =============================================================================
# Using metrix as dict
# =============================================================================

x = [12,4,9,14,18,3,4,5,6,7,8,9,1,6]
sum = 20

from collections import defaultdict

metrix = defaultdict()
count = 0
for n in x:
    print("Loop ",count)
    count +=1
    if sum-n in metrix:
        print("Found sum at %d and %d"%(n,sum-n))
        break
    metrix[n] = n
    
    
high = len(x)-1
low = 0

# =============================================================================
# Using High and Low
# =============================================================================
c1 = 0
x.sort()
while(low < high):
    print("Loop: ",c1)
    c1 +=1
    if x[high]+x[low] == sum:
        print("Found sum at %d and %d"%(x[high],x[low]))
        break
    elif (x[high]+x[low]) < sum:
        low = low+1
    else:
        high = high-1
        