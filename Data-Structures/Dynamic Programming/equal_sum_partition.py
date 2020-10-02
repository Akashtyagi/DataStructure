#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 00:45:12 2020

@author: AkashTyagi
"""

# =============================================================================
# Equal Sum partition 
# =============================================================================


'''
Problem Statement
    Identify if array can be divided into such subsets so that their difference
    becomes 0.

    Logic:
        Array can be divided into equal sum only if their total sum is even, 
        which means:
                S1-S2 = 0, S1 = S2
                S1+S2 = summ ,  and we know 
                so --- S1+ S1 = sum
                        2S1 = sum
                        S1 = sum/2
        
        So we have to find just S1 and that will be around mid, and S2 will 
        automatically be Sum-S1.
        
        Better watch video for this
'''
import subset_sum

arr = [2,5,3,2,1,7,1]
summ = sum(arr)


if summ%2==0:
    print(subset_sum.solve_subset_sum(arr, summ//2))
else:
    print("Equal Sum partition not possible.")
