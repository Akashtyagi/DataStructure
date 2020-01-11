#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 19:32:01 2020

@author: Akash Tyagi
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    #### METHOD-1 ###
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        # If target-val is found at starting of list.
        while head and head.val ==val:
            head = head.next
        
        # At this moment Head will no more have target-val and can be None or other value.    
        if head is None:
            return head
        
        # We set head to a new pointer "new" and this "new" linked list will have 
        # the desired linked list .
        
        # "CURR" contain input Node values and they are compared with target-val and only
        # non-target node are added to "new"
        new,curr = head,head.next
        
        while curr: 
            while curr and curr.val == val: # If current node have target-val
                curr = curr.next
            
            new.next = curr # This valid node is added to our fresh linked list "New"
            
            if curr: 
                new = new.next
                curr = curr.next
        return head
        
      ### METHOD-2 ###
#     def removeElements(self, head: ListNode, val: int) -> ListNode:
        
#         # In this approach, valid Nodes are added to our New Dummy list
#         dummy = ListNode(-1)
#         dummy.next = head
        
#         curr = dummy
#         while curr.next != None:
#             if curr.next.val == val:
#                 curr.next = curr.next.next
#             else:
#                 curr = curr.next
#         return dummy.next
                
                
    