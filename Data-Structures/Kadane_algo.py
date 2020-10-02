#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 20:50:10 2020

@author: AkashTyagi
"""

# =============================================================================
# Kadane Algorithm
# =============================================================================

'''
Find maximum contiguos sumarray within an array.

This Algorithm works for circular and non-circular arrays.
'''

'''
Approach:
    * For every index find prefix sum(all previous element + curr elem sum),
      rule is,
        current sum = max(curr_elem, prefixsum_sofar+curr_elem)
    
    * Also, keep track of maximum-sum-so far, as we keep finding prefix sum,
      we store, the max sum occured so far and the pointers where it ocuured.
    
    * Maximum prefix sum will tell the max sum that can be obtained from array.
'''      

nums = [3,-2,2,9,-1,-14,5]
# nums = [7,1,5,3,6,4]
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [-2,-1]
l = len(nums)

prefix_sum = [0]*l
prefix_sum[0] = nums[0]

max_sum = prefix_sum[0] # To store the max prefix-sum
start = 0
end= 0
fstart = fend = 0

for i in range(1,l):
    curr_sum = prefix_sum[i-1]+nums[i] 
        
    if curr_sum<nums[i]:
        # sum after addition is smaller than current index value.
        prefix_sum[i] = nums[i]
    
    else:
        # collective sum is greater than current index value.
        prefix_sum[i] = curr_sum
        end=i
        
    if prefix_sum[i]<0:
        # if current index sum becomes smaller than 0. Then reset temp start 
        # and end pointer
        
        if i+1<l:
            # start can be set to next element, if exist.
            start = i+1
        else:
            start = i
        end = i
    
    if max_sum<prefix_sum[i]:
        # if max_sum is smaller than current prefix_sum index.
        # Set new max_sum, store starting and ending index for max_sum subarray so far.
        max_sum = prefix_sum[i]
        fstart = start
        fend = end        

print(f"Max subrarray sum is {max_sum}")
print(f"Max subarray is {nums[fstart:fend+1]} -- Maybe Not working correctly")        
    
'''
In order to get circular subarray maximum.
Find max_min from prefix sum, so that we can get minimum subbary sum,

Now, if we do, 
    Total Array prefix sum - Minimum subarray prefix sum = Maximum subbarray prefix sum.
'''