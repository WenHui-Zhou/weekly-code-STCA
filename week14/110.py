# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = [True]
        def dfs(root,res):
            if res[0] == False:
                return False
            if root == None:
                return 0
            left = dfs(root.left,res)
            if res[0] == False:
                return False
            right = dfs(root.right,res)
            if abs(left - right) >= 2:
                res[0] = False 
            return max(left,right) + 1 
        dfs(root,res)
        return res[0]

