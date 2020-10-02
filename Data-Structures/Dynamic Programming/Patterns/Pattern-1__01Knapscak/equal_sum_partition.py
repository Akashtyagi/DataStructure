#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 00:20:06 2020

@author: AkashTyagi
"""

# Question description: https://leetcode.com/problems/partition-equal-subset-sum/

nums = [1, 4, 11]
nums = [2,3,1,2]
def equal_sum_subset_partition(nums):
    summ = sum(nums)
    
    if summ%2!=0:
        return False
    
    S = summ//2
    
    dp = [[False]*(S+1) for i in range(len(nums)+1)]
    
    for i in range(1,len(nums)+1):
        dp[i][0] = True
        for j in range(1, S+1):
            if nums[i-1]<=j:
                dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
                
    return dp[-1][S]

print(equal_sum_subset_partition(nums))


def oneD_sol(nums):
    summ = sum(nums)
    
    if summ%2!=0:
        return False
    
    S = summ//2
    
    dp = [False for i in range(S+1)]
    
    dp[0] = True # Base case
    
    for i in range(1,len(nums)+1):
        for j in range(S,-1,-1):
            if nums[i-1]<=j:
                dp[j] = dp[j-nums[i-1]] or dp[j]
                
    return dp[-1]

print(oneD_sol(nums))

    