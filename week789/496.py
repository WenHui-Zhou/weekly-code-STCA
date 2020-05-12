class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for idx,val in enumerate(nums1):
            index = nums2.index(val)
            for i in range(index,len(nums2)):
                if nums2[i] > val:
                    res.append(nums2[i])
                    break
            if len(res) == idx:
                res.append(-1)
        return res

