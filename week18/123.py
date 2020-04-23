class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        max_pro = 0
        
        def get_pro(nums):
  #          print(nums)
            if len(nums) < 2:
                return 0
            min_val = nums[0]
            res = 0
            for i in nums:
                if  i < min_val:
                    min_val = i
                elif i - min_val > res:
                        res = i - min_val
        #        print(res)
            return res
            
        for k in range(len(prices)):
            left = prices[:k]
            right = prices[k:]
#            if k == 3:
#                print('-----------')
            max_pro = max(max_pro,get_pro(left)+get_pro(right))
        return max_pro
        
        if prices == []:
            return 0
        K = 2
        dp = [[0]*(K+1) for i in prices]
        import sys
        for k in range(1,K+1):
            mins = prices[0]
            for i in range(len(prices)):
                
                mins = min(mins,prices[i] - dp[i][k-1])
                dp[i][k] = max(dp[i-1][k],prices[i] - mins)
                    
        return dp[-1][-1]
        """
        if len(prices) < 2:
            return 0
        dp = [[0]*3 for _ in prices]
        for k in range(1,3):
            mins = prices[0]
            for i in range(len(prices)):
                mins = min(mins,prices[i] - dp[i][k-1])
                dp[i][k] = max(dp[i-1][k],prices[i] - mins)
        return dp[-1][-1]

        mins = min(mins,prices[i] - dp[i][k-1])
        dp[i][k] = max(dp[i-1][k],prices[i]-mins)
