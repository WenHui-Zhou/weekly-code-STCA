class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if S == '':
            return []
        ans = []
        def dfs(S,res):
        #    print(res)
            if len(res) == len(S):
                ans.append(res)
                return
            pos = len(res)
        #    print(pos,len(S))
        #    for i in range(pos,len(S)):
            i = pos
            while S[i].isdigit():
                res += S[i]
                if i == len(S) - 1 and len(res) == len(S):
                    ans.append(res)
                    return
                i += 1
            
            res += S[i].lower()
            dfs(S,res)
            res = res[:-1]
            res += S[i].upper()
            dfs(S,res)
            res = res[:-1]
        dfs(S,'')
        return ans
