class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if s == '':
            return s
        res = []
        tmp = k
        while tmp < len(s):
            res.append(s[tmp-k:tmp])
            tmp += k
        if s[tmp-k:tmp] != []:
            res.append(s[tmp-k:tmp])
        ans = ''
        for idx,ss in enumerate(res):
            if idx %2 == 0:
                ans += ss[::-1]
            else:
                ans += ss
        return ans
