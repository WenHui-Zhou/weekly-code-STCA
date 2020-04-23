u# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
        if root == None:
            return 0
        money = root.val
        if root.left:
            money += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            money += self.rob(root.right.left) + self.rob(root.right.right)
        return max(money,self.rob(root.left)+self.rob(root.right))
        """
        def dfs(root):
            if root == None:
                return 0,0
            result = [0]*2
            left = dfs(root.left)
            right = dfs(root.right)
            result[0] = max(left[0],left[1]) + max(right[0],right[1])
            result[1] = left[0] + right[0] + root.val
            return result
        res = dfs(root)
        return max(res)
    
