class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        if nums == []:
            return [-1,-1]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                l_side = mid
                while l_side-1>= 0 and nums[l_side-1] == target:
                    l_side -= 1
                r_side = mid
                while r_side+1 < len(nums) and nums[r_side+1] == target:
                    r_side += 1
                return [l_side,r_side]
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return [-1,-1]
        
        if nums == []:
            return [-1,-1]
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if left > right:
            return [-1,-1]
        left = mid
        while left >= 0 and nums[left] == target:
            left -= 1
        right = mid
        while right < len(nums) and nums[right] == target:
            right += 1
        return [left+1,right-1]"""
        if nums == []:
            return [-1,-1]
        left = 0
        right = len(nums) - 1
        pos = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                pos = mid 
                break
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        if pos == -1:
            return [-1,-1]
        left = pos
        while left>=0 and nums[left] == target:
            left -= 1
        right = pos
        while right < len(nums) and nums[right] == target:
            right += 1
        return [left+1,right -1]

                
