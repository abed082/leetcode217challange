class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen={}
        for num in nums:
            if num in seen:
                seen[num]=seen[num]+1
            else:
                seen[num]=1
        for value in seen:
            if seen[value]>=2:
                return True
            
        return False
            