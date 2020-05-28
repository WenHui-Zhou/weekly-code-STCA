class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        if len(nums) == 1:
            return nums[0]
        tmp = 0
        res = -sys.maxsize
        for i in range(len(nums)):
            if tmp + nums[i] < 0:
                res = max(nums[i],res)
                tmp = 0
            else:
                tmp += nums[i]
                res = max(res,tmp)
        return res
        """
        if nums == []:
            return 0
        import sys
        res = -sys.maxsize
        tmp = 0
        for val in nums:
            if tmp + val < 0:
                res = max(val,res)
                tmp = 0
            else:
                tmp += val
                res = max(res,tmp)
        return res
