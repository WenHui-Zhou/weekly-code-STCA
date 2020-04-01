class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        
        while val in nums:
            nums.pop(nums.index(val))
        return len(nums)
        """
        if nums == []:
            return 0
        n = len(nums) - 1
        cur = 0
        while cur <= n:
            if nums[cur] == val:
                nums.pop(cur)
                n -= 1
            else:
                cur += 1
        return len(nums)
