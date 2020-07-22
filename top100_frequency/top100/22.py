class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        
        if n == 0:
            return []
        def dfs(right,res,ans,n):
            if len(res) == n*2 :
                if right == 0:
                    ans.append(res)
                return 
            if right > n or right < 0:
                return 
            dfs(right+1,res+'(',ans,n)
            dfs(right-1,res + ')',ans,n)
        ans = []
        dfs(0,'',ans,n)
        return ans
        if n == 0:
            return []
        def dfs(right,res,ans,n):
            if len(res) == n*2:
                if right == 0:
                    ans.append(res)
                return
            if right > n or right < 0:
                return
            dfs(right+1,res+'(',ans,n)
            dfs(right-1,res+')',ans,n)
        ans = []
        dfs(0,'',ans,n)
        return ans"""
        if n == 0:
            return []
        def dfs(right,res,n,ans):
            if len(res) == n*2:
                if right == 0:
                    ans.append(res)
                return 
            if right > n or right < 0:
                return
            dfs(right+1,res+'(',n,ans)
            dfs(right-1,res+')',n,ans)
        ans = []
        dfs(0,'',n,ans)
        return ans
