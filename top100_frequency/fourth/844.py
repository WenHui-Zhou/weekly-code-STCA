class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        
        stack1 = []
        stack2 = []
        for ch in S:
            if ch == '#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(ch)
        for ch in T:
            if ch =='#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(ch)
        return stack1 == stack2
        """
        stack1 = []
        stack2 = []
        for c in S:
            if c == '#':
                if stack1 != []:
                    stack1.pop()
            else:
                stack1.append(c)
        for c in T:
            if c == '#':
                if stack2 != []:
                    stack2.pop()
            else:
                stack2.append(c)
        return stack1 == stack2
   
