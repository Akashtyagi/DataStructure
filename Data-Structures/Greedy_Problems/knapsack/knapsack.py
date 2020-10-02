#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 16:48:55 2020

@author: AkashTyagi
"""

# =============================================================================
# KnapSack Problem
# =============================================================================

'''
This is one of the greedy problems, as here we have to MAXIMIZE our profit within some contraint(max. capacity)

There are 2 types of Knapsack problem. 
    I. Where content division is allowed.
   II. Where content division is not allowed.
   
The code below is for case where content divison is not allowed.

This is a DYNAMIC PROGRAMMING approach !!!!!

My first ever DP code.
'''

# =============================================================================
#  Tabular method of solving Knapsack problem
#      Step 1. Create a profit/object matrix 
#      Step 2. Identify which object contributes to maximum profit.
# =============================================================================

# =============================================================================
# Formula: max(matrix[curr_row-1][curr_space_available],
#              matrix[curr_row-1][curr_space_available - weights[curr_row-1]] + profit[curr_object-1])
# # =============================================================================

def knapscak_tabular(weights,profits,max_capacity):
    # A metrix of Object(rows)*Capacity(columns)
    import numpy as np # for metrix creation
    matrix = np.zeros( (len(weights)+1,max_capacity+1),dtype=int)
    
    # curr_object iteration
    for curr_object in range(1,matrix.shape[0]): 
        # Space avaialbel in sack
        for curr_space_available in range(1,matrix.shape[1]): 
            if weights[curr_object-1] > curr_space_available:
                matrix[curr_object][curr_space_available] = matrix[curr_object][curr_space_available-1]
                
            elif curr_space_available-weights[curr_object-1]<0:
                matrix[curr_object][curr_space_available] = matrix[curr_object][curr_space_available-1]
                
            else:
                matrix[curr_object][curr_space_available] = max(matrix[curr_object-1][curr_space_available],matrix[curr_object-1][curr_space_available-weights[curr_object-1]]+profits[curr_object-1])
    
    objects = len(weights)
    column = matrix.shape[1]-1
    
    object_needed = [0]*objects
    total_weight = 0
    profit = matrix[objects][column]
    
    while objects>0 :
        if profit > matrix[objects-1][column]:
            object_needed[objects-1] = 1
            profit = profit - profits[objects-1]
            total_weight+=weights[objects-1]
        elif profit != matrix[objects-1][column]:
            for j in range(matrix[objects-1]):
                if matrix[objects-1][j] == profit:
                    column = j
        objects-=1
            
    profit = 0
    capacity = 0
    for item in range(len(object_needed)):
        if object_needed[item] == 1:
            capacity+=weights[item]
            profit+=profits[item]
            print(f" Object with weight {weights[item]} added to bucket. Weight - {capacity}  Profit - {profit}")
    print(f"\nResult:  Total weight: {capacity}  & Total Profit: {profit}")
    
if __name__=="__main__":
    weights = [4,2,6,5,3] # Weight of objects
    profits = [8,1,4,2,6] # profit of objects
    max_capacity = 9  # Maximum capacity of Sack.
    print("Max Capacity available- ",max_capacity,"\n")
    knapscak_tabular(weights,profits,max_capacity)

        
        
 
    
    