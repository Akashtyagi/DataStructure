#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 12:37:15 2020

@author: Akash Tyagi
"""

#Question: https://leetcode.com/problems/majority-element/solution/#fnref1

#nums = [1,1,1,2,2,2,4,5] # Doesn't work for this. (No majority elem)
nums = [2,1,2,2,5,2,4]
#nums = [2,3,3]
l = len(nums)
    

# =============================================================================
# Moore Voting Algorithm
# =============================================================================
'''
http://www.cs.utexas.edu/~moore/best-ideas/mjrty/example.html
*** WORKS ONLY if we have atleast 1 element in majority. ***

We increase the count if next element is same as "Value" and 
decrease if its different. 

If at any case count==0 i.e "The "Value" is no more the most repetitive elem.
Then we set current integer as "Value" and set its count = 1.

In the end, most occuring element will be present in "Value" 
because its count will never be 0 as it occurs more than half.
'''
count = 0

for i in range(l):
    if count==0:
        value = nums[i]
        count = 1
        continue
    
    if value == nums[i]: 
        count+=1
    else :
        count-=1

print("Value: ",value)
t = 0    
for i in nums:
    if i == value:
        t+=1
        if t>l//2:
            print(value)
            break
        
