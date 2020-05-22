#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 01:27:32 2020

@author: Akash Tyagi
"""

# =============================================================================
# Explanation: https://www.youtube.com/watch?v=QN9hnmAgmOc
# =============================================================================

def partition(nums,lb,ub):
    start_Pointer = lb
    end_Pointer = ub
    
    print(nums[start_Pointer:end_Pointer+1]," Start ",start_Pointer," End ",end_Pointer)
    
#    print(nums)
    pivot = nums[lb]
    
    while start_Pointer<end_Pointer:
        while nums[start_Pointer] <= pivot: # Keep increasing start_Pointer if less than pivot
            start_Pointer+=1
        while nums[end_Pointer]>pivot:  # Keep increasing start_Pointer if less than pivot
            end_Pointer-=1
        if start_Pointer<end_Pointer: # Swap end<->start as end has smaller than pivot and start has bigger than Pivot.
            temp =  nums[end_Pointer]
            nums[end_Pointer] = nums[start_Pointer]
            nums[start_Pointer] = temp
            
    temp2 = nums[end_Pointer]   # End has crossed Start, at this point end represent correct position where start should be.
    nums[end_Pointer] = nums[lb]
    nums[lb] = temp2
    return end_Pointer

def quicksort(nums,start=None,end=None):
    if start is None and end is None:
        start = 0
        end = len(nums)-1
    
    if start<end:
        loc = partition(nums,start,end)
        quicksort(nums,start,loc-1)
        quicksort(nums,loc+1,end)
    return nums

if __name__ == "__main__":
    nums = [4,7,2,4,1,9,6,5]
    print("\nSorted Array: ",quicksort(nums))


''' 
Output:

[4, 7, 2, 4, 1, 9, 6, 5]  Start  0  End  7
[4, 1, 2]  Start  0  End  2
[2, 1]  Start  0  End  1
[7, 9, 6, 5]  Start  4  End  7
[6, 5]  Start  4  End  5

Sorted Array:  [1, 2, 4, 4, 5, 6, 7, 9]
'''
