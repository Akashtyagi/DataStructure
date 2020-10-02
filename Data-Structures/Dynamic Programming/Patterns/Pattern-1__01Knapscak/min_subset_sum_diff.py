#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 00:34:21 2020

@author: AkashTyagi
"""

def min_subset_sum_diff(nums):
    l = len(nums)
    summ = sum(nums)
    m = summ//2
    
    dp = [[False]*(m+1) for i in range(l+1)]
    dp[0][0] = True
    for i in range(1,l+1):
        dp[i][0] = True
        for j in range(1,m+1):
            if nums[i-1]<=j:
                dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
                
    while dp[-1][m]!=True:
        m-=1
    return (summ-m)-m

nums = [1,11,7]
print("Minimum difference between subset possible is: ",min_subset_sum_diff(nums))
                
    