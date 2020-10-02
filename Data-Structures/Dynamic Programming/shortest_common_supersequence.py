#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 03:03:11 2020

@author: AkashTyagi
"""

# =============================================================================
#                 Shortest common supersequence
# =============================================================================

'''
Problem:
    Given 2 strings, find length of new string which contain both the string
    along with their order.
'''

str1 = "aabc"
str2 = "cab"

def solve_lcs(str1,str2):
    dp = [['']*(len(str2)+1) for i in range(len(str1)+1)]
    
    # Using LCS
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j] = dp[i-1][j-1]+str1[i-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1],key=len)
    return dp[-1][-1]

print(solve_lcs(str1, str2))

'''
So now we have found common subsequence between them.
In order to create shortest common supersequence,
we can reduce length of LCS, to find shortest.
'''
resultstr = []
i = j = 0
for s in solve_lcs(str1,str2):
    while str1[i]!=s:
        resultstr.append(str1[i])
        i+=1
    while str2[j]!=s:
        resultstr.append(str2[j])
        j+=1
    resultstr.append(s)
    i, j = i+1,j+1
print(''.join(resultstr)+str1[i:]+str2[j:])

