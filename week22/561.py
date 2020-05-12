class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        nums.sort()
        res = 0
        for i in range(0,len(nums),2):
            res += nums[i]
        return res
