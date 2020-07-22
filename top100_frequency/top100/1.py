class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        if nums == []:
            return []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        if nums == []:
            return []
        for idx,val in enumerate(nums):
            for j in range(idx+1,len(nums)):
                if val + nums[j] == target:
                    return [idx,j]"""
        dicts = {}
        for idx,val in enumerate(nums):
            if target - val in dicts:
                return [dicts[target-val],idx]
            else:
                dicts[val] = idx
        
