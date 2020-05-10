class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:
            return False
        res = []
        for ll in matrix:
            res += ll
        left = 0
        right = len(res) - 1
    #    res.sort()
        while left <= right:
            mid = (left + right) // 2
            if res[mid] == target:
                return True
            elif res[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
