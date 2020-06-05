class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        
        if matrix == [] or matrix[0] == []:
            return []
        begin = 0
        left = len(matrix[0])
        bottom = len(matrix)
        res = []
        while begin < left and begin < bottom:
            x = begin
            y = begin
            for i in range(x,left):
                res.append(matrix[x][i])
            
            for j in range(y+1,bottom):
                res.append(matrix[j][left - 1])
            if bottom-1 != x:
                for i in range(x,left-1)[::-1]:
                    res.append(matrix[bottom - 1][i])
            if left-1 != x:
                for j in range(y+1,bottom-1)[::-1]:
                    res.append(matrix[j][x])
            begin += 1
            left -= 1
            bottom -= 1
        return res
        
        if matrix == [] or matrix[0] == []:
            return []
        startx,starty = 0,0
        height = len(matrix)
        width = len(matrix[0])
        res = []
        while startx < width and starty < height:
            for j in range(startx,width):
                res.append(matrix[starty][j])
            if starty == height - 1:
                break
            for j in range(starty+1,height):
                res.append(matrix[j][width-1])
            if startx == width - 1:
                break
            for j in range(startx+1,width - 1)[::-1]:
                res.append(matrix[height-1][j])
            for j in range(starty + 1,height)[::-1]:
                res.append(matrix[j][startx])
            startx += 1
            starty += 1
            width -= 1
            height -= 1
        return res"""
        if matrix == []:
            return []
        startx = 0
        starty = 0
        endx = len(matrix[0])
        endy = len(matrix)
        res = []
        while startx < endx and starty < endy:
            for j in range(startx,endx):
                res.append(matrix[starty][j])
            if starty >= endy-1:
                break
            for j in range(starty+1,endy):
                res.append(matrix[j][endx-1])
            if startx >= endx-1:
                break
            for j in range(startx,endx-1)[::-1]:
                res.append(matrix[endy-1][j])
            if starty <= starty - 2:
                break
            for j in range(starty+1,endy-1)[::-1]:
                res.append(matrix[j][startx])
            startx += 1
            starty += 1
            endx -= 1
            endy -= 1
        return res
