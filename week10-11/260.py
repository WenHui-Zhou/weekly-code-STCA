class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        amap = Counter(nums)
        return [x for x in amap if amap[x] == 1]
