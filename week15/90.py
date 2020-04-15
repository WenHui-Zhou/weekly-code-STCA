class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return []
        ans = []
        def dfs(nums,res,lens,visit,pos):
            if len(res) == lens and res not in ans:
                ans.append(res[::])
            for i in range(pos,len(nums)):
                if visit[i] == 0:
                    visit[i] = 1
                    res.append(nums[i])
                    dfs(nums,res,lens+1,visit,i+1)
                    visit[i] -= 1
                    res.pop()
        visit = [0]*len(nums)
        dfs(sorted(nums),[],0,visit,0)
        return ans
