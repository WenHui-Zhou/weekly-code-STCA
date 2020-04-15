# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        def dfs(root,low=-sys.maxsize,high=sys.maxsize):
            if root == None:
                return True
            val = root.val
            if not(low < val < high):
                return False
            if not dfs(root.left,low,val):
                return False
            if not dfs(root.right,val,high):
                return False
            return True
        return dfs(root)

