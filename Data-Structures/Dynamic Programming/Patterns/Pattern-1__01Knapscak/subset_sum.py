#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 00:12:11 2020

@author: AkashTyagi
"""

# Question Description: https://www.geeksforgeeks.org/subset-sum-problem-dp-25/

nums = [3, 34, 4, 12, 5, 2]
S = 9
# Expected Output: True

def subset_sum(nums,s):
    l = len(nums)
    dp = [[False]*(S+1) for i in range(l+1)]
    dp[0][0] = True
    for i in range(1, l+1):
        dp[i][0] = True
        for j in range(1, S+1):
            if nums[i-1]<=j:
                dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
                
    return dp[-1][-1]

nums = [1,11,5]
S = 6
print(subset_sum(nums,S))
