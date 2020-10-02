#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 21:46:52 2020

@author: AkashTyagi
"""

# =============================================================================
# Subset Sum
# =============================================================================

'''
Problem Statement:
        Given a array of numbers and a target sum, identify if a subset can be 
        obtained whose sum is equal to the given sum.
'''

arr = [2,5,3,2,1,7]
summ = 12


def solve_subset_sum(arr,summ):
    dp = [[False]*(summ+1) for i in range(len(arr)+1)]
    for i in range(len(arr)+1):
        dp[i][0] = True
        for j in range(1,summ+1):
            if arr[i-1]<=j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

print(f" Does array contain any subset of sum={summ}? ",solve_subset_sum(arr,summ))

# =============================================================================
# Count subset of given sum
# =============================================================================

dp = [[0]*(summ+1) for i in range(len(arr)+1)]

for i in range(len(arr)+1):
    dp[i][0] = 1
    for j in range(1,summ+1):
        if arr[i-1]<=j:
            dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]

print(f" Count of subset containing sum={summ}? ",dp[-1][-1])