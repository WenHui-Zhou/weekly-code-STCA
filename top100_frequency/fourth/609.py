class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        pas = []
        for path in paths:
            path = path.split(' ')
            for pp in path[1:]:
                pas.append(path[0] + '/' + pp)
    #    print(pas)
        from collections import defaultdict
        dicts = defaultdict(list)
        for path in pas:
            key = path.split('(')[-1][:-1]
            val = path.split('(')[0]
            dicts[key].append(val)
        res = []
        for key,val in dicts.items():
            if len(val) <= 1:
                continue
            res.append(val)
        return res

