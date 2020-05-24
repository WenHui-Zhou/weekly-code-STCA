class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]*(num+1)
        def get_count(n):
            ans ,mask = 0,1
            for i in range(32):
                if n&mask:
                    ans += 1
                mask <<= 1
            return ans
        for idx in range(num+1):
            ans[idx] = get_count(idx)
        return ans
            




