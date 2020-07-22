class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        
        if height == []:
            return 0
        left = [0]*len(height)
        left[0] = height[0]
        le = height[0]
        for i in range(1,len(height)):
            if le >= height[i]:
                left[i] = le
            else:
                le = height[i]
                left[i] = le
        ri = height[-1]
        res = min(left[-1],ri) - height[-1]
        for i in range(len(height) - 1)[::-1]:
            if ri < height[i]:
                ri = height[i]
            res += min(ri,left[i]) - height[i]
        return res
        
        if height == []:
            return 0
        left = []
        right = []
        for i in range(len(height)):
            if i == 0:
                left.append(height[0])
            else:
                left.append(max(left[-1],height[i]))
        for i in range(len(height))[::-1]:
            if right == []:
                right.append(height[-1])
            else:
                right.append(max(right[-1],height[i]))
        res = 0
        right = right[::-1]
        for i in range(len(height)):
            res += min(left[i],right[i]) - height[i]
        return res
        if height == []:
            return 0
        left = []
        right = []
        for val in height:
            if left == []:
                left.append(val)
            else:
                left.append(max(left[-1],val))
        for val in height[::-1]:
            if right == []:
                right.append(val)
            else:
                right.append(max(right[-1],val))
        res = 0
        right = right[::-1]
        for i in range(len(left)):
            res += min(left[i],right[i]) - height[i]
        return res
        left = []
        right = []
        if height == []:
            return 0
        left_m = height[0]
        for val in height:
            if val > left_m:
                left_m = val
            left.append(left_m)
        right_m = height[-1]
        for val in height[::-1]:
            if val > right_m:
                right_m = val
            right.append(right_m)
        right = right[::-1]
        ans = 0
        for i in range(len(left)):
            ans += min(left[i],right[i]) - height[i]
        return ans"""
        if height == []:
            return 0
        left = [height[0]]
        right = [height[-1]]
        for val in height[1:]:
            left.append(max(left[-1],val))
        for val in height[:-1][::-1]:
            right.append(max(right[-1],val))
        right = right[::-1]
        ans = 0
        for i in range(len(height)):
            ans += min(left[i],right[i]) -height[i]
        return ans

            
