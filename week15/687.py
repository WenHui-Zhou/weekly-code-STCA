# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def dfs(root):
            if root == None:
                return 0
            lleft = dfs(root.left)
            lright = dfs(root.right)
            l_a = 0
            r_a = 0
            if root.left and root.left.val == root.val:
                l_a = lleft + 1
            if root.right and root.right.val == root.val:
                r_a = lright + 1
            self.ans = max(self.ans,l_a + r_a)
            return max(l_a,r_a)
        dfs(root)
        return self.ans
