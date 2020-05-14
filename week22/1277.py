class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n,m = len(matrix),len(matrix[0])
        dp = [[0]*m for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                elif matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                ans += dp[i][j]
        return ans
            
