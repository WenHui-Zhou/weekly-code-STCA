# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        queue = [root]
        level = 1
        res = [root.val]
        while queue:
            node = queue.pop(0)
            level -= 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if level == 0:
                level = len(queue)
                if level == 0:
                    return res
                tmp = max([node.val for node in queue])
                res.append(tmp)
            
