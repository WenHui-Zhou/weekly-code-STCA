class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        class compare(str):
            def __lt__(x,y):
                return x + y > y + x
        res = ''.join(sorted(map(str,nums),key = compare))
        return '0' if res[0] == '0' else res
