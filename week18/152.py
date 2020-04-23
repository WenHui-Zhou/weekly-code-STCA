class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
       
        import sys
        maxx = -sys.maxsize
        if nums == []:
            return 0
        imax = 1
        imin = 1
        for ii in range(len(nums)):
            if nums[ii] < 0:
                imax,imin = imin,imax
            imax = max(nums[ii],imax*nums[ii])
            imin = min(nums[ii],imin*nums[ii])
            maxx = max(imax,maxx)
        return maxx
         """
        import sys
        ans = -sys.maxsize
        imax = 1
        imin = 1
        for i in range(len(nums)):
            if nums[i] < 0:
                imax,imin = imin,imax
            imax = max(nums[i],imax*nums[i])
            imin = min(nums[i],imin*nums[i])
            ans = max(ans,imax)
        return ans

