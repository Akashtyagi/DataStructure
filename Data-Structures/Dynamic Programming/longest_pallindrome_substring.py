#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:12:19 2020

@author: AkashTyagi
"""

s = "cbbd"
l = len(s)

dp = [[False]*(l+1) for i in range(l+1)]

'''
Here, 
    row represent = Starting Index
    col represent = Ending Index
'''

for i in range(l+1):
    dp[i][i] = True

'''
Explanation for above line:
        We set all diagnoles to 1,
        we do this as all diagnoles means
        (i,i) = (1,1), (2,2) (3,3) ....
        which means string containing just 1 letter, ith letter,
        and every letter in itself is a pallindrome.
        Hence, dp[i][i] = 1
'''

'''
Concept for main looping:
    
    Suppose we have string: 'wooble'
        Now to check if this string is pallindrome,
            1) we check extreme end of the string, and compare if they are equal,
            2) If they are equal we check the string inside it is pallindrome or not.
            3) To check if inside string is pallindrome, we check 
                 increament-> starting index by 1
                 decrement -> ending index by 1
                 which lead to 
                 dp[i+1][j-1] ?
        Now we can check if this position has positive value or not.
'''

'''
We are filling the dp table from bottom to up fashion
'''
maxlen = 1
string = s[0]    
for i in range(l-1, -1, -1): # Start pointer -> end - till Zero
    for j in range(l-1, i, -1): # End pointer -> end - till start pointer
        currstr_len = j-i+1
        dp[i][j] = (s[i] == s[j])
        
        if j!=i+1: # string is not just 2 character
            dp[i][j] &= dp[i+1][j-1] # checking if inner string is pallindrome
        
        if dp[i][j] and currstr_len>maxlen:
            maxlen = currstr_len
            string = s[i:j+1]
            
print(string)            