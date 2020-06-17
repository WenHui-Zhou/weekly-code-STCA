class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
       
        if word == '':
            return True
        
        def dfs(board,word,pox,poy,visit):
        #    print(visit)
            if word == '':
                return True
            xh = [0,1,0,-1]
            yh = [1,0,-1,0]
            for k in range(4):
                x = pox + xh[k]
                y = poy + yh[k]
            #    print(y,x)
                if 0<=x<len(board[0]) and 0 <= y < len(board) and visit[y][x] == 0 and board[y][x] == word[0]:
                    visit[y][x] = 1
                    if dfs(board,word[1:],x,y,visit) == True:
                        return True
                    visit[y][x] = 0
            return False

        visit = [[0]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visit[i][j] = 1
                    if dfs(board,word[1:],j,i,visit) == True:
                        return True
                    visit[i][j] = 0
        return False
         """
        if word == '':
            return True
        def dfs(board,word,x,y,visit):
        #    print(word)
            if word == '':
                return True
            xh = [1,0,-1,0]
            yh = [0,1,0,-1]
            for k in range(4):
                posx = x + xh[k]
                posy = y + yh[k]
                if 0<= posx < len(board) and 0 <= posy < len(board[0]) and visit[posx][posy] == 0 and board[posx][posy] == word[0]:
                    visit[posx][posy] = 1
                    if dfs(board,word[1:],posx,posy,visit):
                        return True
                    visit[posx][posy] = 0
            return False
        visit = [[0]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != word[0]:
                    continue
                visit[i][j] = 1
                if dfs(board,word[1:],i,j,visit):
                    return True
                visit[i][j] = 0
        return False
        
           
