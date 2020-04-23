class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s == '':
            return False
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(0,i):
                tmp = s[j:i]
                if dp[j] and tmp in wordDict:
                    dp[i] = True
    #    print(dp)
        return dp[-1]

        
