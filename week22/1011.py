class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """

        def get_day(weights,limit):
            day = 0
            r = 0
            for w in weights:
                if r + w <= limit:
                    r += w
                else:
                    day += 1
                    r = w
            return day + 1
        left = max(weights)
        right = sum(weights)
        if left == right:
            return left
        while left < right:
            mid = (left + right) // 2
            day = get_day(weights,mid)
            if day > D:
                left = mid + 1
            else:
                right = mid
        return left
            
