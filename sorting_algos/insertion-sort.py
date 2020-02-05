#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 12:52:11 2020

@author: Akash Tyagi
"""

''' Iterate through list and arrange element w.r.t previous elements in sorting algo. 
As we move forward prev list is sorted and every new element is checked for its correct position in prev array. '''

x = [5,2,4,1,3]

l = len(x)
i = 1

print("Target list: ",x,"\n")

for i in range(1,l): # Pointer Iterates till end of list  # Complexity:n-1
    key = i
    prev = i-1
    print(f" --KEY: {x[key]}--")
    while prev>0 and x[prev]>x[key]: # Check if Previous is bigger than Key. # Complexity: n
        temp = x[key]
        x[key] = x[prev]
        x[prev] = temp      # Swap prev <--> target
        key = key-1         # Reset index of target
        prev = prev-1       # Reset index of prev
        print(f"---> {x}")
    print(x,"\n")
    i=i+1

print(f"Sorted List: {x}")

# =============================================================================
# Complexity Analysis
# =============================================================================
'''
Outer loop will run (n-1)times.
While loop contains 2 condition.
    1. For prev>0, for i=n , prev = n-1, so it will run min (n-1) times.
    2. x[prev]>x[key], in worst case, say reversed array, this condition will always be True, so this loop will run min (n) times.
    
Therefore, 
    Time-complexity = (n-1)*[(n-1)+(n-1)] = n**2
    Space-complexity = 1 = Swap operations no extra space needed.
'''