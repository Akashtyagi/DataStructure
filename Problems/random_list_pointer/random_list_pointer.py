#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 01:23:28 2020

@author: AkashTyagi
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution1:
    def copyRandomList(self, head: 'Node') -> 'Node':
        ''' Constant Space '''
        adding =  assign = head

        while adding:
            temp = adding.next
            adding.next = Node(adding.val)
            adding.next.next = temp
            adding = adding.next.next
        
        while assign :
            if assign.random:
                assign.next.random = assign.random.next
            assign = assign.next.next
        
        newhead = head.next
        head2 = newhead
        while head2 and head2.next:
            head2.next = head2.next.next
            head2 = head2.next
        return newhead
    
    
class Solution2:
	def copyRandomList(self, head: 'Node') -> 'Node':
        ''' Using Dictionary. '''
		# Copying list without random pointer
		deepcopy = Node(x=-1, next=None, random=None)
		list1 = deepcopy
		mapping = {}
		count = 0

		while head:
			if head.random:
				newnode = Node(x=head.val, next=head.next, random = head.random)
				
			else:
				newnode = Node(x=head.val, next=head.next, random = None)
			mapping[head] = newnode
			list1.next = newnode
			list1 = list1.next
			head = head.next
			count+=1
		list2 = deepcopy
		list2 = list2.next
		while list2:
			if list2.random:
				# print(list2.random)
				list2.random = mapping[list2.random]
			list2 = list2.next
		return deepcopy.next			 
    
        

A = Node(1)
B = Node(2)
C = Node(3)

A.next = B
A.random = C

B.next = C
C.random = A

s1 = Solution1()
x = s1.copyRandomList(A)

s2 = Solution2()
xx = s2.copyRandomList(A)