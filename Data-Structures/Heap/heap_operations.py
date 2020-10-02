#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun March  6 17:41:56 2020

@author: Akash Tyagi
"""

'''
Complete Binary Tree = Heap

Max Height of Complete B.T / Heap 
			ceil( log(N+1) )      <-- If root at index 1
			ceil( log(N+1) ) -1   <-- If root at index 0

Max nodes in Heap/Complete B.T -
			2**(H) -1    <-- If root at 1th position
			2**(H+1) -1  <-- If root at 0th position
'''

import math
arr = [4,6,1,2,9,8,4,2]


def draw_heap(arr):
    n = len(arr)
    h = math.ceil(math.log2(n))
    z = int(n/2)
    print(("  "*z),arr[0])
    k = 1
    i = 1
    while k<=h:
        print()
        s = ''
        for j in arr[i:i+2**(k)]:
            s = s + str(j) + '  '*(z-1)
        print(("  ")*(z-k),s)
        z = z-k
        i+=2**k
        k+=1
    print("----------------")
draw_heap(arr)


# Build a maxheap. 
def max_heapify(arr,n,curr):
    ''' 
    Creating max-heap in O(n) time
    
	For any node at index I:
	
	left-child index  = 2*I + 1
	right-child index = 2*I + 2
	parent-node index = floor(I/2)
    '''
    
    largest = curr
    l = 2*curr+1
    r = 2*curr+2
    
    print("Input-heap  ,Targeting heap with head - ",arr[curr])
    print(arr)
    draw_heap(arr)
    
    if l<n and arr[l]>arr[largest]:
        largest = l
    if r<n and arr[r]>arr[largest]:
        largest = r
    
    if largest != curr:
        arr[curr],arr[largest] = arr[largest],arr[curr]
        print("Change occured - ")
        draw_heap(arr)
        max_heapify(arr,n,largest)

arr = [4,6,1,2,9,8,4,2]   
n = len(arr) 
for i in range(math.ceil(n/2)-1, -1, -1): 
    max_heapify(arr, n, i) 
    

# Build a minheap. 
def min_heapify(arr,n,curr):
    minn = curr
    l = 2*curr+1
    r = 2*curr+2
    
    print("Input-heap  ,Targeting heap with head - ",arr[curr])
    print(arr)
    draw_heap(arr)
    
    if l<n and arr[l]<arr[minn]:
        minn = l
    if r<n and arr[r]<arr[minn]:
        minn = r
    if minn != curr:
        arr[curr],arr[minn] = arr[minn],arr[curr]
        print("Change occured - ")
        min_heapify(arr,n,minn)
        
arr = [4,6,1,2,9,8,4,2]   
n = len(arr) 
for i in range(math.ceil(n/2)-1, -1, -1): 
    min_heapify(arr, n, i) 
    

# Heap Insertion    
def insert_to_heap(arr,new_num):
    '''
    Insert a new element at last of already sorted heap, 
    and then manages heap acc to its weight.
    '''
    print("Number to be inserted: ",new_num)
    draw_heap(arr)
    arr.append(new_num)
    n = len(arr)
    for i in range(math.ceil(n/2)-1, -1, -1): 
        max_heapify(arr, n, i) 
    print("Heap has been sorted")
    draw_heap(arr)
    
arr = [4,6,1,2,9,8,4,2]   
for i in range(math.ceil(n/2)-1, -1, -1): 
    max_heapify(arr, n, i) 
draw_heap(arr)
insert_to_heap(arr,7)
draw_heap(arr)
    

# Heap Removal
def remove_from_heap(arr):
    '''
    Only root is removed, just like queue or stack.
    '''
    arr[0] = arr[len(arr)-1]
    arr.pop(len(arr)-1)
    for i in range(math.ceil(n/2)-1, -1, -1): 
        max_heapify(arr, n, i) 
    draw_heap(arr)
    
remove_from_heap(arr)



# =============================================================================
#  Example of Heap Sort = Priority Queue
# =============================================================================

'''
Priority of different Vehicles
Ambulance = 1
Government Vehicles = 2
Normal Vehicles = 3
Transport Vehicles = 4
'''

# Make such a structure where traffic follow queue order, as well as priority

veh_priority = {"amb":1,
                "gov":2,
                "norm":3,
                "trans":4
                }
def min_heap(arr, n, curr):
    minn = curr
    l = 2*curr+1
    r = 2*curr+2
    
    if l<n and veh_priority[arr[l]] < veh_priority[arr[minn]]:
        minn = l
    if r<n and veh_priority[arr[r]] < veh_priority[arr[minn]]:
        minn = r
    
    if minn!=curr:
        arr[curr],arr[minn] = arr[minn],arr[curr]
        min_heap(arr,n,minn)
        
def vehicle_priority(arr):
    n = len(arr)
    for i in range(math.ceil(n/2)-1, -1, -1):
        min_heap(arr,n,i)
    for i in arr:
        print(i)
        
arr = ['trans','norm','norm','gov','amb']
vehicle_priority(arr)

