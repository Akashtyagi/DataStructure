#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 16:05:43 2020

@author: Akash Tyagi
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
            
if __name__ == "__main__":
    root = Node(6)
    root.insert(3) # Left of 6
    root.insert(9) # Right of 6
    root.insert(2) # left of 3
    root.insert(10) # Right of 9
    root.printTree()
    
    
        