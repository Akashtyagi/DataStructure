#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 18:57:18 2020

@author: AkashTyagi
"""

# =============================================================================
# Non-recursive merge sort
# =============================================================================

'''
In this, we sort the list by making pairs in the form of 1,2,4,8,16.

Means as we move forward in list first we sort list of size 1.
Then in 2nd iteration, we sort list of size 2,
Then in 3rd iteration, we sort list of size 4... so on.

So at last we have a sorted list .
Complexity - O(nlogn)

Youtube - https://www.youtube.com/watch?v=WVl2QSe4R14&feature=youtu.be
'''

class Node:
    def __init__(self, x: int, next: 'Node' = None):
        self.val = int(x)
        self.next = next

def printlist(message,head):
    print(message)
    while head:
        print(head.val,end="->")
        head = head.next
    print("\n")

def non_recursive_merge(head):
    
    if not head or not head.next:
        return head
    
    def split(head,l):
        ''' 
        Iterate list till "l" and return the next Node after "L" elements.
        '''
        count = 1
        while count<l and head:
            count+=1
            head = head.next
        if not head:
            return None # End of list
        temp = head.next # Next elem
        head.next = None # Disconnect the list till temp, so it can be sorted.
        return temp

    
    def mergesort(l,r,sublist):
        head = sublist
        printlist("Left: ",l)
        printlist("right: ",r)
        while l and r:
            if l.val<r.val:
                head.next = l
                l = l.next
            else:
                head.next = r
                r = r.next
            head = head.next
            
        head.next = l if l else r # Add remaining bigger list.
        printlist("After merging: ",sublist)
        while head.next: # reaching till end
            head = head.next
        return head # the last element of l/r

    sublength = 1 # Length to list to sort 
    dummy = Node(-1)
    dummy.next = head
    
    # Length of list
    h1 = head
    size = 0
    while h1: 
        size+=1
        h1 = h1.next
    print("Length of input list: ",size)
    
    l,r,sublist = None,None,None    
    
    while sublength<size:
        print("\nFor sublength: ",sublength)
        curr = dummy.next
        sublist = dummy
        
        while curr:
            l = curr # current pointer
            r = split(l,sublength) # From current to size=sublength.
            curr = split(r,sublength) # Remaining list.
            sublist = mergesort(l,r,sublist)
        sublength<<=1 # left shift by 1, means 1,2,4,8
    return dummy.next       
    
x = [5,3,7,6,2,4]
# Sorted = [2,3,4,5,6,7] 


a = Node(5)    
b = Node(3)
a.next = b
c = Node(7)
b.next = c
d = Node(6)
c.next = d
e = Node(2)
d.next = e
f = Node(4)
e.next = f


z = non_recursive_merge(a)


'''
Output

Length of input list:  6

For sublength:  1
Left: 
5->

right: 
3->

After merging: 
-1->3->5->

Left: 
7->

right: 
6->

After merging: 
5->6->7->

Left: 
2->

right: 
4->

After merging: 
7->2->4->


For sublength:  2
Left: 
3->5->

right: 
6->7->

After merging: 
-1->3->5->6->7->

Left: 
2->4->

right: 


After merging: 
7->2->4->


For sublength:  4
Left: 
3->5->6->7->

right: 
2->4->

After merging: 
-1->2->3->4->5->6->7->
'''
        

