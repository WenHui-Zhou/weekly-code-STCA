class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        arr = [['.']*n for _ in range(n)]
        def isValid(arr,row,col):
            for i in range(len(arr)):
                if arr[i][col] == 'Q':
                    return False
            r = row
            c = col
            while r >=0 and c>=0:
                if arr[r][c] == 'Q':
                    return False
                r -=1 
                c -= 1
            r = row
            c = col
            while r >=0 and c<len(arr):
                if arr[r][c] == 'Q':
                    return False
                r -=1 
                c += 1
            return True

        def dfs(arr,row,res):
            if row == len(arr):
                tmp = []
                for i in range(len(arr)):
                    tmp.append(''.join(arr[i]))
                res.append(tmp)
                return
            for i in range(len(arr)):
                if not isValid(arr,row,i):
                    continue
                arr[row][i] = 'Q'
                dfs(arr,row + 1,res)
                arr[row][i] = '.'
        dfs(arr,0,res)
        return res
