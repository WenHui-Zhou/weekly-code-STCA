"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        def dfs(root):
            if root == None:
                return 0
            depth = 0
            for ch in root.children:
                if ch:
                    depth = max(depth,dfs(ch))
        #    depth += 1
        #    print(root.val,depth)
            return depth + 1
        return dfs(root)
