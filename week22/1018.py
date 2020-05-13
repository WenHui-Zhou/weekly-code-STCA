class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        if A == []:
            return []
        res = []
        ans = A[0]
        if ans % 5 == 0:
            res.append(True)
        else:
            res.append(False)
        for val in A[1:]:
            ans *= 2
            ans += val
            if ans % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res


