class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count={}
        if len(s)!=len(t):
            return False
        for char in s:
            count[char]=count.get(char,0)+1
        for char in t:
            count[char]=count.get(char,0)-1
        for val in count.values():
            if val!=0:
                return False
        return True
            
        