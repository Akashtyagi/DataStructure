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
        
                
        
