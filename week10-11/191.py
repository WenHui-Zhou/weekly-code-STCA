class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        
        ans,mask = 0,1
        for i in range(32):
            if n & mask:
                ans += 1
            mask <<= 1
        return ans
        """
        ans,mask = 0,1
        for i in range(32):
            if n & mask:
                ans += 1
            mask <<= 1
        return ans
