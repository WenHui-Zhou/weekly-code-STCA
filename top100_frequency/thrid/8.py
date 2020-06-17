class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        res = ''
        for idx,ch in enumerate(str):
            if ch in ['-','+'] and idx == 0:
                res += ch
            elif '0' <= ch <= '9':
                res += ch
            else:
                break
        if res == '':
            return 0
        if len(res) == 1 and res in ['-','+']:
            return 0
        import sys
        if int(res) < -2**31:
            return -2**31
        if int(res) > 2**31-1:
            return 2**31-1
        return int(res)
