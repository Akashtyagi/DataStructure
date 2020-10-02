#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 00:46:05 2020

@author: AkashTyagi
"""

# =============================================================================
# String Regex
# =============================================================================
# Question: https://www.geeksforgeeks.org/match-a-pattern-and-string-without-using-regular-expressions/

# Backtracking

def patternMatchuntil(s,ci,pattern,pi):
    global dc
    if ci==len(s) and pi ==len(pattern):
        return True
    if ci>=len(s) or pi >=len(pattern):
        return False
    ch = pattern[pi]
    
    if ch in dc:
        temp = dc[ch]
        l = len(temp)
        
        substr = s[ci:ci+l]
        
        if substr!=temp:
            return False
        else:
            print(temp)
            return patternMatchuntil(s,ci+l,pattern,pi+1)
        
    for i in range(1,len(s)):
        dc[ch] = s[ci:i]
        
        if patternMatchuntil(s,i,pattern,pi+1):
            print(dc)
            return True
        else:
            del dc[ch]
    return False

dc = {}
patternMatchuntil("PenPaperPen", 0, "aba", 0)
        