class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if matrix == []:
            return matrix
        ans = [[-1]*len(matrix[0]) for _ in range(len(matrix))]
        
        queue = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    queue.append([i,j])
                    ans[i][j] = 0
        xh = [0,1,0,-1]
        yh = [1,0,-1,0]
        while queue:
            pox,poy = queue.pop(0)
            num = ans[pox][poy]
            for k in range(4):
                x = pox + xh[k]
                y = poy + yh[k]
                if 0<=x<len(matrix) and 0<=y<len(matrix[0]) and \
                 (ans[x][y] == -1 or ans[x][y] > num + 1):
                    ans[x][y] = num + 1
                    queue.append([x,y])
        return ans
