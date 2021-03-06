class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        
        stack,res,multi = [],'',0
        for c in s:
            if c == '[':
                stack.append([multi,res])
                multi,res = 0,''
            elif c == ']':
                cur_multi,last_res = stack.pop()
                res = last_res + cur_multi*res
            elif '0' <= c <= '9':
                multi = multi*10 +int(c)
            else:
                res += c
        return res
        """
        stack,res,multi = [],'',0
        for c in s:
            if '0' <= c <= '9':
                multi = multi*10 + int(c)
            elif c == '[':
                stack.append([multi,res])
                multi = 0
                res = ''
            elif c ==']':
                cur_multi,pre = stack.pop()
                res = pre + cur_multi * res
            else:
                res += c
        return res

