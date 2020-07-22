class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_v = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if self.min_v == [] or  x <= self.min_v[-1]:
            self.min_v.append(x)


    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            val = self.stack.pop()
            if val == self.min_v[-1]:
                self.min_v.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_v[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
