#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 19:39:51 2019

@author: AkashTyagi
"""
# =============================================================================
#  Given an unsorted array of integers, print all elements which are greater than all elements present to its right.
#  Input: [10,4,6,3,9,1]
#  Output: 10,9
# =============================================================================

x = [10,4,6,3,5,1,9,1]

# Approach 1-->  Use a stack whose top is always greater than the current value of loop.
count = 0
bv = []
lp =1
for n in x:
    print("Loop: ",lp)
    lp+=1
    while len(bv)!= 0 and bv[-1] < n:
        bv.pop()
    bv.append(n)
print("Result: ",bv)
print('\n')
# Analysis: Complexity= O(n) as 1 iteration chalega

#######################

# Approach 2--> Traverse list from R-to-L and store max value until new max value found. Store all max value.

count = len(x) -1 # Dicy of this line complexity
max_list = []
max = 0
c = 1
while count>=0:
    print("Loop ",c)
    c+=1
    if x[count] > max:
        max = x[count]
        max_list.append(max)
    count-=1
print("Result: ",max_list)
    

x = {1,3,2}
x = {1,2,4,4,5}





