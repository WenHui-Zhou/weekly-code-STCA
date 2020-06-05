class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s == "" or t == '':
            return ''
        if len(s) < len(t):
            return ''
        left = right = 0
        res = ''
        window = {}
        count = 0
        for c in t:
            window[c] = 0
        upper = {}
        for c in t:
            if c in upper:
                upper[c] += 1
            else:
                upper[c] = 1

        while right < len(s):
            if s[right] in window:
                window[s[right]] += 1
                if window[s[right]] == upper[s[right]] or (upper[s[right]] > 1 and window[s[right]] < upper[s[right]]):
                    count += 1
            if count >= len(t):
                while count >= len(t):
                    if len(res) > right - left + 1 or res == '':
                        res = s[left:right+1]
                    if s[left] in window:
                        window[s[left]] -= 1
                        if window[s[left]] < upper[s[left]]:
                            count -= 1
                    left += 1
                
            
            right += 1
            if right >= len(s):
                if len(res) > right - left + 1:
                    res = s[left-1:right]
        return res



