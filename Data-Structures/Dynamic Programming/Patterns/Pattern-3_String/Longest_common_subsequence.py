#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 01:12:37 2020

@author: AkashTyagi
"""

s1 = "Akash"
s2 = "miash"

# =============================================================================
# Find longest common Subsequence between 2 string
# =============================================================================

l1 = len(s1)
l2 = len(s2)
dp = [[0]*(l2+1) for i in range(l1+1) ]

r = 0

for i in range(1,l1+1):
    for j in range(1,l2+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
        r = max(dp[i][j], r)
        
print(r)

print("Longest Subsequence:--> ",end = ' ')

for i in range(1,l2+1):
    if dp[l1][i]!=0 and dp[l1][i] != dp[l1][i-1]:
        print(s2[i-1],end='')