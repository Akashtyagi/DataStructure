# =============================================================================
#  Valid Paranthesis
# =============================================================================
# Question: https://www.geeksforgeeks.org/top-20-backtracking-algorithm-interview-questions/
'''

Approach
------------

BFS - Approach
1. Check if string is complete bracket or not

2. If not iterate through array and whenever come accross any bracket ,
    make new string ignoring that particular bracket and add it to queue.

3. This way we will keep adding all new possible string with 1 bracket missing 
    to queue for a single string.
    
4. Pop top from queue, repeat step 1->2->3.
'''
s = "()(v))"

def isbracket(ss):
    if ss=="(" or ss==")":
        return True
    return False

def validstring(ss):
    count = 0
    for si in ss:
        if si =="(":
            count+=1
        elif si==")":
            count-=1
        if count<0:
            return False
    return count==0


def main(s):
    queue= []
    seen = set()
    
    queue.append(s)
    seen.add(s)
    
    while queue:
        ss = queue.pop(0)
        if validstring(ss):
            print(ss)
            continue
        for i in range(len(ss)):
            if not isbracket(ss[i]):
                continue
            temp = s[:i]+s[i+1:]
            if temp not in seen:
                queue.append(temp)
                seen.add(temp)

main(s)