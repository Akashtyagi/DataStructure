#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 23:30:47 2019

@author: Akash Tyagi
"""

#https://leetcode.com/problems/merge-two-sorted-lists/

# =============================================================================
# Question: Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
# =============================================================================


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new = copy = ListNode(0)
        
        while l1 is not None and l2 is not None:
            if l1.val<l2.val:
                new.next = l1
                l1 = l1.next
            else:
                new.next = l2
                l2 = l2.next
            new = new.next
        new.next = l1 or l2
        return copy.next
            
'''
Explanation:
    Here a new Linked list is created and then both the existing lists node values
    are compared abd smaller one is added to the new list.
    
    This process is done until one of the linked list get exhausted.
    
'''
