#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 00:57:18 2020

@author: AkashTyagi
"""

# =============================================================================
# Rod Cutting problem
# =============================================================================
# Question: https://www.educative.io/edpresso/the-rod-cutting-problem


def rod_cutting(profits,N):
    dp = [[0]*(N+1) for i in range(N+1)]
    
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i<=j: # j=length of rod, i-> cut length
                dp[i][j] = max(dp[i][j-i]+profits[i-1],
                               dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

profits = [1, 5, 8, 9, 10, 17, 17, 20]
N = len(profits)
print(rod_cutting(profits,N))


# 1D array

INT_MIN = -1
price = [2,5,7,8]
n = len(price)
val = [0 for x in range(n+1)] 
  
# Build the table val[] in bottom up manner and return 
# the last entry from the table 
for i in range(1, n+1): 
    max_val = INT_MIN 
    for j in range(i): 
         max_val = max(max_val, price[j] + val[i-j-1]) 
    val[i] = max_val 
    
val[n]    