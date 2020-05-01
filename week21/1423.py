class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        for i in range(k):
            res += cardPoints[i]
        ans = res
        t = k-1
        for i in range(len(cardPoints) - k, len(cardPoints))[::-1]:
       #     print(t,i)
            res = res - cardPoints[t] + cardPoints[i]
            if ans < res:
                ans = res
            t -= 1
        #    print(res)
        return ans


