class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        cur = 1
        k = 0
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i] and k < 1:
                nums[cur] = nums[i]
                k += 1
                cur += 1
            else:
                if nums[i-1] != nums[i]:
                    k = 0
                    nums[cur] = nums[i]
                    cur += 1
        return cur
        """
        if len(nums) < 3:
            return len(nums)
        cur = 2
        n = len(nums) - 1
        while cur <= n:
            if nums[cur - 2] == nums[cur]:
                nums.pop(cur)
                n -= 1
            else:
                cur += 1
        return n + 1

