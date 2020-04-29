class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        num &= 0xFFFFFFFF
        s = '0123456789abcdef'
        mask = 0b1111
        res = ''
        while num > 0:
            res  += s[num & mask]
            num >>= 4
        return res[::-1] if res else '0'
