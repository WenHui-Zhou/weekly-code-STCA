class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        
        if nums == []:
            return []
        if k == 1:
            return nums
        if k == len(nums):
            return [max(nums)]
        left2right = [0]*len(nums)
        for i in range(len(nums)-1):
            left2right[i] = max(nums[i:i+k])
        res = []
        for ii in range(len(left2right)-k+1):
            res.append(left2right[ii])
        return res"""
        if nums == []:
            return []
        if k == 1:
            return nums
        if k == len(nums):
            return [max(nums)]
        stack = []
        ans = []
        for idx in range(len(nums)):
            while stack and stack[0] <= idx - k:
                stack.pop(0)
            if stack == [] or nums[stack[-1]] >= nums[idx]:
                stack.append(idx)
                if idx >= k - 1:
                    ans.append(nums[stack[0]])
            else:
                while stack:
                    if nums[stack[-1]] < nums[idx]:
                        stack.pop()
                    else:
                        break
                stack.append(idx)
                if idx >= k - 1:
                    ans.append(nums[stack[0]])
        return ans
