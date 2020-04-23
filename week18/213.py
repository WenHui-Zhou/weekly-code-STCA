class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int 
        def help(nums):
            dp = [0]* len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            for i in range(2,len(nums)):
                dp[i] = max(nums[i] + dp[i-2],dp[i-1])
            return dp[-1]
        if nums == []:
            return 0
        if len(nums) <= 2:
            return max(nums)
        res = help(nums[1:])
        res = max(res,help(nums[:-1]))
        return res
        """
        if nums == []:
            return 0
        if len(nums) <= 2:
            return max(nums)

        def help(nums):
            dp = [0]*len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            for i in range(2,len(nums)):
                dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            return dp[-1]
        res = help(nums[1:])
        res = max(res,help(nums[:-1]))
        return res
        
