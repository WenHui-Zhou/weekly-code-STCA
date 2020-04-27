class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(R):
            for j in range(C):
                dis = abs(i-r0) + abs(j-c0)
                temp = [dis,[i,j]]
                res.append(temp[::])
        res.sort(key = lambda x:x[0])
        ans = []
        for item in res:
            ans.append(item[1])
        return ans
            
