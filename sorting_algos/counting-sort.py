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
    print(f"log[i] =log[i]+ log[i-1] i:{i} {log[i]}= {log[i]}+{log[i-1]} ")
    log[i] = log[i]+ log[i-1]
    

print("\nDictionary: This tells the correct postiton of each element")
# Below loop only for explanation purpose.
for d in log:       
    if d in nums:
        print(f'\t {d}:{log[d]}')
    
sorted_array = [0]*len(nums)
print("\nPostion of 'i' in new sorted array")
for i in nums:
    x = log[i]
    sorted_array[x-1] = i
    print(f" i={i}, sorted_array[{x-1}]={i}")
    if x>0:
        print(f"\t{i}:{log[i]} -> {i}:{log[i]-1}")
        log[i]-=1

print("\nUnsorted Array: ",nums)
print("Sorted Array: ",sorted_array)

'''
Output:

log[i] =log[i]+ log[i-1] i:-7 1= 1+0 
log[i] =log[i]+ log[i-1] i:-6 0= 0+1 
log[i] =log[i]+ log[i-1] i:-5 0= 0+1 
log[i] =log[i]+ log[i-1] i:-4 1= 1+1 
log[i] =log[i]+ log[i-1] i:-3 0= 0+2 
log[i] =log[i]+ log[i-1] i:-2 0= 0+2 
log[i] =log[i]+ log[i-1] i:-1 0= 0+2 
log[i] =log[i]+ log[i-1] i:0 0= 0+2 
log[i] =log[i]+ log[i-1] i:1 1= 1+2 
log[i] =log[i]+ log[i-1] i:2 1= 1+3 
log[i] =log[i]+ log[i-1] i:3 0= 0+4 
log[i] =log[i]+ log[i-1] i:4 1= 1+4 
log[i] =log[i]+ log[i-1] i:5 0= 0+5 
log[i] =log[i]+ log[i-1] i:6 0= 0+5 
log[i] =log[i]+ log[i-1] i:7 0= 0+5 
log[i] =log[i]+ log[i-1] i:8 0= 0+5 
log[i] =log[i]+ log[i-1] i:9 1= 1+5 

Dictionary: This tells the correct postiton of each element
         -4:2
         1:3
         9:6
         4:5
         2:4
         -7:1

Postion of 'i' in new sorted array
 i=-4, sorted_array[1]=-4
        -4:2 -> -4:1
 i=1, sorted_array[2]=1
        1:3 -> 1:2
 i=9, sorted_array[5]=9
        9:6 -> 9:5
 i=4, sorted_array[4]=4
        4:5 -> 4:4
 i=2, sorted_array[3]=2
        2:4 -> 2:3
 i=-7, sorted_array[0]=-7
        -7:1 -> -7:0

Unsorted Array:  [-4, 1, 9, 4, 2, -7]
Sorted Array:  [-7, -4, 1, 2, 4, 9]
'''

