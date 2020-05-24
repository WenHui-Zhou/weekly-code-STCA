class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                new_t = target - nums[i] - nums[j]
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == new_t:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        right -= 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                    elif nums[left] + nums[right] > new_t:
                        right -= 1
                    else:
                        left += 1
        return res
