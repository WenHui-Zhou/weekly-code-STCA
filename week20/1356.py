class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def count_1(n):
            tmp = 0
            while n > 0:
                if n & 1 == 1:
                    tmp += 1
                n >>= 1
            return tmp
        res = []
        for val in arr:
            tmp = [count_1(val),val]
            res.append(tmp[::])
        res.sort(key = lambda x:(x[0],x[1]))
        ans = []
        for val in res:
            ans.append(val[1])
        return ans
