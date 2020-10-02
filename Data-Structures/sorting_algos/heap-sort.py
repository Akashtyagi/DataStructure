#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 12:52:11 2020

@author: Akash Tyagi
"""
import math
def max_heapify(arr,n,curr):
    ''' 
    Complexity =  O(n)    
	
	For any node at index I:	
	left-child index  = 2*I + 1
	right-child index = 2*I + 2
	parent-node index = floor(I/2)
    '''
    largest = curr
    l = 2*curr+1
    r = 2*curr+2
    
    if l<n and arr[l]>arr[largest]:
        largest = l
    if r<n and arr[r]>arr[largest]:
        largest = r
    
    if largest != curr:
        arr[curr],arr[largest] = arr[largest],arr[curr]
        max_heapify(arr,n,largest)
    
    
def sort_heap(arr,n):       # COMPELXITY = O(nlogn)
    while n>1:                
        for i in range(math.ceil(n/2),-1,-1):
            max_heapify(arr,n,i)
        arr[0],arr[n-1] = arr[n-1],arr[0] # smallest element at last and last element at top
        n = n-1
    return arr

if __name__ == '__main__':
	arr = [1,5,13,0,8,4,2]
	print("Input array: ",arr)
	print("Sorted array: ",sort_heap(arr,len(arr)))
