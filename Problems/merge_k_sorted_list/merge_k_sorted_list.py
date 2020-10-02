#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 09:30:57 2019

@author: Akash Tyagi
"""

# https://leetcode.com/problems/merge-k-sorted-lists/

# =============================================================================
# Question : Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
# =============================================================================

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# My Older approach
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        new = copy = ListNode(0)
        if len(lists)==0:
            return None
        while len(lists)>1:
            minn = None
            t = None
            z = []
            for i in range(len(lists)):
                if lists[i] is None:
                    z.append(i)
                    continue
                if t is None:
                    minn = lists[i].val
                    t = i
                else:
                    if lists[i].val<minn:
                        minn = lists[i].val
                        t = i
            if t is None:
                return None
            new.next = lists[t]
            new = new.next
            if lists[t].next is not None:
                lists[t] = lists[t].next
            else:
                z.append(t)
#            if lists[t] is None:
 #               lists.(pop(t))
            for i in range(len(z)-1,-1,-1):
                lists.pop(z[i])

        if len(lists) == 0 or lists[0] is None:
            return copy.next or None
        new.next = lists[0]                
        return copy.next or None

#Best Approach
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return 
        if len(lists) == 1:
            return lists[0]
        mid = len(lists)//2
        print("l: ",lists[:mid])
        print("r: ",lists[mid:])
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        #print("LEft",l,"\n",r)
        return self.merge(l, r)

    def merge(self, l, r):
        dummy = cur = ListNode(0)
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l or r
        return dummy.next
    
'''
## Explanation

Refer to Merge 2 sorted list for better understanding.

Lets suppose:
    Input:
            [
              1->4->5,
              1->3->4,
              2->6
            ]
            
First Iteration:
    lists = [[1,4,5],[1,3,4],[2,6]]
    mid = 1
    
    l = mergeKlists([[1,4,5]]) 
      ** Sub Loop **
            lists = [[1,4,5]]
            len(lists) = 1
      <---- return [1,4,5]
    l = [1,4,5]
    
    r = mergeKlists([1,3,4],[2,6]])
      ** Sub Loop **
            lists = [[1,3,4],[2,6]]
            l = mergeKlists([[1,3,4]])
                ** Sub Loop **
                    lists = [[1,3,4]]
                    len(lists) = 1
                <-- return [1,3,4]
            l = [1,3,4]
            
            r = mergeKlists([[2,6]])
                ** Sub Loop **
                    lists = [2,6]
                <-- return [2,6]
            r = [2,6]
            
            l = [1,3,4]
            r = [2,6]
            
      <---- return self.merge([1,3,4],[2,6]) = [1,2,3,4,6]
      
      l = [1,4,5]
      r = [1,2,3,4,6]
      
      self.merge([1,4,5],[1,2,3,4,6])
      
      OUTPUT = [1,2,3,4,5,6]
'''
            
               
            
