class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [-1]
        max_res = 0
        for i in range(len(heights)):
            while len(stack) > 1 and heights[i] <= heights[stack[-1]]:
                max_res = max(max_res, heights[stack.pop()] * (i - stack[-1] - 1))  
            stack.append(i)
        for i in range(len(stack)-1):
            max_res = max(max_res, heights[stack.pop()]*(len(heights)-1-stack[-1]))
        return max_res

