class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        
        if candidates == []:
            return []
        ans = []
        def dfs(candidates,target,res,pos):
            if sum(res) == target and sorted(res) not in ans:
                ans.append(sorted(res[::]))
                return
            for i in range(pos,len(candidates)):
                if sum(res) + candidates[i] > target:
                    return
                res.append(candidates[i])
                dfs(candidates,target,res,pos)
                res.pop()
        dfs(sorted(candidates),target,[],0)
        return ans"""
        if candidates == []:
            return []
        def dfs(candidates,target,res,ans,pos):
            if sum(res) == target and sorted(res) not in ans:
                ans.append(sorted(res))
                return 
            for i in range(pos,len(candidates)):
                if sum(res) + candidates[i] > target:
                    return
                res.append(candidates[i])
                dfs(candidates,target,res,ans,pos)
                res.pop()
        ans = []
        dfs(sorted(candidates),target,[],ans,0)
        return ans
