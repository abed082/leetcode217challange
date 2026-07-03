class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        excepted=n*(n+1)//2
        
        actual=0
        for num in nums:
            actual+=num
        return excepted-actual
        