class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        mask = x^y
        distance = 0
        while mask:
            if mask & 1:
                distance += 1
            mask >>= 1
        return distance

