class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(pos,res):
            ans.append(res[::])
            for i in range(pos,len(nums)):
            #    res.append(nums[i])
                dfs(i+1,res+[nums[i]])
            #    res.pop()
        
        dfs(0,[])    
        return ans        
