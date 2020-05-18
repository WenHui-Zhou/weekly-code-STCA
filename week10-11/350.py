class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        
        adict = {}
        for c in nums1:
            if c not in adict:
                adict[c] = 1
            else:
                adict[c] += 1
        bdict = {}
        for c in nums2:
            if c not in bdict:
                bdict[c] = 1
            else:
                bdict[c] += 1
        res = []
        for key in adict:
            if key in bdict:
                res.extend([key]*min(adict[key],bdict[key]))
        return res
        if nums1 == [] or nums2 == []:
            return []
        res = []
        for item in set(nums1):
            if nums2.count(item) > 0:
                res += [item]*min(nums1.count(item),nums2.count(item))
        return res"""
        nums1.sort()
        nums2.sort()
        cur1 = 0
        cur2 = 0
        res = []
        while cur1 < len(nums1) and cur2 < len(nums2):
            if nums1[cur1] == nums2[cur2]:
                res.append(nums1[cur1])
                cur1 += 1
                cur2 += 1
            elif nums1[cur1] < nums2[cur2]:
                cur1 += 1
            else:
                cur2 += 1
        return res

