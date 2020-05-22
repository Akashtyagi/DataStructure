#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:50:08 2020

@author: AkashTyagi
"""
# Question: https://leetcode.com/problems/top-k-frequent-words/


''' 
Approach:
    Use dict to find count of words
    Add words and count to heap with negative count[by-default its min-heap, 
                                                    and we want max heap]
    
    For adding words to heap:
        1. If more than 1 word have same length then
            add on basis of alphabetic increasing order (sort again).
        
    The above idea can be internally managed in heapq. [The concept above is right]
'''

import heapq


def top_k_freq_words(words,k):
    heap = []
    dc = {}
    
    for i in words:
        if i not in dc:
            dc[i]=1
        else:
            dc[i]+=1
    
    heap = [(-v,k) for k,v in dc.items()]
    heapq.heapify(heap)
    result = []
    while k>0:
        result.append(heapq.heappop(heap)[1])
        k-=1
    return result

words = ["the", "day", "is", 'aa','aa','aa',"sunny", "the", "the", "the", "sunny", "is", "is"]
k=3
print("top_k_freq_words: ",top_k_freq_words(words,k))