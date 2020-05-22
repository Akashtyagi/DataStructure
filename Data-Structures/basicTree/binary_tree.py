#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 01:45:43 2020

@author: Akash Tyagi
"""

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Array to binary Tree

def array_to_tree(root, arr, i,n):
    """
    For any given I
    left-child  = 2*I+1
    right-child = 2*I+2
    parent-node = math.ceil(I/2)
    """
    # Left Child
    left_child_index = 2*i+1
    if left_child_index>=n:
        return
    root.left = Tree(arr[left_child_index])

    # right child
    right_child_index = 2*i+2
    if right_child_index >= n:
        return
    root.right = Tree(arr[right_child_index])

    array_to_tree(root.left, arr, left_child_index, n)
    array_to_tree(root.right, arr, right_child_index, n)


arr = [4,3,6,2,5,1,9]

root = Tree(-1)
root.left = Tree(arr[0])
array_to_tree(root.left, arr, 0, len(arr))

import math
def draw_tree(arr):
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
draw_tree(arr)


def printTree(root):
    if not root:
        return
    tree_order_list.append(root.data)
    if root.left:
        printTree(root.left)
    if root.right:
        printTree(root.right)
tree_order_list = []
printTree(root.left)
draw_tree(tree_order_list)

# Traversal Below Comment

"""
Recursion explanation --
 0 1 2 3 4 5 6
[4,3,6,2,5,1,9]
    4
  3   6
 2 5 1 9

4 , 0 - LEFT
    root = 4
    root.left = 3 (1)
    root.right = 6 (2)

      4
     3 6

    3, 1 - LEFT
        root = 3
        root.left = 2 (3)
        root.right = 5 (4)

            4
          3   6
         2 5
        
            2, 3 - LEFT
            root.left = None
            root.right = None
                4
              3   6
             2 5

                None - LEFT

            5, 4 - RIGHT
            root.left = None
            root.right = None
                4
              3   6
             2 5

    6, 2 - RIGHT
        root.left = 1 (5)
        root.right = 9 (6)
            4
          3    6
         2 5  1 9

""" 


# 3 Type of basic traversal - Pre-order, In-order, Post-order
# PRE-order (nlr)-  Visit yourself(n)-PRE others, then left(l), then right(r)
# IN-order  (lnr)- Visit left(l), then yourself(n) [IN between], then right(r)
# POST-order(lrn)- Visit left(l), then right(r), then yourself(n)- [POST all]


def PREorder_traversal(root):
    if not root:
        return
    pre_order_list.append(root.data)
    PREorder_traversal(root.left)
    PREorder_traversal(root.right)

draw_tree(arr)
pre_order_list = []
PREorder_traversal(root.left)
print(pre_order_list)


def INorder_traversal(root):
    if not root:
        return
    INorder_traversal(root.left)
    in_order_list.append(root.data)
    INorder_traversal(root.right)

draw_tree(arr)
in_order_list = []
INorder_traversal(root.left)
print(in_order_list)

def POSTorder_traversal(root):
    if not root:
        return    
    POSTorder_traversal(root.left)
    POSTorder_traversal(root.right)
    post_order_list.append(root.data)

draw_tree(arr)
post_order_list = []
POSTorder_traversal(root.left)
print(post_order_list)

