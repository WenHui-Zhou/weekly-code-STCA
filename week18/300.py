class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        if nums == []:
            return 0
        res = [1]*len(nums)
        for ii in range(len(nums)):
            for jj in range(ii):
                if nums[jj] < nums[ii]:
                    res[ii] = max(res[ii],res[jj]+1)
        return max(res)
        """
        if nums == []:
            return 0
        dp = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1,dp[i])
    #    print(dp)
        return max(dp)
