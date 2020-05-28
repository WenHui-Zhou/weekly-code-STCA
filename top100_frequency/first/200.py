class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        
        if grid == []:
            return 0
        
        def dfs(grid,pox,poy,visit):
            xh = [0,1,0,-1]
            yh = [1,0,-1,0]
            for k in range(4):
                x = pox + xh[k]
                y = poy + yh[k]
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and visit[x][y] == 0 and grid[x][y] == '1':
                    visit[x][y] = 1
                    dfs(grid,x,y,visit)
        visit = [[0]*len(grid[0]) for _ in range(len(grid))]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and visit[i][j] == 0:
                    ans += 1
                    visit[i][j] = 1
                    dfs(grid,i,j,visit)
        return ans"""
        if grid == []:
            return 0
        def dfs(grid,visit,pox,poy):
            xh = [1,0,-1,0]
            yh = [0,1,0,-1]
            for k in range(4):
                x = xh[k] + pox
                y = yh[k] + poy
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1" and visit[x][y] == 0:
                    visit[x][y] = 1
                    dfs(grid,visit,x,y)

        ans = 0
        visit = [[0]*len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and visit[i][j] == 0:
                    ans += 1
                    visit[i][j] = 1
                    dfs(grid,visit,i,j)
        
        return ans




