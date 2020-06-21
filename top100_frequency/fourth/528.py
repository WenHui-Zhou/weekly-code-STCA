class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        num = sum(w)
        self.w = []
        cur = 0
        for c in w:
            cur += c
            self.w.append(cur*1.0 / num)

    def pickIndex(self):
        """
        :rtype: int
        """
        return bisect.bisect_right(self.w,random.random())


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
