# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left == None:
                root = root.right
            else:
                pre = root.left
                while pre.right != None:
                    pre = pre.right
                pre.right = root.right
                root.right = root.left
                root.left = None
                root = root.right
