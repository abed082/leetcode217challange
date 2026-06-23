class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        element=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[element]=nums[i]
                element+=1
        return element

