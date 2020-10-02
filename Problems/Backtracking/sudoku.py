#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 19:02:56 2020

@author: AkashTyagi
"""

# Sudoku

board = [ [ 3, 1, 6, 5, 7, 8, 4, 9, 2 ],
         [ 5, 2, 9, 1, 3, 4, 7, 6, 8 ],
         [ 4, 8, 7, 6, 2, 9, 5, 3, 1 ],
         [ 2, 6, 3, 0, 1, 5, 9, 8, 7 ],
         [ 9, 7, 4, 8, 6, 0, 1, 2, 5 ],
         [ 8, 5, 1, 7, 9, 2, 6, 4, 3 ],
         [ 1, 3, 8, 0, 4, 7, 2, 0, 6 ],
         [ 6, 9, 2, 3, 5, 1, 8, 7, 4 ],
         [ 7, 4, 5, 0, 8, 6, 3, 1, 0 ] ]
def subcolumn(board,row,col):
    stack = []
    xr = row//3
    xy = col//3
    # Down
    for i in range(xr*3,xr*3+3):
        for j in range(xy*3,xy*3+3):
            if i>=0 and i<len(board[0]) and j>=0 and j<len(board[0]):
                stack.append(board[i][j])
    return stack

subcolumn(board,1,7)

def checkcolumn(board,row,col,target):
    for i in range(row-1,0):
        if board[i][col]==target:
            return False
    for i in range(row+1,len(board[0])):
        if board[i][col]==target:
            return False
    return True

def sudoku(board,row,col):
    for row in range(row,len(board)):
        for col in range(col,len(board[0])):
            if board[row][col]==0:
                for p in range(1,10):
                    if p not in board[row] and checkcolumn(board,row,col,p):
                        if p not in subcolumn(board,row,col):
                            board[row][col] = p
                            if sudoku(board,row,col):
                                return True
                            else:
                                board[row][col] = 0
                return False
            if col==len(board[0])-1:
                col = 0
                
    return True

sudoku(board,0,0)
                    

    