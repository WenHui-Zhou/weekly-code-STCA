class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if path == '':
            return ''
        path = path.split('/')
        stack = []
        for word in path:
            if word == '..':
                if stack:
                    stack.pop()
            elif word == '.' or word == '':
                pass
            else:
                stack.append(word)
        return '/' + '/'.join(stack)
            
