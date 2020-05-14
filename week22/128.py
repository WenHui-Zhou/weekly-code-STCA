class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        aset = set(nums)
        res = 0
        for i in nums:
            if i-1 not in aset:
                cur = i
                curstreak = 1
                
                while cur+1 in aset:
                    cur = cur + 1
                    curstreak += 1
                res = max(res,curstreak)
        return res
        """
        ss = set(nums)
        res = 0
        for i in ss:
            if i - 1 not in ss:
                cur = i
                cur_len = 1
                while cur + 1 in ss:
                    cur += 1
                    cur_len += 1
                res = max(res,cur_len)
        return res

