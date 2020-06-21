class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        
        pos = -1
        for ii in range(len(nums)):
            if nums[ii] != 0:
                if pos == -1:
                    continue
                else:
                    nums[pos],nums[ii] = nums[ii],nums[pos]
                    pos += 1
            else:
                if pos == -1:
                    pos = ii
        return nums"""
        if nums == []:
            return []
        cur = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[cur] = nums[i]
                cur += 1
        while cur < len(nums):
            nums[cur] = 0
            cur += 1
        return nums
