class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        pos = len(nums) - 1
        while pos > 0 and nums[pos] <= nums[pos - 1]:
            pos -= 1
        if pos == 0:
            nums.sort()
            return
        min_val = nums[pos]
        for i in range(len(nums[:pos])+1,len(nums)):
        #    print(nums[i])
            if nums[i] > nums[pos-1] and nums[i] < min_val:
                min_val = nums[i]
        print(min_val)
        min_index = nums[pos:].index(min_val) + pos
        nums[pos-1],nums[min_index] = nums[min_index],nums[pos-1]
        for i in range(len(nums[pos:])):
            for j in range(i+1,len(nums[pos:])):
                if nums[pos+i] > nums[pos+j]:
                    nums[pos+i],nums[pos+j] = nums[pos+j],nums[pos+i]
