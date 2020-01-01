class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not g or not s:
            return 0
        g = sorted(g)
        s = sorted(s)

        result = 0
        jj = 0
        for ii in g:
            while jj < len(s):
                if s[jj] >= ii:
                    s[jj] = -1
                    result += 1
                    break
                jj += 1
            jj += 1
        return result