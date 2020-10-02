#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 00:34:03 2020

@author: AkashTyagi
"""

# =============================================================================
# Kinght Tour
# Problem: https://www.geeksforgeeks.org/the-knights-tour-problem-backtracking-1/
# =============================================================================

board = [[-1]*8 for i in range(8) ]

'''
Knight move
1. X+2,Y+1
2. X+2, Y-1
3. X-2, Y+1
4. X-2, Y-1

5. Y+2, X+1
6. Y+2, X-1
7. Y-2, X+1
6. Y-2, X-1
'''


move_x = [2, 1, -1, -2, -2, -1, 1, 2] 
move_y = [1, 2, 2, 1, -1, -2, -2, -1] 

def check(board,row,col,pos):
    global moves
    if pos==len(board)**2:
        print(board)
        return True,board
    if pos>=62:
        print(f"check({row},{col},{pos},{board}")
    for i in range(8):
        tr = row+move_x[i]
        tc = col+move_y[i]
        if tr<0 or tr>len(board)-1 or tc<0 or tc>len(board)-1:
            continue
        elif board[tr][tc]==-1:
            board[tr][tc]=pos
            # print(f"check({tr},{tc},{pos}")
            result,board = check(board,tr,tc,pos+1)
            if result==True:
                return True,board
            else:
                board[tr][tc]=-1
    # board[row][col]=-1
    return False,board

            
    
def knight(board):
    for i in range(len(board)):
        for j in range(len(board)):
            board[i][j] = 1
            result,finalboard = check(board,i,j,1)
            if result==True:
                return finalboard
            else:
                board[i][j]=-1

# knight(board)
board[0][0] = 0
result,finalboard = check(board,0,0,1)