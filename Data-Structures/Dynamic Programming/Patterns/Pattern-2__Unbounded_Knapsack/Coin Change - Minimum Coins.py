#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 21:46:54 2020

@author: AkashTyagi
"""

# =============================================================================
# Coin change - Minimum Coins
# =============================================================================
# Problem Statement - https://leetcode.com/problems/coin-change/


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        l = len(coins)
        dp = [[-1]*(amount+1) for i in range(l+1)]
        
        for i in range(amount+1):
            dp[0][i] = float('inf')
            
        for i in range(1,l+1):
            dp[i][0] = 0
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    dp[i][j] = min(1+dp[i][j-coins[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
                    
        if dp[-1][-1]==float('inf'):
            return -1
        else:
            return dp[-1][-1]
            