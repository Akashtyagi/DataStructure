#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 01:50:28 2020

@author: AkashTyagi
"""
# =============================================================================
# Minimum no. of Coin required
# =============================================================================

'''
Problem:
    Given an amount, find minimum number of coins required to form the amount.
'''

arr = [1,2,3]
summ = 6

dp = [[0]*(summ+1) for i in range(len(arr)+1)]

for i in range(summ+1):
    dp[0][i] = float("inf")

for i in range(1,len(arr)+1):
    for j in range(1,summ+1):
        if arr[i-1]<=j:
            dp[i][j] = min(dp[i][j-arr[i-1]] + 1,
                           dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
            
print("Minimum ",dp[-1][-1]," coin needed to form ",summ)