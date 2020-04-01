class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return [[]]
        res = [[0]*n for _ in range(n)]
        width = n - 1
        height = n - 1
        startx = 0
        starty = 0
        count = 1
        while startx <= width and starty <= height:
            for i in range(startx,width+1):
                res[starty][i] = count
                count += 1
            for i in range(starty + 1,height+1):
                res[i][width] = count
                count += 1
            for i in range(startx,width)[::-1]:
                res[height][i] = count
                count += 1
            for i in range(starty + 1,height)[::-1]:
                res[i][startx] = count
                count += 1
            startx += 1
            starty += 1
            width -= 1
            height -= 1
        return res

