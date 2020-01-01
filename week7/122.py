class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        add_val = 0
        for ii in range(1,len(prices)):
            add_val = max(add_val,add_val + prices[ii] - prices[ii-1])
        return add_val
