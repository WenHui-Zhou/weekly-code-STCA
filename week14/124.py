# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [-sys.maxsize]
        if root == None:
            return 0
        def dfs(root,res):
            if root == None:
                return 0
            left = max(dfs(root.left,res),0)
            right = max(dfs(root.right,res),0)
            ans = left + right + root.val
            if ans > res[0]:
                res[0] = ans
            return root.val + max(left,right)
        
        dfs(root,res)
        return res[0]
