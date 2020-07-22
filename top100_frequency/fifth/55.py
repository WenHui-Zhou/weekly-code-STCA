class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        
        cur = 0
        right = 0
        while cur <= right:
            right = max(cur+nums[cur],right)
            cur += 1
            if right >= len(nums)-1:
                return True
        return False
        
        if len(nums) == 0:
            return True
        cur = 0
        right = 0
        while cur <= right:
            right = max(right,nums[cur] + cur)
            cur += 1
            if right >= len(nums) - 1:
                return True
        return False"""
        cur = 0
        right = 0
        while cur <= right:
            right = max(right,cur + nums[cur])
            cur += 1
            if right >= len(nums) - 1:
                return True
        return False


