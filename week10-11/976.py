class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        A = A[::-1]
        for i in range(len(A)-2):
                    if A[i+1] + A[i+2] > A[i]:
                        return A[i+1] + A[i+2] + A[i]
        return 0
