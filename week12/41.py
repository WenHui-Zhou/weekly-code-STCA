class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        if nums == []:
            return 1
        res = [0]* (len(nums) + 1)
        for i in nums:
            if i < 0 or i > len(nums):
                continue
            res[i] = 1
        for i in range(1,len(res)):
            if res[i] == 0:
                return i
        return len(res)
        
        i = 0
        while i < len(nums):
            if (0 >= nums[i] or nums[i] > len(nums)) or nums[i] == i + 1 or nums[nums[i]-1] == nums[i]:
                i += 1
                continue
            else:
                tmp = nums[i]
                nums[i] = nums[tmp-1]
                nums[tmp-1] = tmp
    #            print(nums)
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
       
        return len(nums) + 1
        """
        if nums == []:
            return 1
        cur = 0
        while cur < len(nums):
            if nums[cur] <= 0 or nums[cur] > len(nums) or nums[cur] == cur + 1 or nums[nums[cur] - 1] == nums[cur]:
                cur += 1
            else:
                tmp = nums[cur]
                nums[cur] = nums[nums[cur] - 1]
                nums[tmp - 1] = tmp
                
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
