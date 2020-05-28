class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        
        if intervals == []:
            return intervals
        intervals = sorted(intervals,key= lambda x:x[0])
        new_inter = [intervals[0]]
        for item in intervals[1::]:
            if new_inter[-1][-1] >= item[0]:
                new_inter[-1][-1] = max(new_inter[-1][-1],item[-1])
            else:
                new_inter.append(item[::])
        return new_inter
        
        if intervals == []:
            return []
        intervals.sort(key = lambda x:x[0])
        res = [intervals[0]]
        last = res[0][1]
        for i in range(1,len(intervals)):
            left,right = intervals[i]
            if left <= last:
                res[-1][1] = max(right,last)
            else:
                res.append([left,right])
            last = max(last,right)
        return res"""

        if intervals == []:
            return []
        intervals.sort(key=lambda x:(x[0],x[1]))
        last = intervals[0][1]
        res = [intervals[0]]
        for inter in intervals:
            if inter[0] <= last:
                last = max(last,inter[1])
            else:
                res[-1][1] = last
                res.append(inter)
                last = inter[1]
        if last != res[-1][1]:
            res[-1][1] = last
        return res
