#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 01:40:24 2020

@author: AkashTyagi
"""

s1 = "akash"
s2 = "ashmit"


l1 = len(s1)
l2 = len(s2)
dp = [[0]*(l2+1) for i in range(l2+1)]

r = 0
for i in range(1,l1+1):
    for j in range(1, l2+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = 1+dp[i-1][j-1]
            r = max(r,dp[i][j])
        else:
            dp[i][j] = 0
print(r)    
    