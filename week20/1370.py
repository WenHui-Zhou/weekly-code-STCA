class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp_s = sorted(list(set(s)))
        tmp_d = {}
        for val in s:
            if val not in tmp_d:
                tmp_d[val] = 1
            else:
                tmp_d[val] += 1
        res = []
        while len(res) < len(s):
            # right 2 left
            for val in tmp_s:
                if tmp_d[val] > 0:
                    res.append(val)
                    tmp_d[val] -= 1
            for val in tmp_s[::-1]:
                if tmp_d[val] > 0:
                    res.append(val)
                    tmp_d[val] -= 1
        return ''.join(res)
