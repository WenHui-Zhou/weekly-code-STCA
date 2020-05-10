class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
       
        if nums == []:
            return 0
        res = 1
        flag = -2
        for kk in range(1,len(nums)):
            if flag == -2:
                if nums[kk] > nums[kk -1]:
                    flag = 1
                    res += 1
                elif nums[kk] < nums[kk-1]:
                    flag = -1
                    res += 1
            
            elif nums[kk] > nums[kk-1] and flag == -1:
                res += 1
                flag = 1
            elif nums[kk] < nums[kk - 1] and flag == 1:
                res += 1
                flag = -1
        return res """
        res = 1
        if len(nums) >= 2:
            kk = 1
            while kk < len(nums):
                if nums[kk-1] == nums[kk]:
                    kk += 1
                else:
                    break
            nums = nums[kk-1:]
            if len(nums) <= 1:
                return len(nums)
            if nums[0] > nums[1]:
                flag = 1 # down
            else:
                flag = 0 # up
        else:
            return len(nums)
        tmp = nums[0]  
        for kk in range(1,len(nums)):
            if nums[kk] > tmp:
                if flag == 0:
                    res += 1
                    flag = 1
                    tmp = nums[kk]
                else:
                    tmp = max(tmp,nums[kk])
            else:
                if nums[kk] == tmp:
                    tmp = min(tmp,nums[kk])
                    continue
                if flag == 1:
                    res += 1
                    flag = 0
                    tmp = nums[kk]
                else:
                    tmp = min(tmp,nums[kk])
        return res
