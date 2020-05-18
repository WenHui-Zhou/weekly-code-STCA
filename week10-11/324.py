class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        
        nums.sort()
        if len(nums) % 2 == 0:
            mid = len(nums)//2
        else:
            mid = len(nums) // 2 + 1

        small = nums[:mid][::-1]
        big = nums[mid:][::-1]
        i = 0
        cur = 0
        while cur < len(nums):
            nums[cur] = small[i]
            if cur+1 == len(nums):
                break
            nums[cur+1] = big[i]
            cur += 2
            i += 1
           
        nums.sort()
        if len(nums) <= 2:
            return
        if len(nums) % 2 == 0:
            mid = len(nums) // 2
        else:
            mid = len(nums) // 2 + 1
        small = nums[:mid][::-1]
        big = nums[mid:][::-1]
        i = 0
        cur = 0
        while cur < len(nums):
            nums[cur] = small[i]
            if cur + 1 == len(nums):
                break
            nums[cur+1] = big[i]
            cur += 2
            i += 1
         """
        nums.sort()
        mid = len(nums) // 2
        if len(nums) % 2 != 0:
            mid += 1
        right = len(nums) - 1
        left = mid - 1
        res = []
        while left >= 0:
            res.append(nums[left])
            if len(res) == len(nums):
                break
            res.append(nums[right]) 
            left -= 1
            right -= 1
        for i in range(len(res)):
            nums[i] = res[i]

