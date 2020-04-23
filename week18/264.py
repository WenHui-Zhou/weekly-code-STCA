class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0]*n
        res[0] = 1
        r2 = r3 = r5 = 0
        for i in range(1,n):
            ulgy = min(res[r2]*2,res[r3]*3,res[r5]*5)
            res[i] = ulgy
            if ulgy == res[r2]*2:
                r2 += 1
            if ulgy == res[r3] * 3:
                r3 += 1
            if ulgy == res[r5] *5:
                r5 += 1
        return res[-1]
