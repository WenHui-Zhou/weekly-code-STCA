class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        
        if x < 2:
            return x
        left = 1
        right = x // 2
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            elif (mid + 1)**2 > x:
                return mid
            else:
                left = mid+1
        """
        left = 0
        right = x // 2 + 1
        while left <= right:
            mid = (left + right) // 2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1 if left*left > x else left
