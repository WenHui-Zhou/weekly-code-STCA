class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        stack = []
        for c in s:
            if c in ['(','{','[']:
                stack.append(c)
            else:
                if stack == []:
                    return False
                if c == ']':
                    if stack[-1]!='[':
                        return False
                    else:
                        stack.pop()
                elif c == ')':
                    if stack[-1] != '(':
                        return False
                    else:
                        stack.pop()
                if c == '}':
                    if stack[-1] != '{':
                        return False
                    else:
                        stack.pop()
        if stack == []:
            return True
        else:
            return False

