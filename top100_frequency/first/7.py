class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0
        if x < 0:
            flag = 1
            x = -x
        x = str(x)[::-1]
        x = int(x)
        if flag:
            x = -x
        if 2**31 -1 >= x >= -2**31:
            return x
        else:
            return 0
