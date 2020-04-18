class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import numpy
        if grid == []:
            return 0
        
        xh = [1,0,-1,0]
        yh = [0,1,0,-1]
        minute = 0
        while True:
            tmp = copy.deepcopy(grid)
            flag = 0
            for i in range(len(tmp)):
                for j in range(len(tmp[0])):
                   
                    if tmp[i][j] == 2:
                        for k in range(4):
                            x = i + xh[k]
                            y = j + yh[k]
                            if 0 <=x<len(tmp) and 0<=y<len(tmp[0]) and tmp[x][y] == 1:
                                grid[x][y] = 2 
                    elif tmp[i][j] == 1:
                        flag = 1
                        score = 0
                        for k in range(4):
                            x = i + xh[k]
                            y = j + yh[k]
                            if 0<=x<len(tmp) and 0<=y<len(tmp[0]) and tmp[x][y] != 0:
                                score += 1
                        if score == 0:
                        #    print(i,j)
                            return -1
            if flag == 0:
                break
            if numpy.array(tmp).sum() == numpy.array(grid).sum():
                return -1
            
            minute += 1
            
        return minute
