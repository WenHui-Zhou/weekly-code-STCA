class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        from collections import defaultdict
        amap = defaultdict(int)
        res = 0
        for t in time:
            if t%60 in amap:
                res += amap[t%60]
            if t % 60 == 0:
                amap[0] += 1
            amap[60 - t%60] += 1
        return res


