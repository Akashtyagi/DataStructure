#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 02:14:16 2020

@author: AkashTyagi
"""

# =============================================================================
# Longest common substring
# =============================================================================

'''
Problem:
        Given 2 string - S1 & S2,
        find the length of longest continuous substring common between them.
'''

s1 = "abcdef"
s2 = "abdef"

def solve_substring(s1,s2):
    dp = [[0]*(len(s1)+1) for i in range(len(s2)+1)]
    maxlen = 0
    for i in range(1,len(s2)+1):
        for j in range(1,len(s1)+1):
            if s2[i-1]==s1[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
                maxlen = max(maxlen,dp[i][j])
    return maxlen

print(solve_substring(s1, s2))
                