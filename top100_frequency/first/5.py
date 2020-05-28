class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        
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
        """
        ans = ''
        if s == '':
            return ''
        ans = s[0]
        for i in range(1,len(s)):
            # 偶数
            if s[i-1] == s[i]:
                left = i-1
                right = i
                while left >=0 and right < len(s):
                    if s[left] == s[right]:
                        left -= 1
                        right += 1
                    else:
                        if right - left - 1 > len(ans):
                            ans = s[left+1:right]
                        break
                if left < 0 or right >= len(s):
                    if right - left - 1 > len(ans):
                        ans = s[left+1:right]
            if i-1 >=0 and i+1<len(s) and s[i-1] == s[i+1]:
                left = i-1
                right = i+1
                while left >= 0 and right < len(s):
                    if s[left] == s[right]:
                        left -= 1
                        right += 1
                    else:
                        if right - left - 1 > len(ans):
                            ans = s[left + 1:right]
                        break
                if left < 0 or right >= len(s):
                    if right - left -1 >len(ans):
                        ans = s[left+1:right]
        return ans
