class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return s
        res = s.split(' ')
        ans = ''
        for ss in res:
            ans += ss[::-1] + ' '
        return ans[:-1]
