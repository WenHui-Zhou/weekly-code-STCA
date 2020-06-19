class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == [] or grid[0] == []:
            return 0
        def travel_grid(grid,visit,pox,poy):
            xh = [0,1,-1,0]
            yh = [1,0,0,-1]
            count = 0
            for k in range(4):
                x = xh[k] + pox
                y = yh[k] + poy
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and  visit[x][y] == 0 and grid[x][y] != 0:
                    visit[x][y] = 1
    #                grid[x][y] = 2
                    count += travel_grid(grid,visit,x,y) + 1
                    print(x,y,count)
        #            visit[x][y] = 0
            return count
                
        visit = [[0]*len(grid[0]) for _ in range(len(grid))]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and visit[i][j] == 0:
                    visit[i][j] = 1
                    tmp = travel_grid(grid,visit,i,j) + 1
                    ans = max(ans,tmp)
        return ans

