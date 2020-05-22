#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 21:22:24 2019

@author: AkashTyagi
"""

# =============================================================================
#         Merge Sort
# =============================================================================


#https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-8.php
def Mergesort(nlist):
    print("Spliting: ",nlist)
    
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]
        
        Mergesort(lefthalf)
        Mergesort(righthalf)
        
        i=0 # Index for lefthalf
        j=0 # Index for righthalf
        k=0 # Index for sortedlist
        print("Yaha khel hai: ",lefthalf,righthalf)
        while i<len(lefthalf) and j<len(righthalf):
            print("\tSorting: ",lefthalf[i]," ? ",righthalf[j])
            if lefthalf[i]<righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k] = righthalf[j]
                j=j+1
            k=k+1
        
        while i<len(lefthalf):
            nlist[k] = lefthalf[i]
            i=i+1
            k=k+1
            
        while j<len(righthalf):
            nlist[k] = righthalf[j]
            j=j+1
            k=k+1
        print("\t\t Sorted-> ",nlist,"\n\t")
    print("Merging: ",nlist)
    
nlist = [3,5,2,9,7,1]
Mergesort(nlist)

print("Sorted list: ",nlist)

'''
Output:

Spliting:  [3, 5, 2, 9, 7, 1]
Spliting:  [3, 5, 2]
Spliting:  [3]
Merging:  [3]
Spliting:  [5, 2]
Spliting:  [5]
Merging:  [5]
Spliting:  [2]
Merging:  [2]
Yaha khel hai:  [5] [2]
        Sorting:  5  ?  2
                 Sorted->  [2, 5] 
        
Merging:  [2, 5]
Yaha khel hai:  [3] [2, 5]
        Sorting:  3  ?  2
        Sorting:  3  ?  5
                 Sorted->  [2, 3, 5] 
        
Merging:  [2, 3, 5]
Spliting:  [9, 7, 1]
Spliting:  [9]
Merging:  [9]
Spliting:  [7, 1]
Spliting:  [7]
Merging:  [7]
Spliting:  [1]
Merging:  [1]
Yaha khel hai:  [7] [1]
        Sorting:  7  ?  1
                 Sorted->  [1, 7] 
        
Merging:  [1, 7]
Yaha khel hai:  [9] [1, 7]
        Sorting:  9  ?  1
        Sorting:  9  ?  7
                 Sorted->  [1, 7, 9] 
        
Merging:  [1, 7, 9]
Yaha khel hai:  [2, 3, 5] [1, 7, 9]
        Sorting:  2  ?  1
        Sorting:  2  ?  7
        Sorting:  3  ?  7
        Sorting:  5  ?  7
                 Sorted->  [1, 2, 3, 5, 7, 9] 
        
Merging:  [1, 2, 3, 5, 7, 9]
Sorted list:  [1, 2, 3, 5, 7, 9]

'''
        
                
        
