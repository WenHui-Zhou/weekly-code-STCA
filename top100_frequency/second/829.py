class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        res,i = 0,1
        while N>0:
            res += N%i == 0
            N -= i
            i += 1
        return res
