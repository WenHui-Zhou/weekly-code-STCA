# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(r1,r2):
            if r1 == None and r1 == None:
                return True
            if r1 == None or r2 == None:
                return False
            return (r1.val == r2.val) and dfs(r1.left,r2.right) and dfs(r1.right,r2.left)
        return dfs(root,root)
