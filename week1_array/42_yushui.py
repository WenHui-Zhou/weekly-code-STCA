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
        """
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
