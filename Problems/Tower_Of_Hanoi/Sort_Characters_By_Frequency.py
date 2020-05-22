#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:35:37 2020

@author: AkashTyagi
"""

# Question: https://leetcode.com/submissions/detail/343019014/
'''
Simple solution using dictionary and array.

1. Store count of every word in dictionary. [Intentially Avoided using inbuilt counter function]
2. Transfer dictionary into a temporaray array with its frequency.
3. Reverse sort on basis of frequency.
4. Join sorted array.

For Follow Up:


1. .... 
2. ....
3. Reverse sort on basis of frequency.
4. If multiple sorted element have same frequency, sort them again of basis of "*char*".
5. Join the resulted array.
'''

class Solution:
    def frequencySort(self, s: str) -> str:   
    	dc = {}
    	temp = []
    	result = ''
    	
    	# Store freqency of chars
    	for i in s:
    		if i not in dc:
    			dc[i] = 1
    		else:
    			dc[i]+=1
    	
    	# Transfer dict to array
    	for i in dc:
    		temp.append([dc[i],i])
    	
    	# Basic solution LAST STEP
    	sort_string = sorted(temp,reverse=True)
    	
    	# --------------------------FOLLOW UP ----------------------------------------------------
    	count = sort_string[0][0]  # Store freq of sorted char
    	subarray = [sort_string[0][1]] # Subarray of similar freq characters
    	
    	i = 1
    	l = len(sort_string)
    	
    	while True:
    		while i<l and sort_string[i][0]==count: # Multiple char of similar freq
    			subarray.append(sort_string[i][1])
    			i+=1
    		if len(subarray)>1:
    			subarray.sort()
    		for w in subarray:
    			result+=str(w*count)
    		if i<l-1: # Terminating condition
    			count = sort_string[i][0]
    			subarray = [sort_string[i][1]]
    			i+=1
    		else:
    			break
    	print(result)
