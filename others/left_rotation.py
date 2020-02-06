#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 19:37:16 2019

@author: AkashTyagi
"""

# https://www.hackerrank.com/challenges/array-left-rotation/problem

# Shift array to its left N times

# =============================================================================
# Input :
#     First line : n d   [ n->no. of integers, d-> no. of left rotation ]
#     Second line: array that has to shifted
# =============================================================================


#firstline = input()
#secondline = input()
#
#N = int(firstline.split(' ')[0])
#d = int(firstline.split(' ')[1])
#
#arr = [int(x) for x in secondline.split(' ')]

firstline = '5 2'
secondline = '1 2 3 4 5'

N = int(firstline.split(' ')[0])
d = int(firstline.split(' ')[1])

arr = [int(x) for x in secondline.split(' ')]

arrlen = len(arr)
rightrotation = arrlen - d

newarr = [0]*arrlen
index = 0
while index<arrlen:
    frmula = (index+rightrotation)%arrlen
    newarr[frmula]=arr[index]
    index+=1
    
print(newarr)