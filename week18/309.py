class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        dp = [[0]*len(prices) for _ in range(3)]
        dp[0][0] = 0 # 不持股当天没卖出
        dp[1][0] = -prices[0] # 持股
        dp[2][0] = 0 # 不持股，当天卖出

        for i in range(1,len(prices)):
            dp[0][i] = max(dp[0][i-1],dp[2][i-1])
            dp[1][i] = max(dp[1][i-1],dp[0][i-1]-prices[i])
            dp[2][i] = dp[1][i-1] + prices[i]
        return max(dp[0][-1],dp[2][-1])

