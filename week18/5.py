class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        if s == '':
            return ans
        for pivot in range(len(s)):
            # pivot 为重心
            lens = 1
            i = pivot - 1
            j = pivot + 1
            while i>=0 and j < len(s):
                if s[i] == s[j]:
                    lens += 2
                    i -= 1
                    j += 1
                else:
                    break
            if len(ans) < lens:
                ans = s[i+1:j]
            lens = 0
            i = pivot - 1
            j = pivot
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    i -= 1
                    j += 1
                    lens += 2
                else:
                    break
            if len(ans) < lens:
                ans = s[i+1:j]
        return ans

