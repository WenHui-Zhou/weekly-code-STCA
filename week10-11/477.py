class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum([a.count('1')*a.count('0') for a in zip(*map('{:032b}'.format,nums))])

