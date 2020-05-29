class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        k = 1
        res = []
        for ii in range(len(nums)):
            res.append(k)
            k *= nums[ii]
        k = 1
        for ii in range(len(nums))[::-1]:
            res[ii] *= k
            k *= nums[ii]
        return res
        """
        k = 1
        res = []
        for val in nums:
            res.append(k)
            k *= val
        k = 1
        for i in range(len(nums))[::-1]:
            res[i] *= k
            k*=nums[i]
        return res
