class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count={}
        n=len(nums)
        for num in nums:
            if num in count:
                count[num]=count[num]+1
            else:
                count[num]=1
        for key in count:
            if count[key]>(n//2):
                return key
            
        