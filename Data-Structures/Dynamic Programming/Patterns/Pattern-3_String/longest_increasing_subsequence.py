#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 23:17:03 2020

@author: AkashTyagi
"""

# =============================================================================
# Longest Increasing Subsequence
# =============================================================================

a = [2,5,3,7,11,8,10,13,6]

def lis(a):
    '''
    Store how many smaller no. visited, as we move forward in array.
    
    arr[] will contain, for each index, how many smaller than that we got.
    
    We find that by checking arr[] value of all elements previous to current,
    and if they got more count than current then it means that subsequence has
    higher value.
    '''
    arr = [1 for i in range(len(a))]
    mx = 0
    i = 1
    for i in range(len(a)):
        for j in range(0,i):
            if a[j]<a[i] and arr[j]>=arr[i]:
                arr[i] = arr[j]+1
                mx = max(arr[i],mx)
    print("Length of LIS ",mx)
    
    lis_arr = [0]*mx
    index = mx-1
    for i in range(len(arr)-1,-1,-1):
        if arr[i]==mx:
            lis_arr[index] = a[i]
            mx -= 1
            index-=1
        if mx==0:
            break
    print(lis_arr)
        

lis(a)
