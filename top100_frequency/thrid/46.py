class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        
        if nums == []:
            return []
        def dfs(nums,res,ans,visit):
            if len(res) == len(nums):
                ans.append(res[::])
            for i in range(len(nums)):
                if visit[i] == 1:
                    continue
                res.append(nums[i])
                visit[i] = 1
                dfs(nums,res,ans,visit)
                res.pop()
                visit[i] = 0
        ans = []
        visit = [0]*len(nums)
        dfs(nums,[],ans,visit)
        return ans"""
        if nums == []:
            return nums
        def dfs(nums,visit,ans,res):
            if len(res) == len(nums):
                ans.append(res[::])
                return
            for i in range(len(nums)):
                if visit[i] == 0:
                    visit[i] = 1
                    res.append(nums[i])
                    dfs(nums,visit,ans,res)
                    res.pop()
                    visit[i] = 0
        visit = [0]*len(nums)
        ans = []
        dfs(nums,visit,ans,[])
        return ans
