class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        
        from collections import defaultdict
        dict = defaultdict(list)
        for val in strs:
            dict[''.join(sorted(val))].append(val)
        res = []
        for val in dict.values():
            res.append(val)
        return res"""
        from collections import defaultdict
        dicts = defaultdict(list)
        if strs == []:
            return []
        for val in strs:
            dicts[''.join(sorted(val))].append(val)
        ans = []
        for key,val in dicts.items():
            ans.append(val)
        return ans

