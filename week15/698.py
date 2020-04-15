class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if nums == []:
            return True
        target = sum(nums) // k
        if target != sum(nums) / k:
            return False
        nums.sort()
        if nums[-1] > target:
            return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1
        def dfs(groups):
            if not nums:
                return True
            v = nums.pop()
            for i,group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if dfs(groups):
                        return True
                    groups[i] -= v
                if not group:
                    break
            nums.append(v)
            return False
        return dfs([0]*k)
