#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 23:04:34 2020

@author: AkashTyagi
"""

# =============================================================================
# Morris Traversal
# =============================================================================


class TreeNode:
    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None
        
head = TreeNode(1)
head.left = TreeNode(2)
head.left.left = TreeNode(3)
head.left.right = TreeNode(4)
head.right = TreeNode(5)
head.right.right = TreeNode(6)

'''
        1
      /   \
     2     5
   /   \     \
  3     4     6
 '''
 
# =============================================================================
#  Inorder Traversal
# =============================================================================

head2 = TreeNode(1)
head2.left = TreeNode(2)
head2.left.left = TreeNode(4)
head2.left.right = TreeNode(5)
head2.left.left.left = TreeNode(8)
head2.left.left.right = TreeNode(9)
head2.right = TreeNode(3)
head2.right.right = TreeNode(7)

def morris_inorder(curr):
    while curr:
        if curr.left is None:
            print(curr.val)
            curr = curr.right
        else:
            temp = curr.left
            while temp.right and temp.right != curr:
                temp = temp.right
                
            if temp.right is None:
                temp.right = curr
                curr = curr.left
                
            elif temp.right==curr:
                temp.right = None
                print(curr.val)
                curr = curr.right
            
morris_inorder(head)
morris_inorder(head2)
