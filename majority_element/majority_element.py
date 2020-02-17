class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # =============================================================================
        # Moore Voting Algorithm
        # =============================================================================
        '''
        *** WORKS ONLY if we have atleast 1 element in majority. ***

        We increase the count if next element is same as "Value" and 
        decrease if its different. 

        If at any case count==0 i.e "The "Value" is no more the most repetitive elem.
        Then we set current integer as "Value" and set its count = 1.

        In the end, most occuring element will be present in "Value" 
        because its count will never be 0 as it occurs more than half.
        '''
        count = 0

        for i in range(len(nums)):
            if count==0:
                value = nums[i]
                count = 1
                continue

            if value == nums[i]: 
                count+=1
            else :
                count-=1

        t = 0    
        for i in nums:
            if i == value:
                t+=1
                if t>len(nums)//2:
                    return value
