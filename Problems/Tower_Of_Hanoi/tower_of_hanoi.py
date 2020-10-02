#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:40:40 2020

@author: AkashTyagi
"""

# =============================================================================
# Tower of Hanoi
# =============================================================================


'''
    |   |   |
    |   |   |
    |   |   |
   --- --- ---
    A   B   C
    
For 1 Disk:
    If just 1 disk was there
        Move directly from A to C
        
For 2 Disk:
    If just 2 disk were to move,
        1. Move A to C [Recurive]
        2. Move directly from A to C 
        3. Move B to C [Recursive]

For 3 Disk:
    If 3 Disk were to move,
    1. Move A to C [recurisve]
    2. Move directly from A to C
    3. Move B to C [using func for 2 Disk]


Nomenclature:
    function = TOH(n, A, C, B)  # From A, To C, Using B
    
**    1 Disk:
        TOH(1,A,B,C):
            Move directly from A to C

**    2 Disk:
        TOH(2,A,B,C):
            TOH(1,A,C,B) # From A, To C, Using B
            Move directly from A to C 
            TOH(1,B,C,A) # From B, To C, Uisng A

**    n Disk:
        TOH(n,A,B,C):
            TOH(n-1,A,C,B)
            Move directly from A to C
            TOH(n-1,B,C,A)
'''


first_pipe = 'A'
second_pipe = 'B'
third_pipe = 'C'
n = 3

def tower_of_hanoi(n,first_pipe,second_pipe,third_pipe):
    '''
    Move all disk from first_pipe --> third_pipe
    '''
    
    if n>0:
        tower_of_hanoi(n-1,first_pipe,third_pipe,second_pipe)
        print(f"Move from {first_pipe} to {third_pipe}")
        tower_of_hanoi(n-1,second_pipe,third_pipe,first_pipe)

tower_of_hanoi(4, first_pipe, second_pipe, third_pipe)
