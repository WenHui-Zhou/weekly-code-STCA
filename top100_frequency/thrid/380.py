class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.adict  = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.adict:
            return False
        self.adict[val] = 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.adict:
            return False
        self.adict.pop(val)
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        keys = list(self.adict.keys())
        import random
        a = random.randint(0,len(keys) - 1)
        return keys[a]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
