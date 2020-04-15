# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        
        def dfs(root,res):
            if root == None:
                return
            dfs(root.left,res)
            res.append(root.val)
            dfs(root.right,res)
        res =[]
        dfs(root,res)
        
        return res[k-1]"""
        if root == None:
            return None
        def dfs(root,res):
            if root == None:
                return
            
            dfs(root.left,res)
            res.append(root.val)
            dfs(root.right,res)
        res = []
        dfs(root,res)
        return res[k-1]
