class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
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
