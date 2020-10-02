#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:19:34 2020

@author: AkashTyagi
"""

# Problem Description: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50

def knapsack(val,wt,W):
    dp = [[0]*(W+1) for i in range(len(val)+1)]
    
    for item in range(1,len(val)+1):
        for weight in range(1,W+1):
            if wt[item-1]<=weight:
                dp[item][weight] = max(dp[item-1][weight-wt[item-1]] + val[item-1],
                                        dp[item-1][weight])
            else:
                dp[item][weight] = dp[item-1][weight]
                
    return dp[-1][-1]

knapsack(val, wt, W)