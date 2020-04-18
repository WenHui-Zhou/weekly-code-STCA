class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image == []:
            return image
        def dfs(image,sr,sc,oldColor,newColor):
            xh = [0,1,-1,0]
            yh = [1,0,0,-1]
            for k in range(4):
                x = xh[k] + sr
                y = yh[k] + sc
                if 0<=x<len(image) and 0<=y <len(image[0]) and image[x][y] == oldColor:
                    image[x][y] = newColor
                    dfs(image,x,y,oldColor,newColor)
        
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        image[sr][sc] = newColor
        dfs(image,sr,sc,oldColor,newColor)
        return image
