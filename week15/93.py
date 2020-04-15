class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        n = len(s)
        def dfs(start,depth,path,s):
            if depth == 4:
                path = path[:-1]
                ans.append(path)
                return
            minend = max(start+1,n - (3 - depth) * 3)
            maxend = min(start+3,n - (3 - depth) * 1)
            for end in range(minend,maxend+1):
                split = s[start:end]
                if len(split) > 1 and split[0] == '0':
                    break
                
                if int(split) <= 255:
                    dfs(end,depth+1,path + split + '.',s)
        dfs(0,0,'',s)
        return ans
