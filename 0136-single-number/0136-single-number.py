class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        abed=0
        for num in nums:
           abed= abed^num
        return abed

        