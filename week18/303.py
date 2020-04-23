class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.ans = [0]*(len(nums)+1)
        for idx,nu in enumerate(nums):
            if idx == 0:
                self.ans[idx+1] = nu
            else:
                self.ans[idx+1] = self.ans[idx] + nu

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.ans[j+1] - self.ans[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
