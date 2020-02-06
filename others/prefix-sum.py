#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:15:10 2019

@author: Akashtyagi
"""

# =============================================================================
#                 arr1 = [ 1, 2, 3, 4, 5]
# Right shifted array =  [ 1, 3, 6, 10, 15]
# =============================================================================


# So value of sum arr1[1,5] after left shift = a[5] = 15
#    Value of sum arr1[1,3] after left shift = a[3] = 6

'''
But to calculate value of sum arr[2,4] after left shift we again need to find sum from index 2 to 4
and this can be very time consuming process for large array values suppose sum of arr[10,90] for array [500]

So to eliminate repetitive process of finding sum again and again...we can look as....

Summ of arr[2,4] = sum of arr[0,4]-sum of arr[1,2]
which is again equal to...  summ of arr[2,4] = arr[4]-arr[2-1] = 9
'''

print("Enter array ")
arr = input().split(' ')
prefix_array = []
prefix_array.append(int(arr[0]))
for i in range(1,len(arr)):
    prefix_array.append(int(arr[i])+int(prefix_array[i-1]))

print("Find prefix sum of range: ")
y = input()
x = [int(yy) for yy in y.split(' ')]

if x[0]>=0 and x[1]<len(arr):
    if x[0]==0:
        sum = prefix_array[x[1]-1]-prefix_array[x[0]-1]
        print("Sum: ",sum)
    else:
        sum = prefix_array[x[1]-1]-prefix_array[x[0]-2]
        print("Sum: ",sum)
else :
    print('Array values out of range')


