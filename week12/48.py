class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if matrix == [] or matrix[0] == []:
            return matrix
        n = len(matrix)
        # 对角线
        x,y = 0,0
        while x < n:
            leftx,lefty = x,y
            rightx,righty = x,y
            while True:
                leftx = leftx-1
                righty = righty-1
                if leftx<0 or lefty >= n or rightx >= n or righty < 0:
                    break
                else:
                    matrix[lefty][leftx],matrix[righty][rightx] = \
                    matrix[righty][rightx],matrix[lefty][leftx]
            x += 1
            y += 1
        # 纵向
        row = 0
        while row < n:
            left = 0
            right = n - 1
            while left < right:
                matrix[row][left],matrix[row][right] = matrix[row][right],matrix[row][left]
                left += 1
                right -= 1
            row += 1
        return matrix

