class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        cur = 0
        cur_right = 0
        max_right = 0
        res = 0
        if len(nums) == 1:
            return 0
        while cur <= max_right:
            max_right = max(cur+nums[cur],max_right)
            if max_right >= len(nums) - 1:
                return res + 1
            if cur >= cur_right:
                res += 1
                cur_right = max_right
            cur += 1
            
        dp = [len(nums)] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            for step in range(1,nums[i]+1):
                if i +step >= len(dp):
                    return dp[-1]
                dp[i + step] = min(dp[i+step],dp[i] + 1)
 #           print(dp)
 #       print(dp)
        return dp[-1]
        """
        cur = 0
        cur_right = 0
        max_right = 0
        res = 0
        if len(nums) == 1:
            return 0
        while cur <= max_right:
            max_right = max(max_right,nums[cur] + cur)
            if max_right >= len(nums) -1:
                return res + 1
            elif cur >= cur_right:
                res += 1
                cur_right = max_right
            cur += 1
                    
