class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0x100000000
        max_int = 0x7FFFFFFF
        min_int = max_int + 1
        while b != 0:
            carry = (a&b) << 1
            a = (a ^ b) % mask
            b = carry % mask
        return a if a<=max_int else ~((a%min_int) ^ max_int)
