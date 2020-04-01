# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        queue = [root]
        level = 1
        ans = []
        tmp = []
        while queue:
            node = queue.pop(0)
            tmp.append(node.val)
            level -= 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if level == 0:
                ans.append(tmp[::])
                level = len(queue)
                tmp = []
        return ans[::-1]
