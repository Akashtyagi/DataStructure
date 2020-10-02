#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 01:13:09 2020

@author: Akash Tyagi
"""

#Question: 
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null

# 2 Approaches -> Using Extra Mem, without Extra Memory, Just pointers

### Using pointers
'''
https://www.youtube.com/watch?v=-YiQZi3mLq0
Assumptions
1. Lets assume a point where cycle starts and distance from start of link list to this point be D.
2. From the point of D, lets assue Hare & Tortoise pinter meet at point "Meeting Point" which is at distance K from D.
3. Length of Cycle part = C
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
	hare = tortoise = head
		
	if head==None or head.next==None:
	    return None

	while hare.next and hare.next.next:
	    hare = hare.next.next
	    tortoise = tortoise.next
	    
	    if hare.next == tortoise.next: # Meeting point
		p1 = head
		p2 = tortoise
		while(p1!=p2):
		    p1 = p1.next
		    p2 = p2.next
		return p1 # Point where Cycle Begins
	return None

### Using Extra Memory
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        nodes = {}
        nodes[head] = 1
        while head:
            if head.next in nodes:
                return head.next
            nodes[head.next] = 1
            head = head.next
