#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 00:02:09 2020

@author: AkashTyagi
"""

nums = [2,3,4,1,5,6,7,3,9]

# =============================================================================
#                           Next Smallest Element
# =============================================================================
# Maintain Increasing order stack
nums = [2,3,4,1,5,6,7,3,9]
stack = []
count = 0
for i in nums:
    if not stack:
        stack.append(i)
        continue
    while len(stack)>0 and i<stack[-1]: # Maintain increasing order, i<stack[-1]
        n = stack.pop()
        print(f"For {n} next smallest element is {i}")
    stack.append(i)
print("\n")
# =============================================================================
# Next Biggest Element
# =============================================================================
# Maintain Decreasing order stack

stack = []

p = q =0

for i in nums:
    p+=1
    if not stack:
        stack.append(i)
        continue
    while len(stack)>0 and i>stack[-1]: # Maintain Decreasing order, i>stack[-1]
        q+=1
        n = stack.pop()
        print(f"For {n} next biggest element is {i}")
    stack.append(i)
print(p+q)


