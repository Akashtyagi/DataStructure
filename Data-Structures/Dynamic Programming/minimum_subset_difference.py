#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 01:30:46 2020

@author: AkashTyagi
"""

# =============================================================================
# Minimum subset sum difference problem
# =============================================================================

# arr = [14,1,5,7,4]
# arr= [1,1,2,3]
# arr = [1,2,7]
# arr = [1,3,2,4]
arr=[2,5,3,2,6]
def subset_sum(arr,target):
    dp = [[0]*(target+1) for i in range(len(arr)+1)]
    
    for i in range(1,len(arr)+1):
        dp[i][0] = 1
        for j in range(1,target+1):
            if arr[i-1]<=j:
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
                
    return dp

rang = sum(arr)

index = rang//2 # Half of total sum
dp = subset_sum(arr,index)


while True:
    if dp[-1][index]!=0:
        print(f"arr: {arr},\nTotal Sum: {rang},\nMinimum-Difference: {(rang-index)-index}")
        break
    else:
        index-=1

# Remaining index - sum of other set
remindex = rang-index


# =============================================================================
# Printing the subsets
# =============================================================================
set1 = []
for i in range(len(arr)-1,-1,-1):
    if index==0:
        break
    if arr[i]<=index:
        set1.append(arr[i])
        index-=arr[i]
        
set2 = []        
for i in range(len(arr)-1,-1,-1):
    if remindex==0:
        break
    if arr[i]<=remindex and arr[i] not in set1:
        set2.append(arr[i])
        remindex-=arr[i]

print(set1,set2)