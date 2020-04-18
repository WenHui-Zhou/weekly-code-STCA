class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        
        if board == [] or board[0] == []:
            return []
        visit = [[0] * len(board[0]) for i in board]
        
        def dfs(board,visit,x,y):
      #      print(x,y)
            xh = [1,0,-1,0]
            yh = [0,1,0,-1]
            for k in range(4):
                posx = x + xh[k]
                posy = y + yh[k]
                if 0 <= posx<len(board) and 0 <= posy < len(board[0]) and visit[posx][posy] == 0 and board[posx][posy] == 'O':
                    visit[posx][posy] = 1
                    dfs(board,visit,posx,posy)
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                visit[0][i] = 1
                dfs(board,visit,0,i)
        for i in range(len(board)):
            if board[i][-1] == 'O':
                visit[i][-1] = 1
                dfs(board,visit,i,len(board[0]) - 1)
        for i in range(len(board[0])):
            if board[-1][i] == 'O':
                visit[-1][i] = 1
                dfs(board,visit,len(board)-1,i)
        for i in range(len(board)):
            if board[i][0] == 'O':
                visit[i][0] = 1
                dfs(board,visit,i,0)
 #       print(visit)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if visit[i][j] == 0:
                    board[i][j] = 'X'
        """
        if board == []:
            return board
        def dfs(board,pox,poy,visit):
            xh = [0,1,0,-1]
            yh = [1,0,-1,0]
            for k in range(4):
                x = pox + xh[k]
                y = poy + yh[k]
                if 0<=x<len(board) and 0<=y<len(board[0]) and \
                board[x][y] == 'O' and visit[x][y] == 0:
                    visit[x][y] = 1
                    dfs(board,x,y,visit)
        visit = [[0]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board[0])):
            if visit[0][i] == 0 and board[0][i] == 'O':
                visit[0][i] = 1
                dfs(board,0,i,visit)
        for i in range(len(board)):
            if visit[i][-1] == 0 and board[i][-1] == 'O':
                visit[i][-1] = 1
                dfs(board,i,len(board[0])-1,visit)
        for i in range(len(board[0])):
            if visit[-1][i] == 0 and board[-1][i] == 'O':
                visit[-1][i] = 1
                dfs(board,len(board)-1,i,visit)
        for i in range(len(board)):
            if visit[i][0] == 0 and board[i][0] == 'O':
                visit[i][0] = 1
                dfs(board,i,0,visit)      
        for i in range(len(visit)):
            for j in range(len(visit[0])):
                if board[i][j] == 'O' and visit[i][j] == 0:
                    board[i][j] = 'X'
#        print(visit)
        return board
