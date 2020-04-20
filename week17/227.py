class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
       
        res = 0
        stack = []
        oper = []
        cur = 0
        for i in range(len(s)):
#            print(stack)
#            print(oper)
            if s[i] in ['+','-','*','/']:
                stack.append(int(s[cur:i].strip()))
                cur = i + 1
                if not oper:
                    oper.append(s[i])
                else:
                    while True:
          #              print(stack)
          #              print(oper)
                        if oper[-1] in ['*','/']:
                            oper2 = stack.pop(-1)
                            oper1 = stack.pop(-1)
                            if oper[-1] == '*':
                                stack.append(oper1*oper2)
                            else:
                                stack.append(oper1//oper2)
                            oper.pop(-1)

                        elif s[i] in ['*','/']:
                       #     oper.append(s[i])
                            break
                        else:
                 #           print(oper[-1])
                            oper2 = stack.pop(-1)
                            oper1 = stack.pop(-1)
      #                      print(oper1,oper2)
                            if oper[-1] == '+':
                                stack.append(oper1+oper2)
                            else:
                                stack.append(oper1-oper2)
                            oper.pop(-1)
                        if  not oper:
                            break
                    oper.append(s[i])
        stack.append(int(s[cur:]))
#        print(stack)
#        print(oper)
        for i in oper[::-1]:
#            print(stack)
            oper1 = stack.pop(-1)
            oper2 = stack.pop(-1)
            if i == '*':
                stack.append(oper1*oper2)
            elif i == '/':
                stack.append(oper2//oper1)
            elif i == '+':
                stack.append(oper1 + oper2)
            else:
                stack.append(oper2 - oper1)
            
        return stack[-1] """
        stack = []
        oper = []
        res = {'+':0,'-':0,'*':1,'/':1}
        flag = 1
        for c in s:
            if '0'<=c<='9':
                if flag == 0:
                    stack[-1] = stack[-1]*10 + int(c)
                else:
                    stack.append(int(c))
                flag = 0
            elif c in res.keys():
                flag = 1
                while oper != [] and (res[c] <= res[oper[-1]]) :
                #    print(oper,stack)
                    ch = oper.pop()
                #    oper.append(c)
                    op1,op2 = stack.pop(),stack.pop()
                    if ch =='*':
                        stack.append(op1*op2)
                    elif ch == '/':
                        stack.append(op2 // op1)
                    elif ch == '-':
                        stack.append(op2 - op1)
                    else:
                        stack.append(op1+op2)
                oper.append(c)
    #    print(oper,stack)      
        while oper:
            ch = oper.pop()
            op1 = stack.pop()
            op2 = stack.pop()
            if ch == '+':
                stack.append(op1+op2)
            elif ch == '-':
                stack.append(op2-op1)
            elif ch == '*':
                stack.append(op1*op2)
            else:
                stack.append(op2//op1)
        return stack[-1]
