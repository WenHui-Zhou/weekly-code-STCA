class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        
        stack = []
        # 记录数字的符号, 因为题目说没有负数,说明第一个为正数,设为1
        sign = 1
        # 数字
        num = 0
        # 结果
        res = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "+":
                res += sign * num
                # 为下一次做准备
                num = 0
                sign = 1
            elif c == "-":
                res += sign * num
                # 为下一次做准备
                num = 0
                sign = -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif c == ")":
                res += sign * num
                num = 0
                res = stack.pop() * res + stack.pop()
        res += sign * num
        return res
        """
        def calculate(expression):
            
            res = 0
            num = 0
            sign = 1
            for c in expression:
                if c.isdigit():
                    num = num * 10 + int(c)
                elif c == '+':
                    res += num*sign
                    num = 0
                    sign = 1
                else:
                    res += num*sign
                    sign = -1
                    num = 0
#            print(expression)
            return res + num*sign

        s = ''.join([c for c in s if c != ' '])
        res = 0
        while s != '':
#            print(s)
            in_left = s.rfind('(')
            if in_left >= 0:
                # 有括号
                in_right = s.find(')',in_left)
                expression = s[in_left+1:in_right]
                res = calculate(expression)
                if res >= 0:
                    s = s[:in_left] + str(res) + s[in_right+1:]
                else:
                    if in_left > 0 and s[in_left-1] == '+':
                        s = s[:in_left-1] + str(res) + s[in_right+1:]
                    elif in_left > 0 and s[in_left-1] == '-':
                        s = s[:in_left-1] + '+' + str(-res) + s[in_right+1:]
                    else:
                        if in_left == 0:
                            return res
            else:
                res = calculate(s)
                s = ''
        return res
