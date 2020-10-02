#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 19:24:25 2020

@author: AkashTyagi
"""

'''
Resources:
    Youtube: https://www.youtube.com/watch?v=dis_c84ejhQ
    Code: https://leetcode.com/problems/course-schedule/discuss/58537/AC-Python-topological-sort-52-ms-solution-O(V-%2B-E)-time-and-O(V-%2B-E)-space
'''

"""
# =============================================================================
#                               Topological Sort
# =============================================================================

'''
Used to find out dependency order in graphs.

Suppose we have to find out order of courses, doing some course requires to 
already complete prerequisites course.

So topological sort can be used in such chaining based scenarios,
to find out.

* That kis course se start krke baki sare courses complete kiye ja sakte hai.

Complexity: O(N+M)
            N -> number of course
            M -> Internal chaining of course
            
Approach:
-----------
    These courses can be redesigned as graph, 
    [0,1] mean for course 0, take course 1 as pre-req.
    [graph-term] 0 -----> 1
    
    Step 1. For every node store the prereq courses required for it.
    Step 2. For every node count the number of courses for which current 
            course is prereq.[out-cout]
    Step 3. Form a stack with nodes on which no edge is pointing i.e such courses 
            that are pre-req of none.
    Step 4. Loop through this stack and with every iteration:
            I. Remove that node from graph,pop from stack.
            II. From courses, jiske liye ye pre-req tha, uska 
                [out-count] reduce kro.
            III. Jo naya 0 [out-count] ho vo stack me append kro.
"""

# Question: https://leetcode.com/problems/course-schedule/

numCourses = 5
prerequisites = [[0,4],[1,3],[2,0],[4,3]]
# prerequisites =[[1,0]]

dc = {i:{'prereq_for':{}, 
         'count':0, 
         } for i in range(numCourses)}

# STEP-1&2
for pair in prerequisites: 
    dc[pair[0]]['count']+=1 # Increase count, as this course req pre-req course.
    dc[pair[1]]['prereq_for'][pair[0]]=-1 # For pair[0], pair[1] pre-req hai

# Step-3
from collections import deque
stack = deque()
for i in range(numCourses):
    if dc[i]['count']==0:
        stack.append(i)

# Step-4
courses_finished = 0
while stack:
    # Step-4--I
    course = stack.popleft() 
    courses_finished += 1
    for dependent_course in dc[course]['prereq_for']:
        dc[dependent_course]['count']-=1 # Step-4--II
        if dc[dependent_course]['count']==0:
            stack.append(dependent_course) # Step-4--III
courses_finished == numCourses
        

# =============================================================================
# More Simplified Version
# =============================================================================
def canFinish(numCourses, prerequisites):
    G = [[] for i in range(numCourses)]
    degree = [0] * numCourses
    for j, i in prerequisites:
        G[i].append(j)
        degree[j] += 1
    bfs = [i for i in range(numCourses) if degree[i] == 0]
    for i in bfs:
        for j in G[i]:
            degree[j] -= 1
            if degree[j] == 0:
                bfs.append(j)
    return len(bfs) == numCourses

print(canFinish(numCourses, prerequisites))