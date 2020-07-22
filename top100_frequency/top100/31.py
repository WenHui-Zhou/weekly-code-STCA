class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        
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
        if len(nums) <= 1:
            return 
        pos = len(nums) - 1
        while pos > 0 and nums[pos] <= nums[pos - 1]:
            pos -= 1
        if pos == 0:
            nums.sort()
            return
        min_val = nums[pos]
        for i in range(pos+1,len(nums)):
            if nums[i] > nums[pos - 1] and nums[i] < min_val:
                min_val = nums[i]
        min_index = nums[pos:].index(min_val) + pos
        for idx,val in enumerate(nums[pos:]):
            if min_val == val:
                min_index = idx + pos
        min_index = len(nums) - nums[-1::-1].index(min_val) - 1
        nums[pos - 1],nums[min_index] = nums[min_index],nums[pos-1]
        left = pos
        right = len(nums) - 1
        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1
    #    nums = nums[:pos] + nums[pos:][::-1]
        return"""
        if nums == []:
            return
        pos = len(nums) - 2
        while pos >= 0 and nums[pos] >= nums[pos+1]:
            pos -= 1
        if pos < 0:
            nums.sort()
            return
        min_val = nums[pos]
        for i in range(pos+1,len(nums))[::-1]:
            if nums[i] > min_val:
                nums[i],nums[pos] = nums[pos],nums[i]
                break
        left = pos + 1
        right = len(nums) - 1
        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1
    #    nums = nums[:pos+1] + nums[pos+1:][::-1]
    #    return nums
