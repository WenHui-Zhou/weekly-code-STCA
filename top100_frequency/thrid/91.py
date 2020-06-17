class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        if s[0] == '0':
            return 0
        dp = [0]*(len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        for idx,ch in enumerate(s):
            if idx == 0:
                continue
            if ch != '0':
                dp[idx+1] += dp[idx]
            if s[idx-1] != '0' and 1 <= int(s[idx-1:idx+1]) <= 26:
                dp[idx+1] += dp[idx-1]
        return dp[-1]
