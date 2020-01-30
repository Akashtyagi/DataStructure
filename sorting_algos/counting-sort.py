#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 19:22:38 2020

@author: Akash Tyagi
"""
'''
Counting Sort:
    
Logic -->
    arr = [-4,1,6,4,7,3]

Create a empty array with val 0 of range(min,max+1)min value of arr till max arr of nums, lets say "log"
    log = [0,1,0,0,2,0,1,0]
           0 1 2 3 4 5 6 7 

Now iterate through arr and for every value vistied, add 1 at index equival. of val in "log" array.
    4  --->  [0, 0, 0, 0, 1, 0, 0, 0]
    1  --->  [0, 1, 0, 0, 1, 0, 0, 0]
    6  --->  [0, 1, 0, 0, 1, 0, 1, 0]
    7  --->  [0, 1, 0, 0, 1, 0, 1, 1]
    3  --->  [0, 1, 0, 1, 1, 0, 1, 1]
    
    log = [0, 1, 0, 1, 1, 0, 1, 1]
           0  1  2  3  4  5  6  7 
           
Now add present value of log with prev value.
    log =   [0, 1, 0, 1, 1, 0, 1, 1]
                   1, 
                      2,
                         3,
                            3,
                               4,
                                   5,
    log =   [0, 1, 1, 2, 2, 3, 4, 5]
             0  1  2  3  4  5  6  7

Now, every value of nums array has its correct position in log array at its index.
Ex- nums[0] = 4 ---> log[4] = 3
    So, in sorted array first occurance of 4 needs to be at index 3.                     
           
    
    '''



from collections import defaultdict
nums = [-4,1,9,4,2,-7]

max_ = max(nums)
min_ = min(nums)
log = defaultdict(int)

for i in nums: # For every occurance of value in nums increase its index value in log-array by 1. 
    log[i]+=1

for i in range(min_,max_+1):
    print("log[i] =log[i]+ log[i-1]",i,log[i],log[i]+log[i-1])
    log[i] = log[i]+ log[i-1]
    
sorted_array = [0]*len(nums)
for i in nums:
    x = log[i]
    sorted_array[x-1] = i
    if x>0:
        log[i]-=1

print("Unsorted Array: ",nums)
print("Sorted Array: ",sorted_array)

