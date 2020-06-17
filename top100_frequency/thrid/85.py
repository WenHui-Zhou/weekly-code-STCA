class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == [] or matrix[0] == []:
            return 0
        for i in range(len(matrix[0])):
            matrix[0][i] = int(matrix[0][i])
        for i in range(len(matrix[0])):
            for j in range(1,len(matrix)):
                matrix[j][i] = int(matrix[j][i])
                if matrix[j][i] != 0:
                    matrix[j][i] += matrix[j-1][i]
        def get_max(height):
            stack = [-1]
            max_res = 0
            for i in range(len(height)):
                while len(stack) > 1 and height[stack[-1]] >= height[i]:
                    max_res = max(max_res,height[stack.pop()] * (i - stack[-1] - 1))
                stack.append(i)
            for i in range(len(stack) - 1):
                max_res = max(max_res,height[stack.pop()] * (len(height) - stack[-1] - 1))
            return max_res
        ans = 0
        for arr in matrix:
            ans = max(ans,get_max(arr))
        return ans
