#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 19:37:41 2020

@author: Akash Tyagi
"""

# =============================================================================
# Question: Find maximum repeating elem in list 
# =============================================================================

nums = [1,3,5,4,3,2]

'''
k = Max number in array.
n = Length of array

Condition: k<=n 
            
Logic: As 1 integer will be present more than once we add "k" to 
index equivalent of that integer i.e x[1]=5 so x[5]+=k .

In this way the most repeating number will lead to biggest value.

Now, the index at which we will have biggest value is answer.'''

#nums = [1,1,2,2,2,4,24]

#k = max(nums)
k = 6
l = len(nums)

for i in range(l):
    print(f"i:{i}, nums[i]= {nums[i]} -->{nums[i]%k} = {nums[i]%k} nums[{nums[i]%k}] = {nums[nums[i]%k]}+{k}={nums[nums[i]%k]+k}")
    nums[nums[i]%k]+=k
    

max_val = 0
answer = 0
for i in range(l):
    if nums[i]>max_val:
        max_val = nums[i]
        answer = i
print("\nMost repeating element: ",answer)

'''
Output:

i:0, nums[i]= 1 -->1 = 1 nums[1] = 1+6=7
i:1, nums[i]= 7 -->1 = 1 nums[1] = 7+6=13
i:2, nums[i]= 2 -->2 = 2 nums[2] = 2+6=8
i:3, nums[i]= 2 -->2 = 2 nums[2] = 8+6=14
i:4, nums[i]= 2 -->2 = 2 nums[2] = 14+6=20
i:5, nums[i]= 4 -->4 = 4 nums[4] = 2+6=8
i:6, nums[i]= 24 -->0 = 0 nums[0] = 1+6=7

Most repeating element:  6
'''
    



