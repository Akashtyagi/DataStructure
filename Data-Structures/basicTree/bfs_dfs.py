#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 22:33:30 2020

@author: AkashTyagi
"""

class Tree:
    def __init__(self, data, left_data=None, right_data=None):
        self.data = data
        self.left = left_data
        self.right = right_data
        
a1 = Tree(3)
a2 = Tree(1)
a3 = Tree(5)
a4 = Tree(7)
a5 = Tree(8)
a6 = Tree(2)
a7 = Tree(9)

a1.left = a2
a1.right = a3
a2.left = a4
a2.right = a5
a3.left = a6
a3.right = a7


# Supposing it is a tree.
'''
        3
    1        5
  7   8    2   9

BFS - Traveling in tree level by level. == 3-> 1-> 5-> 7-> 8-> 2-> 9
DFS-  Traveling in tree depth first     == 3-> 1-> 7-> 8-> 5-> 2-> 9
'''

def bfs(root):
    '''
        BFS: Breadth First Search
        In BFS, tree/Graph is traversed level by level.
        Uses - Queue
        
        Step 1- Take Element, process operation to it.
        Step 2- Add element to the "seen" list.
        Step 3- Add its child to queue.
        Step 4- Pop first element from the queue, GOTO step 1.
    '''
    queue = []
    seen = set()
    
    queue.append(root)
    
    while queue:
        element = queue[0] # FIFO
#        if element is None:
#            return
        if element in seen:
            queue.pop(0) # Element has already been processed
            continue
        print(element.data) # Operation on element
        seen.add(element)
        if element.left:
            queue.append(element.left)
        if element.right:
            queue.append(element.right)
        queue.pop(0)
        
print("BFS: ")
bfs(a1)

def dfs(root):
    '''
        BFS: Breadth First Search
        In BFS, tree/Graph is traversed level by level.
        Uses - Queue
        
        Step 1- Take Element, process operation to it.
        Step 2- Add element to the "seen" list.
        Step 3- Add its child to stack.
        Step 4- Pop first element from the stack, GOTO step 1.
    '''
    stack = []
    seen = set()
    
    stack.append(root)
    while stack:
        element = stack[-1] #LIFO

        if element in seen:
            stack.pop() # Element has already been processed
            continue
        print(element.data)
        seen.add(element)
        stack.pop()
        if element.right:
            stack.append(element.right) # order can be reversed, we can add left first too.
        if element.left:
            stack.append(element.left)
        
print("DFS: ")
dfs(a1)