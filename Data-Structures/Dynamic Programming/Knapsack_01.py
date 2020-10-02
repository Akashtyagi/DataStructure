#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 21:09:02 2020

@author: AkashTyagi
"""

# =============================================================================
#                             0/1 Knapscak
# =============================================================================

weights = [2,4,3,1,2,3]
profits = [7,5,6,9,5,4]
capacity = 10

l = len(weights)


dp = [[0]*(capacity+1) for i in range(l+1)]
    
for i in range(1,l+1):
    for j in range(1,capacity+1):
        if weights[i-1]<=j:
            dp[i][j] = max(dp[i-1][j-weights[i-1]] + profits[i-1],
                           dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
            
print("Max profit: ",dp[-1][-1])

# =============================================================================
# Answer
# =============================================================================

print("Weights and profits that we took: ")
i = l
j = capacity
available_profit = dp[-1][-1]

while available_profit>0:
    if dp[i][j]==available_profit:
        while i>=0 and dp[i][j]==dp[i-1][j]:
            i = i-1
    while dp[i][j]>available_profit :
        j=j-1
    available_profit -= profits[i-1]
    print(f"\t Weight: {weights[i-1]}",end=", ")
    print(f"\t Profit: {profits[i-1]}")
    i-=1
    
    
    