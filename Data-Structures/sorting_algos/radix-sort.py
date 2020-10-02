#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 20:50:10 2020

@author: Akash Tyagi
"""

'''
Explanation: https://www.youtube.com/watch?v=JMlYkE8hGJM

Fastest sorting algo in term of time complexity.

* Redix sort maintains Locality of reference i.e If 3 occurs twice, then the 3 which occured first will present first in sorted array.

Different from counting sort as it does not need to make new array of k size, where k = max(arr)     

Logic - Find the biggest no. in array and make every no equal to that number's decimal count. 
if max. no is 234, so its decimal no is 3, so make every no. of 3 digit.

Then create a bucket from 0-9 and with every pass arrange value according to decimal position.

For, String sorting, buckets are made as 0-26
'''

nums = [4,123,34,75,54,13]

max_ = max(nums) # Time Complexity: N

total_passes = len(str(max_))
from collections import defaultdict
sorted_dict = defaultdict(list)
sorted_arr =  nums  # Space Complexity: n


for passes in range(0,total_passes): # Time Complexity: k
    if len(sorted_dict)>0:
        sorted_arr = [] 
        for i in range(0,10) : # Time Complexity: 10
            sorted_arr.extend(sorted_dict[i]) 
            sorted_dict[i]=[]   
    for i in sorted_arr: # Time Complexity: N
        n = int((i/10**passes)%10)
        sorted_dict[n].append(i)   
    print(f"For decimal Position: {passes} \n\t {sorted_dict}")
    
sorted_arr = [] # Space complexity: n
for i in range(0,10): # Time Complexity: 10
    sorted_arr.extend(sorted_dict[i])

print("\nUnsorted Array: ",nums)
print("Sorted Array: ",sorted_arr)

# =============================================================================
# Complexity Analysis
# =============================================================================
'''    
Time Complexity:
    = N + k(10+N) + 10 
    = N + 10k + Nk + 10
    = N(k+1) + 10(k+1)
    = Nk --> Ignoring Constant
    
Time Complexity = Nk
Space Complexity = n + 10(k) = n+k = As we have integers here so we had 0-9, so 10 was choosed, for char it can be 26, 
as it is variable and using a dict space, it is treated as K.
'''    


# =============================================================================
# Output
# =============================================================================
'''
For decimal Position: 0 
         defaultdict(<class 'list'>, {4: [4, 34, 54], 3: [123, 13], 5: [75]})
For decimal Position: 1 
         defaultdict(<class 'list'>, {4: [], 3: [34], 5: [54], 0: [4], 1: [13], 2: [123], 6: [], 7: [75], 8: [], 9: []})
For decimal Position: 2 
         defaultdict(<class 'list'>, {4: [], 3: [], 5: [], 0: [4, 13, 34, 54, 75], 1: [123], 2: [], 6: [], 7: [], 8: [], 9: []})

Unsorted Array:  [4, 123, 34, 75, 54, 13]
Sorted Array:  [4, 13, 34, 54, 75, 123]

'''
    
