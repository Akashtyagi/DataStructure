#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:08:08 2019

@author: AkashTyagi
"""


# =============================================================================
# ***Question*** Check if array has any subset in it whose sum is 0.
# Problem_link: https://www.techiedelight.com/check-subarray-with-0-sum-exists-not/
# 
# Logic: The concept is to save sum of all values as we iterate in a set. 
#        The sum value will keep changing with every iteration and will become same to any existing
#        sum-value only if values in between cancel each other i.e result sum to 0. As soon as we find that we stop.
#        
# Example: sum-set= [2,4,6,8,4]
#             The last 4 will only come only if there are values after 4(first) whose sum resulted
#             to 6 & 8 and had -ve values which canceled 6 & 8 and again made sum to 4.
#             That means that sub-array between both 4 had sum of 0.
# =============================================================================

arr = [4,2,-3,-3,5,-2]


def sum0(arr):
    sum = 0
    sum_set = set()
    sum_set.add(0)

    
    for n in arr:
        sum = sum+n
        if sum in sum_set: # Checks if sum already exist in set
            return "Subset exists. " 
        else:
            sum_set.add(sum)
    return "No subset exists."

sum0(arr)