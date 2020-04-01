class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
       
        cur = 0
        for i in range(len(nums)):
            if i > 0:
                if nums[i-1] == nums[i]:
                    continue
            nums[cur] = nums[i]
            cur += 1
        return cur
        
        cur = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            else:
                nums[cur] = nums[i]
                cur += 1
        return cur
         """
        if nums == []:
            return 0
        cur = 1
        n = len(nums) - 1
        while cur <= n:
            if nums[cur] == nums[cur - 1]:
                nums.pop(cur)
                n -= 1
            else:
                cur += 1
        return n + 1
