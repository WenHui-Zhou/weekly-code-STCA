# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        queue = [root]
        level = 1
        tmp = []
        ans = []
        while queue:
            node = queue.pop(0)
            level -= 1
            tmp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if level == 0:
                ans.append(tmp[::])
                tmp = []
                level = len(queue)
        return ans
