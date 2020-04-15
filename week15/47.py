class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return []
        ans = []
        def dfs(nums,res,visit):
            if len(res) == len(nums) and res not in ans:
                ans.append(res[::])
            for i in range(len(nums)):
                if visit[i] == 0:
                    visit[i] = 1
                    res.append(nums[i])
                    dfs(nums,res,visit)
                    visit[i] = 0
                    res.pop()
        visit = [0]*len(nums)
        dfs(nums,[],visit)
        return ans

