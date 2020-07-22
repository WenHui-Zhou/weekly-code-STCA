class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        
        def match(s,p):
            if not p:
                return not s
            first_match = bool(s) and p[0] in {s[0],'.'}
            if len(p) >= 2 and p[1] == '*':
                return match(s,p[2:]) or (first_match and match(s[1:],p))
            else:
                return first_match and match(s[1:],p[1:])
        return match(s,p)
        # 递归做法
        def match(s,p):
            if not p:
                return not s
            first_match = bool(s) and p[0] in {s[0],'.'}
            if len(p) >= 2 and p[1] == '*':
                return match(s,p[2:]) or (first_match and match(s[1:],p))
            else:
                return first_match and match(s[1:],p[1:])
        return match(s,p)"""
        # 动态规划
        dp = [[0]*(len(s)+1) for _ in range(len(p) + 1)]
        dp[0][0] = 1
        for i in range(1,len(p) + 1):
            if i > 1 and p[i-1] == '*':
                dp[i][0] = dp[i-2][0]
            else:
                dp[i][0] = 0
        for i in range(1,len(p) + 1):
            for j in range(1,len(s) + 1):
                if p[i-1] == s[j-1] or p[i-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif i > 1 and p[i-1] == '*':
                    if dp[i-2][j]:
                        dp[i][j] = dp[i-2][j]
                    elif p[i-2] == '.' or p[i-2] == s[j-1]:
                        dp[i][j] = dp[i][j-1]
        return True if dp[-1][-1] else False




