class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        
        import sys
        res = sys.maxsize
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            tmp = target - nums[i]
            left = i+1
            right = len(nums) -1
            ans = sys.maxsize
            while left < right:
                if abs(nums[left] + nums[right] - tmp) < abs(ans - tmp):
                    ans = nums[left] + nums[right]
            #        print(nums[left],nums[right])
                if nums[left] + nums[right] - tmp > 0:
                    right -= 1
                else:
                    left += 1
            res = res if abs(res - target) < abs(ans + nums[i] - target) else ans + nums[i]
        return res
        """
        if nums == []:
            return 0
        nums.sort()
        
        res = sys.maxsize
        for i in range(len(nums)):
            new_t = target - nums[i]
            left = i + 1
            right = len(nums) - 1
            ans = sys.maxsize
            while left < right:
                if abs(nums[left] + nums[right] - new_t) < abs(ans-new_t):
                    ans = nums[left] + nums[right]
                if nums[left] + nums[right] - new_t > 0:
                    right -= 1
                else:
                    left += 1
            if abs(ans + nums[i] - target) < abs(res - target):
                res = ans + nums[i]
        return res

