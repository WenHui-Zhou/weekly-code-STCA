class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mp = {0:1}
        count = 0
        pre = 0
        for val in nums:
            pre += val
            if pre - k in mp:
                count += mp[pre-k]
            if pre in mp:
                mp[pre]+= 1
            else:
                mp[pre] = 1
        return count
            
                
                        

