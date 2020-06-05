class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        tmp = str(x)
        other = str(x)[::-1]
        return tmp == other
