class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.res = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        import bisect
        self.res.insert(bisect.bisect(self.res,num),num)

       
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.res) == 0:
            return 0
        if len(self.res) %2 != 0:
            return self.res[len(self.res) // 2]
        else:
            return (self.res[len(self.res) // 2 ] + self.res[len(self.res) // 2 -1]) / 2.0
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
