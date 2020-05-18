class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        
        if nums1 == [] or nums2 == []:
            return []
        res = []
        for item in nums1:
            if item in nums2:
                res.append(item)
        return list(set(res))
        """
        n1 = {}
        res = []
        for val in set(nums1):
            n1[val] = 1
        for val in set(nums2):
            if val in n1:
                res.append(val)
        return res

