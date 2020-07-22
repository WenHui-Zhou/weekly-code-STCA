class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        
        def dfs(x,n):
            if n == 0:
                return 1.0
            half = dfs(x,n//2)
            if n%2 == 0:
                return half * half
            else:
                return half * half * x
        if n < 0:
            x = 1/x
            n = -n
        return dfs(x,n)
        if n < 0:
            n = -n
            x = 1.0/x
        def dfs(x,n):
            if n == 0:
                return 1.0
            half = dfs(x,n//2)
            if n%2 == 0:
                return half*half
            else:
                return half*half*x
        return dfs(x,n)"""
        if n<0:
            n = -n
            x = 1.0 / x
        def dfs(x,n):
            if n == 0:
                return 1.0
            half = dfs(x,n//2)
            if n%2 == 0:
                return half*half
            else:
                return half*half*x
        return  dfs(x,n)
