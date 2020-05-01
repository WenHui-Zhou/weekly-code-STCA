class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        res = 0
        for i in range(1,len(s)):
            res = max(res,s[:i].count('0') + s[i:].count('1'))
        return res

