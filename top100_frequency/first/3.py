class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        left = 0
        right = 1
        ans = 0
        aset = set()
        aset.add(s[left])
        while right < len(s):
            if s[right] not in aset:
                aset.add(s[right])
            else:
                ans = max(ans,right - left)
                index = s[left:right].index(s[right]) + left
                left = index + 1
                aset = set(s[left:right+1])
            right += 1
        if len(set(s[left:right])) == right - left:
            ans = max(ans,right - left)
        return ans
            
