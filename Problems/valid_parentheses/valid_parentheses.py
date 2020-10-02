# https://leetcode.com/problems/valid-parentheses/

# Question: Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

class Solution(object):
    def isValid(self, s):
        stack = []
        brackets = {"{":"}","[":"]","(":")"}
        openb = set(['(','{','['])
        
        for x in s:
            if x in openb:
                stack.append(x)
            elif len(stack)>0 and brackets[stack[-1]] == x:
                stack.pop()
            else:
                return False
        return stack==[]
            


