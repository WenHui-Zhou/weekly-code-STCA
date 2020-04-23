class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        if k > len(prices) // 2:
            res = 0
            for i in range(1,len(prices)):
                if prices[i] > prices[i-1]:
                    res += prices[i] - prices[i-1]
                    
            return res
        dp = [[0]*(k+1) for i in prices]
        for kk in range(1,k+1):
            mins = prices[0]
            for i in range(1,len(prices)):
                mins = min(mins,prices[i] - dp[i][kk-1])
                dp[i][kk] = max(dp[i-1][kk],prices[i] - mins)
        return dp[-1][-1]
