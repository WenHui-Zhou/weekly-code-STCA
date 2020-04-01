# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def dfs(root,sum,addup):
            if root.left == None and root.right == None:
                if addup + root.val == sum:
                    return True
                else:
                    return False
            
            if  root.left and dfs(root.left,sum,addup + root.val):
                return True
            if root.right and dfs(root.right,sum,addup + root.val):
                return True
            return False
        if root == None:
            return False
        return dfs(root,sum,0)
