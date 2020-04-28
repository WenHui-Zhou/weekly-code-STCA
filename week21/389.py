class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s1 = sorted(list(s))
        t1 = sorted(list(t))
        for i in range(len(s1)):
            if s1[i] != t1[i]:
                return t1[i]
        return t1[-1]
