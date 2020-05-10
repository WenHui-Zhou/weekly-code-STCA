class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        pro = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                pro += prices[i] - prices[i-1]
        return pro
        
        pro = 0
        for i in range(1,len(prices)):
            if prices[i]  -  prices[i-1] > 0:
                pro += prices[i]  -  prices[i-1]
        return pro
        """
        res = 0
        if len(prices)<2:
            return 0
        for i in range(1,len(prices)):
            res = max(res,res + prices[i] - prices[i-1])
        return res
