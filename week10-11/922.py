class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        jishu = []
        oushu = []
        res = []
        for val in A:
            if val % 2 == 0:
                oushu.append(val)
            else:
                jishu.append(val)
        cur = 0
        for i in range(len(A)):
            if (i) % 2 == 0:
                res.append(oushu[cur])
            else:
                res.append(jishu[cur])
                cur += 1
        return res

