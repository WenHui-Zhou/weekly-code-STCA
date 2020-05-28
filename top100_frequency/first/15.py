class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            target = -nums[i]
            j = i+1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == target:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1

        return res"""

        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if right + 1 < len(nums) - 1:
                    if nums[right] == nums[right+1]:
                        right -= 1
                        continue
                if left - 1 > i and nums[left - 1] == nums[left]:
                    left += 1
                    continue
                val = nums[left] + nums[right] + nums[i]
                if  val == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                elif val > 0:
                    right -= 1
                else:
                    left += 1
        return res

