class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        cur = 0
        res = 0
        for val in g:
            while cur < len(s):
                if s[cur] >= val:
                    res += 1
                    cur += 1
                    break
                else:
                    cur += 1
        return res
