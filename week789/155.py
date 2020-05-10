class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_v = sys.maxsize


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if x < self.min_v:
            self.min_v = x


    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            val = self.stack.pop()
            if self.stack == []:
                self.min_v = sys.maxsize
            elif val == self.min_v:
                self.min_v = min(self.stack)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_v



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
