class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        
        n = len(nums1)
        m = len(nums2)
        
        stack = []
        while len(stack) < (n+m) // 2 + 1:
            if nums1 == []:
                stack.append(nums2.pop(0))
            elif nums2 == []:
                stack.append(nums1.pop(0))
            elif nums1[0] < nums2[0]:
                stack.append(nums1.pop(0))
            else:
                stack.append(nums2.pop(0))
        return stack[-1] if (n+m) % 2 != 0 else (stack[-1] + stack[-2]) / 2.0
        n = len(nums1)
        m = len(nums2)
        stack = []
        while len(stack) < (m+n) // 2 + 1:
            if nums1 == []:
                stack.append(nums2.pop(0))
            elif nums2 == []:
                stack.append(nums1.pop(0))
            elif nums1[0] > nums2[0]:
                stack.append(nums2.pop(0))
            else:
                stack.append(nums1.pop(0))
        return stack[-1] if (m+n) % 2 == 1 else (stack[-1] + stack[-2]) / 2.0"""
        k1 = (len(nums1) + len(nums2) + 1) // 2
        k2 = (len(nums1) + len(nums2) + 2) // 2
        def helper(nums1,nums2,k):
            if len(nums1) < len(nums2):
                nums1,nums2 = nums2,nums1
            if nums2 == []:
                return nums1[k-1]
            if k == 1:
                return min(nums1[0],nums2[0])
            t = min(k//2, len(nums2))
            if nums1[t-1] >= nums2[t-1]:
                return helper(nums1,nums2[t:],k-t)
            else:
                return helper(nums1[t:],nums2,k-t)
        return (helper(nums1,nums2,k1) + helper(nums1,nums2,k2)) / 2.0










