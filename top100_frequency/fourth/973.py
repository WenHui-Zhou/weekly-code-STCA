class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        
        if points == []:
            return []
        res = [0]*len(points)
        for i in range(len(points)):
            res[i] = points[i][0]**2 + points[i][1]**2
        idx = sorted(enumerate(res),key=lambda x:x[1])
        ans = []
        for i in range(k):
            ans.append(points[idx[i][0]])
        return ans
        """
        if points == []:
            return []
        res = [0]*len(points)
        for i in range(len(points)):
            res[i] = points[i][0]**2 + points[i][1]**2
        idx = sorted(enumerate(res),key = lambda x:x[1])
        ans = []
        for i in range(k):
            ans.append(points[idx[i][0]])
        return ans

