class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        
        word = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = 0
        flag = 0
        for  i in range(len(s))[::-1]:
            c = s[i]
            if c in ['I','X','C']:
                if i + 1 < len(s) and word[s[i+1]] > word[s[i]]:
                    res -= word[c]
                    flag = 1
            if flag == 0:
                res += word[c]
            flag = 0
        return res"""
        ch_map = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        res = 0
        i = len(s) - 1
        while i >= 0:
            if i >= 1 and ch_map[s[i-1]] < ch_map[s[i]]:
                    res += ch_map[s[i]] - ch_map[s[i-1]]
                    i -= 2
            else:
                res += ch_map[s[i]]
                i -= 1
        return res



