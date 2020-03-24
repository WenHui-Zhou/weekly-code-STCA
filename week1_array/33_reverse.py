class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        
        if nums == []:
            return -1
        left = 0
        right = len(nums) -1
        if left <= right:
            if nums[left] <= target:
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] == target:
                        return mid
                    elif nums[left] > nums[mid]:
                        right = mid - 1
                    elif nums[mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
            else:
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] > nums[right]:
                        left = mid + 1
                    elif nums[mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
        return -1
        """
        if nums == []:
            return -1
        left = 0
        right = len(nums) - 1
        if left <= right:
            if nums[left] <= target:
                while left <= right:
                    mid = (right + left) // 2
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] < nums[left] or nums[mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
            else:
                while left <= right:
                    mid = (right + left) // 2
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] > nums[right] or nums[mid] < target:
                        left = mid + 1
                    else:
                        right -= 1
        return -1 
