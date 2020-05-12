class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if sum(A) % 3 != 0:
            return False
        thresh = sum(A) // 3
        n,i,cur = len(A),0,0
        while i < n:
            cur += A[i]
            if cur == thresh:
                break
            i += 1
        if cur != thresh:
            return False
        j = i + 1
        while j+1 < n:
            cur += A[j]
            if cur == thresh*2:
                return True
            j += 1
        return False
        

