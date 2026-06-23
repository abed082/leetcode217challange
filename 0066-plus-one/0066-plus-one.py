class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1]<9:
            digits[-1]+=1
        else:
            if len(digits)==1:
                digits=[1,0]
            else:
                digits=self.plusOne(digits[:-1])+[0]
        return digits

        