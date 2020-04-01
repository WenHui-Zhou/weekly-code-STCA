class Solution(object):
    def insert(self, inter, newIn):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        
        if intervals == []:
            return [newInterval]
        if newInterval == []:
            return intervals
        new_inter = []
        for item in intervals:
            if newInterval == [] or item[1] < newInterval[0]:
                new_inter.append(item[::])
            elif newInterval[1] < item[0]:
                new_inter.append(newInterval[::])
                newInterval = []
                new_inter.append(item[::])
            else:
                newInterval[0] = min(newInterval[0],item[0])
                newInterval[1] = max(newInterval[1],item[1])
        if newInterval!=[]:
            new_inter.append(newInterval[::])
        return new_inter"""
        if inter == [] or inter[0] == []:
            return [newIn]
        res = []
        flag = 0
        for data in inter:
            left,right = data
            if newIn != [] and (left <= newIn[0] <=right or left <= newIn[1] <= right or newIn[0]<=left and newIn[1] >= right):
                newIn[0] = min(left,newIn[0])
                newIn[1] = max(right,newIn[1])
                flag = 1
            else:
                if newIn != [] and (flag == 1 or left > newIn[1]):
                    res.append(newIn[::])
                    flag = 0
                    newIn = []
                res.append(data)
        if flag == 1:
            res.append(newIn)
        if newIn!= [] and  res[-1][1] < newIn[0]:
            res.append(newIn)
        return res
        
