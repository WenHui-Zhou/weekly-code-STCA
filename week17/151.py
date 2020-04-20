class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = [ss for ss in s.strip().split(' ') if ss != '']
        return ' '.join(ans[::-1])
