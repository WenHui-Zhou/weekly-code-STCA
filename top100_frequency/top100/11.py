class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            res = max(res,(right-left)*min(height[left],height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            res = max(res,(right - left)*min(height[right],height[left]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
        
        if height == []:
            return 0
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            res = max(res,(right - left)*min(height[left],height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res"""
        if height == []:
            return 0
        left = 0
        right = len(height) - 1
        ans = 0
        while left < right:
            ans = max(min(height[left],height[right]) * (right - left),ans)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return ans






