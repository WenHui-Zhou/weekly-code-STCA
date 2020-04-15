# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        cur = root
        queue = []
        while cur or queue:
            while cur:
                queue.append(cur)
                ans.append(cur.val)
                cur = cur.left
            cur = queue.pop()
            cur = cur.right
        return ans
