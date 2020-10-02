#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 21:16:40 2020

@author: AkashTyagi
"""

s = 'defaultdict'
from collections import defaultdict
count = defaultdict(int)
# for i in set(s):
#     count[i]+=1
    
i = j = 0
longest = 0
count[s[0]] = 1
l = len(s)
start = end = 0
while j<l-1:
    if count[s[j+1]]==0:
        j+=1
        count[s[j]]+=1
        if longest<j-i+1:
            longest = j-i+1
            start = i
            end = j
    else:
        count[s[i]]-=1
        i+=1
        
print(s[start:end+1])
print(longest)
    