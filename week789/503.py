class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lens = len(nums)
        nums += nums
        res = []
        for idx,val in enumerate(nums):
            if idx == lens:
                break
            for i in range(idx+1,idx + lens +1):
                if val < nums[i]:
                    res.append(nums[i])
                    break
            if len(res) == idx:
                res.append(-1)
        return res
