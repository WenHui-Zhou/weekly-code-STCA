# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        
        if root == None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        if left != None and left != p and left != q:
            return left
        right = self.lowestCommonAncestor(root.right,p,q)
        if right != None and right != p and right != q:
            return right
        if left != None and right != None:
            return root
        if left == None:
            return right
        else:
            return left
        """
        if root == None or root == q or root == p:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        if left != None and left != p and left != q:
            return left
        right = self.lowestCommonAncestor(root.right,p,q)
        if right != None and right != p and right!= q:
            return right
        if left!=None and right!=None:
            return root
        if left==None:
            return right
        if right == None:
            return left
        
