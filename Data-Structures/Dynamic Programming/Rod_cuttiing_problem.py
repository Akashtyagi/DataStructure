#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 01:24:37 2020

@author: AkashTyagi
"""
# =============================================================================
#                         Rod Cutting Problem 
# =============================================================================

'''
Problem:
    Cut the rod into such peices that the profit is maximized.
    Max length of rod
'''

length = [2,4,3,1,2,3] # rod length
profits = [7,5,6,1,5,4] # Profit of each length
N = 10 # Length of rod

dp = [[0]*(N+1) for i in range(len(length)+1)]

for i in range(len(length)+1):
    dp[0][i] = 1
    
for i in range(1,len(length)+1):
    for j in range(1,N+1):
        if length[i-1]<=j:
            dp[i][j] = max(dp[i][j-length[i-1]]+profits[i-1],
                           dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

dp[-1][-1]