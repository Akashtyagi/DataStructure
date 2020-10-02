#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:38:44 2020

@author: AkashTyagi
"""

# =============================================================================
# Job Sequencing - Greedy algo 
# =============================================================================
'''
Given a set time frame every job takes,  
Each job have different deadline, 
The task is to complete jobs accordingly to maximise profit within given time frame.
'''

# Each job take 1unit time.
# Job Array - 'JobName, Job-deadline, JobProfit'  
arr =  [['a', 4, 20], 
       ['b', 1, 10], 
       ['c', 3, 40], 
       ['d', 2, 30], 
       ['e', 5, 5]] 
  
time_frame = 2

# Step 1 - Sort jobs in decreasing order of profit
# We will use Heap sort for sorting jobs
import math

def min_heap(arr,n,curr):
    minn = curr
    l = 2*curr+1
    r = 2*curr+2
    
    while l<n and arr[l][2] < arr[minn][2]:
        minn = l
    while r<n  and arr[r][2] < arr[minn][2]:
        minn = r
    
    if minn != curr:
        arr[curr],arr[minn] = arr[minn],arr[curr]
        min_heap(arr,n,minn)
    return arr

n = len(arr)
for i in range(math.ceil(n/2),-1,-1):
    min_heap(arr,n,i)
    
    
def sort_heap(arr,n):       # COMPELXITY = O(nlogn)
    while n>1:
        arr[0],arr[n-1] = arr[n-1],arr[0] # smallest element at last and last element at top
        n = n-1
        for i in range(math.ceil(n/2),-1,-1):
            min_heap(arr,n,i)
    return arr

sorted_jobs = sort_heap(arr,len(arr))
jobs_order = [0]*time_frame
suitable_jobs = []
jobs_done_so_far = 0

for job in sorted_jobs:
    time_available_for_job  = job[1]-1 
    if time_available_for_job >= time_frame:
        hour = time_frame-1  # Incase time_available_for_job is more than max-time allocated to us. It can be done at last hour.
    else:
        hour = time_available_for_job
        
    
    while hour>=0 and jobs_order[hour]!=0:
        hour-=1
        
    if hour>=0:
        jobs_order[hour] = job
        suitable_jobs.append(job)
        jobs_done_so_far += 1
        
    if jobs_done_so_far == time_frame:
        break
        
print(suitable_jobs)
    
