# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nest):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nes = []
        
        def dfs(nest):
            for c in nest:
                if not c.isInteger():
                    a = dfs(c.getList())
                    if a != None:
                        self.nes.extend(a)
                else:
                    self.nes.append(c)
        dfs(nest)
  #      print(self.nes)
        self.index = 0
        
    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            self.index += 1
            return self.nes[self.index-1]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index >= len(self.nes):
            return False
        else:
            return True
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
