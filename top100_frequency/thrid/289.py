class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        
        index = {}
        for k in range(len(board)):
            for l in range(len(board[0])):
                x,y = k-1,l-1
                count = 0
                for i in range(3):
                    if i != 0:
                        y += 1
                    if y >=0 and y <len(board[0])  and x >= 0 and x < len(board) and board[x][y]:
                        count += 1
                for i in range(1,3):
                    x += 1
                    if x >= 0 and x < len(board)  and y >=0 and y <len(board[0]) and board[x][y]:
                        count += 1
                for i in range(1,3):
                    y -= 1
                    if y >=0 and y <len(board[0])  and x >= 0 and x < len(board) and board[x][y]:
                        count += 1
                for i in range(1,2):
                    x -= 1
                    if x >=0 and x <len(board)  and y >=0 and y <len(board[0]) and board[x][y]:
                        count += 1
                if board[k][l] == 0 and count == 3:
                    index[(k,l)] = 1
                else:
                 
                    if count < 2 or count > 3:
                        
                        index[(k,l)] = 0
        for i,j in index:
            board[i][j] = index[(i,j)]
        """
        index = [[0]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                x = i -1
                y = j - 1
                count = 0
                for t in range(3):
                    if t != 0:
                        y += 1
                    if 0<=x<len(board) and 0<=y<len(board[0]):
                        if board[x][y] == 1:
                            count += 1
                for t in range(1,3):
                    x += 1
                    if 0<=x<len(board) and 0<=y<len(board[0]):
                        if board[x][y] == 1:
                            count += 1
                y = j - 1
                x = i - 1
                for t in range(1,3):
                    x += 1
                    if 0<=x<len(board) and 0<=y<len(board[0]):
                        if board[x][y] == 1:
                            count += 1
                x = i + 1
                y = j
                if 0<=x<len(board) and 0<=y<len(board[0]):
                    if board[x][y] == 1:
                        count += 1
                if  count == 3:
                    index[i][j] = 1
                else:
                    if count < 2 or count > 3:
                        index[i][j] = 0
                    else:
                        index[i][j] = board[i][j]
    #    print(index)
        for i in range(len(index)):
            for j in range(len(index[0])):
                board[i][j] = index[i][j]
                         
                    
