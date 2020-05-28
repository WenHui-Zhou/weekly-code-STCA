class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.stack = []
        self.capacity = capacity
        self.dict = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.stack:
            return -1
        else:
            self.stack.pop(self.stack.index(key))
            self.stack.insert(0,key)
            return self.dict[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.stack:
            self.stack.pop(self.stack.index(key))
            self.stack.insert(0,key)
            self.dict[key] = value
        else:
            if len(self.stack) == self.capacity:
                self.stack.pop()
            self.stack.insert(0,key)
            self.dict[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
