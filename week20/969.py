class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if len(A) == 1:
            return []

        max_val, max_pos = -1, -1
        for i, val in enumerate(A):
            if val > max_val:
                max_val, max_pos = val, i

        ans = [max_pos+1, len(A)]
        l1 = A[:max_pos+1]
        l1.reverse()
        l2 = l1 + A[max_pos+1:]
        l2.reverse()
        ans = ans +  self.pancakeSort(l2[:-1])

        return ans
