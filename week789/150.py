class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        
        stack = []
        for num in tokens:
            if num not in ['+','-','*','/']:
                stack.append(int(num))
            else:
                oper2 = stack.pop(-1)
                oper1 = stack.pop(-1)
                if num == '+':
                    stack.append(oper1 + oper2)
                elif num == '-':
                    stack.append(oper1 - oper2)
                elif num == '*':
                    stack.append(oper1 * oper2)
                else:
              #      if abs(oper1) < abs(oper2):
              #          stack.append(0)
              #          continue
                    if oper1 * oper2 >= 0:
                        stack.append(int(oper1 // oper2))
                    else:
                        stack.append(int(-(-oper1 // oper2)))
#            print(stack)
        return stack[-1]
        """
        stack = []
        for val in tokens:
            if val not in ['+','-','*','/']:
                stack.append(int(val))
            else:
                if val == '+':
                    stack.append(stack.pop() + stack.pop())
                elif val == '-':
                    stack.append(-(stack.pop() - stack.pop()))
                elif val == '*':
                    stack.append(stack.pop()*stack.pop())
                else:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    if val1 *val2 >= 0:
                        stack.append(int(val2 // val1))
                    else:
                        stack.append(int(-(-val2 // val1)))
#            print(stack)
        return stack[-1]
