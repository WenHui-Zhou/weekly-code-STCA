class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 1:
            if (n & 1) == 0: # 偶数直接右移
                n >>= 1
            else:
                n += -1 if (n & 2) == 0 or n == 3 else 1  # 奇数01或者3减一，其他加1
            count += 1
        return count
