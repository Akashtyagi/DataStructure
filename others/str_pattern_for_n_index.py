#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 19:05:10 2019

@author: AkashTyagi
"""

st = 'abcdef'
n = 3
# Expected Output= adbecf

arr = [s for s in st]

arsize = len(arr)
result = ''
indexes = set()

c =0
d = 0
lp = 0
count = 0    
    
while c<arsize and count < arsize :
    lp+=1
    if d > arsize-1:
        c+=1
        d=c
    if d not in indexes:
        result += arr[d]
        indexes.add(d)
        count += 1
        d+=n
    
print("Initial: ",st)
print("Final: ",result)
