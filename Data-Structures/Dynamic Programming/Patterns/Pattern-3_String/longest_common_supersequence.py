#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 01:17:53 2020

@author: AkashTyagi
"""

# =============================================================================
# Shortest common supersequence
# =============================================================================
# Question: https://leetcode.com/problems/shortest-common-supersequence/

s1 = "xyzakwudl"
s2 = "zperwuqcl"

# Approach
# 1. Find Longest common subsequence
# 2. Combine both string and remove 1st common subsequence

def lcs(s1,s2):
    l1 = len(s1)
    l2 = len(s2)
    
    dp = [['']*(l2+1) for i in range(l1+1)]
    
    for i in range(1,l1+1):
        for j in range(1,l2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]+s1[i-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1],key=len)
                
    return dp[-1][-1]

r = lcs(s1,s2)
result = []
i = j = 0

for s in r:
    while s!=s1[i]:
        result.append(s1[i])
        i+=1
    while s!=s2[j]:
        result.append(s2[j])
        j+=1

    result.append(s)
    i, j = i+1, j+1
    
r = ''.join(result) + s1[i+1:] + s2[j+1:]
print("Answer----> ",r)