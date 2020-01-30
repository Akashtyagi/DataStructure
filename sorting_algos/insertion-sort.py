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

for i in range(1,l): # Pointer Iterates till end of list
    key = i
    prev = i-1
    print(f" --KEY: {x[key]}--")
    while prev>0 and x[prev]>x[key]: # Check if Previous is bigger than Key.
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
# Worst Case Complexity - N**2
# =============================================================================
