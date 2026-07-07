class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix=0
        max_len=0
        sum_map={0:-1}
        for i in range(len(nums)):
            if nums[i]==0:
                prefix+=-1
            else:
                prefix+=1
            if prefix in sum_map:
                max_len=max(max_len,i-sum_map[prefix])
            else:
                sum_map[prefix]=i
        return max_len