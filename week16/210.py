class Solution(object):
    def findOrder(self, numC, pre):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        course = {} #xianxiu:houxiu
        rudu = {}
        for i in range(numC):
            course[i] = []
            rudu[i] = 0
        for cour in pre:
            course[cour[1]].append(cour[0])
            rudu[cour[0]] += 1
        queue = []
        for c in rudu.keys():
            if rudu[c] == 0:
                queue.append(c)
        res = []
        while queue:
            index = queue.pop(0)
            res.append(index)
            for i in course[index]:
                if rudu[i] == 0:
                    continue
                else:
                    rudu[i] -= 1
                    if rudu[i] == 0:
                        queue.append(i)
        if len(res) != numC:
            return []
        return res
