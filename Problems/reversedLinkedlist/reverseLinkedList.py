# Definition for singly-linked list.  Question 
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Recursive
class Solution:
    def reverse(self,head,pointer):
        if head.next is None:   # Check if last Node in list
            return head,head
        
        curr,pointer = self.reverse(head.next,pointer)
        head.next.next = head
        head.next = None
        return head,pointer
        
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        _,head = self.reverse(head,None)
        return head


'''
Example:  List = [1,71] [2,72] [3,73] [4,74] [5,None]

>Line 19
>Line 21 
-> Line 9  head = [1,71], pointer=None
-> Line 13 --Further Inside -- {head.next}      --Call I
->-> Line 9  head = [2,72], pointer=None
->-> Line 13 --Further Inside -- {head.next}    --Call II
->->-> Line 9  head = [3,73], pointer=None
->->-> Line 13 --Further Inside -- {head.next}  --Call III
->->->-> Line 9  head = [4,74], pointer=None
->->->-> Line 13 --Further Inside -- {head.next}  --Call IV
->->->->-> Line 9  head = [5,None], pointer=None
->->->->-> Line 10 TRUE
->->->->-> Line 11 return ([5,None],[5,None])
#--#--#--#--#--#--Returning All function calls--#--#--#--#--#--#
->->->-> Line 13 curr= [5,None], pointer= [5,None], head= [4,74] --Call III
->->->-> Line 14 [5,74]
->->->-> Line 15 head=[4,None]
->->->-> Line 16 return [4,None],[5,74]  {Pointer changed in line 42}
->->-> Line 13 curr= [4,None], pointer= [5,74], head= [3,73] --Call II
->->-> Line 14 [4,73]
->->-> Line 15 head=[3,None]
->->-> Line 16 return [3,None],[5,74]
->-> Line 13 curr= [3,None], pointer= [5,74], head= [2,72] --Call I
->-> Line 14 [3,72]
->-> Line 15 head=[2,None]
->-> Line 16 return [2,None],[5,74]
-> Line 13 curr= [2,None], pointer= [5,74], head= [1,71] --Call 0
-> Line 14 [2,71]
-> Line 15 head=[1,None]
-> Line 16 return [1,None],[5,74]
> Line 21 head [5,74]
Line 22 [5,74]

[5,74]-[4,73]-[3,72]-[2,71]-[1,None]  { Reversed }






#     #Iteration
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         previous = next_ = None
#         while head:
#             next_ = head.next
#             head.next = previous
#             previous = head
#             head = next_
#         return previous
''' 
            
