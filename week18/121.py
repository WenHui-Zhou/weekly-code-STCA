class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        import sys
        minp = sys.maxsize
        res = 0
        for i in prices:
            if i < minp:
                minp = i
            elif res < i - minp:
                res = i - minp
        return res
        min_val = sys.maxsize
        res = 0
        for val in prices:
            if min_val > val:
                min_val = val
            res = max(res,val - min_val)
        return res
        """
        min_val = sys.maxsize
        res = 0
        for val in prices:
            if min_val > val:
                min_val = val
            res = max(res,val - min_val)
        return res
