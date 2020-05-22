#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 00:44:33 2020

@author: Akash Tyagi
"""
# Question - https://leetcode.com/problems/3sum/
'''
From linked list 3 values such that, a+b+c=0
'''


# =============================================================================
# Approach
# =============================================================================
'''
We analyse certain points that needs to be true for a+b+c=0 scenario.

1. Sort the array, so indexing can be done better.
2. Take 2 pointers, LEFT & RIGHT, to make searching faster.
3. for each iteration fix one value and find remaining 2 values ahead of fixed using pointers.
4. If fixed value is greater than 0,remaining 2 values will always be >0 so sum can never be 0, so no more solutions.
5. If for some pointer values the total sum is greater than 0 then we need to reduce the RIGHT pointer.
6. If less than 0 then we need bigger value so increase LEFT pointer.
7. If Equal==0, answer.
8. As we have to find unique values, if the next fixed value is same as prev, it should be auto incremented to next value.
9. The loop needs to run only till n-2 because when we fix n-2th value, we wont have 2 values to find.
10. Loop needs to be continued only until LEFT<RIGHT pointer
'''

# Test cases
#nums = [-5,-10,-15,3,4,11,17,20]
#nums = [-1, 0, 1, 2, -1, -4]
#nums = [0,0,0,0]
#nums = [-2,0,1,1,2]


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        length = len(nums)
        nums.sort() # Point 1         
        
        for FIXED_pointer in range(length-2): # Point-8
            if nums[FIXED_pointer]>0: # Point-4
                break
            if FIXED_pointer>0 and nums[FIXED_pointer]==nums[FIXED_pointer-1]:
                continue
            LEFT_pointer = FIXED_pointer+1 # Point-2,3
            RIGHT_pointer = length-1 # Point-2
            
            while LEFT_pointer<RIGHT_pointer: # Point-10
                total = nums[FIXED_pointer]+nums[LEFT_pointer]+nums[RIGHT_pointer]
                if total>0: # Point-5
                    RIGHT_pointer-=1
                elif total<0: # Point-6
                    LEFT_pointer+=1
                else: # Total=0 -- Answer  # Point-7
                    result.append([nums[FIXED_pointer],nums[LEFT_pointer],nums[RIGHT_pointer]])
                    while LEFT_pointer<RIGHT_pointer and nums[LEFT_pointer]==nums[LEFT_pointer+1]: # Point-8
                        LEFT_pointer+=1
                    while LEFT_pointer<RIGHT_pointer and nums[RIGHT_pointer]==nums[RIGHT_pointer-1]: # Point-8
                        RIGHT_pointer-=1
                    LEFT_pointer+=1
                    RIGHT_pointer-=1
        return result        