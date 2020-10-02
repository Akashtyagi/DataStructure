'''
https://leetcode.com/problems/single-number/solution/
'''

## Question: Given a non-empty array of integers, every element appears twice except for one. Find that single one. ##



# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         aldict = {}
#         st = []
        
#         for n in nums:
#             if n not in aldict:
#                 aldict[n] = 1
#                 st.append(n)
#             else:
#                 st.remove(n)
#         if len(st)>0:
#             return st[-1]
#         else:
#             return 0


## O(n) time and O(1) space complexity.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result^=num
        return result
    
    
    '''
    It is XOR operation = (^) , return 1->values are different,
                                return 0-> values are same.
    
    a (XOR) a = 0   and 
    a (XOR) 0 = a
    
    meaning XOR of value to itself will result in 0, 
        101
        101 (XOR)
        ----
        000
        
    and XOR of value to 0 will result in value,
        101
        000 (XOR)
        ---
        101
        
    and XOR of value of  any other value will return in to a new value.
        101
        100 (XOR)
        ---
        001
        
    As we saw xor to different value returns in some new value, in our loop every time XOR is happening with current   num bit values result value is modified to some new value. 
    
    This process keeps happening until the once occured value has occured again, as it will null the effect of first time occurance of that value and now the present value of result will be the because of digits present betweeen initial occuring of value and just occured value. And as repeating value keeps on occuring its value will become null and only value which didn't occur twice will remain.
    
    result = 0
    x = [5,4,3,4,5]
    
          000 (0)     101 (R)    001 (R)     010 (R)                                110 (R) 
          101 (5)     100 (4)    011 (3)     100 (4) [This 4 cancl prev 4 affect]   101 (5) [This 5 cancel previous 5 affect]
          ---         ---        ---         ---                                    ---
result =  101 (5)R    001 (1)R   010 (2)R    110 (6)R                               011 (3) <- ANSWER {as only value didn't repeat itself.}

    '''
