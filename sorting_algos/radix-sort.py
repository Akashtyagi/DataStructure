#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 20:50:10 2020

@author: Akash Tyagi
"""

'''
Explanation: https://www.youtube.com/watch?v=JMlYkE8hGJM

Fastest sorting algo in term of time complexity.

Different from counting sort as it does not need to make new array of k size, where k = max(arr)     

Logic - Find the biggest no. in array and make every no equal to that number's decimal count. 
if max. no is 234, so its decimal no is 3, so make every no. of 3 digit.

Then create a bucket from 0-9 and with every pass arrange value according to decimal position.
'''

nums = [4,123,34,75,54,13]

max_ = max(nums) # Time Complexity: N

total_passes = len(str(max_))
from collections import defaultdict
sorted_dict = defaultdict(list)
sorted_arr =  nums


for passes in range(0,total_passes): # Time Complexity: k
    if len(sorted_dict)>0:
        sorted_arr = []
        for i in range(0,10) : # Time Complexity: 10
            sorted_arr.extend(sorted_dict[i])
            sorted_dict[i]=[]
    for i in sorted_arr: # Time Complexity: N
        n = int((i/10**passes)%10)
        sorted_dict[n].append(i)

sorted_arr = []
for i in range(0,10): # Time Complexity: 10
    sorted_arr.extend(sorted_dict[i])

print("Unsorted Array: ",nums)
print("Sorted Array: ",sorted_arr)
    
'''    
Total Time Complexity:
    = N + k(10+N) + 10 
    = N + 10k + Nk + 10
    = N(k+1) + 10(k+1)
    = Nk --> Ignoring Constant
'''    
# =============================================================================
# So total time complexity: Nk
# =============================================================================
    
