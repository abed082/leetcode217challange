class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=0
        for num in nums:
            if nums.count(num)==1:
                total+=num
        return total
