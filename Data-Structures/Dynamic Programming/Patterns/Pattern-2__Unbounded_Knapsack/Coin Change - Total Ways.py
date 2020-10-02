#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 19:28:58 2020

@author: AkashTyagi
"""

# =============================================================================
# Coin Change - Total Ways
# =============================================================================
# Problem Statement: https://www.geeksforgeeks.org/coin-change-dp-7/

def solve(arr,N):
    ''' Using 2D array '''
    l = len(arr)
    dp = [[0]*(N+1) for i in range(l+1)]
    
    for i in range(1,l+1):
        dp[i][0] = 1 # Given any number of coins, 0 sum with no coins selected
        for j in range(1,N+1):
            if arr[i-1]<=j:
                dp[i][j] = dp[i][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]
                

arr = [1,2,3]
N = 5

print(solve(arr,N))


def solve2R(arr,N):
    ''' Using 2 array '''
    prev = curr = [0]*(N+1)
    
    prev[0] = curr[0] = 1
    
    for i in range(1,len(arr)+1):
        for j in range(1,N+1):
            if arr[i-1] <= j:
                curr[j] = curr[j-arr[i-1]] + prev[j]
            else:
                curr[j] = prev[j]
        prev = curr
        curr = [0]*(N+1)
        curr[0] = 1
    return prev[-1]

print(solve2R(arr, N))


def solve1D(arr,N):
    ''' Using 1 array '''
    dp = [0]*(N+1)
    dp[0] = 1
    
    for i in range(1, len(arr)+1):
        for j in range(1, N+1):
            if arr[i-1]<=j:
                dp[j] = dp[j-arr[i-1]] + dp[j]
    
    return dp[-1]


print(solve1D(arr, N))
            
        
    
arr = []        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    