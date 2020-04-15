# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder == []:
            return None
        def dfs(inorder,postorder):
            if inorder == []:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            index = inorder.index(val)
            root.right = dfs(inorder[index+1:],postorder)
            root.left = dfs(inorder[:index],postorder)
            
            return root
        return dfs(inorder,postorder)
