class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == [] or len(nums) == 1:
            return True
        left = 0
        for ii in range(len(nums)):
            if ii > left:
                return False
            left = max(left,ii + nums[ii])
            if left >= len(nums) - 1:
                return True
            