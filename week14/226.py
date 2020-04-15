# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        
        if root == None:
            return
        Node = TreeNode(root.val)
        Node.left = self.invertTree(root.right)
        Node.right = self.invertTree(root.left)
        return Node
        """
        """
        if root == None:
            return None
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left,root.right = root.right,root.left
        return root
        if root == None:
            return None
        queue = [root]
        while queue:
            node = queue.pop(0)
            node.left,node.right = node.right,node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
        """
        if root == None:
            return None
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left,root.right = root.right,root.left
        return root
