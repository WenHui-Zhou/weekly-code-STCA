class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        score = 0
        for ch in ops:
            if ch == 'C':
                stack.pop()
            elif ch =='D':
                stack.append(stack[-1]*2)
            elif ch == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(ch))
        return sum(stack)

