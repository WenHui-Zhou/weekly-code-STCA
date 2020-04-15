class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < k:
            return []
        ans = []
        def dfs(nums,k,visit,res,pos):
            if len(res) == k:
                ans.append(res[::])
            for i in range(pos,len(nums)):
                if visit[i] == 0:
                    visit[i] = 1
                    res.append(nums[i])
                    dfs(nums,k,visit,res,i+1)
                    visit[i] = 0
                    res.pop()
        nums = range(1,n+1)
        visit = [0]*n
        dfs(nums,k,visit,[],0)
        return ans

