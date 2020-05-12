# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        
        if root == None:
            return []
        count = 1
        queue = [root]
        ans = []
        res = []
        flag = 0
        level = 0
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            count -= 1

            if node.left:
                queue.append(node.left)
                level += 1
            if node.right:
                queue.append(node.right)
                level += 1
            
            if count == 0:
                ans.append(res[::] if flag == 0 else res[::-1][::])
                res = []
                count = level
                level = 0
                flag = 1 if flag == 0 else 0
               
        return ans
        ans = []
        if root == None:
            return ans
        queue = [root]
        level = 1
        res = []
        flag = 0
        while queue:
            item = queue.pop(0)
            res.append(item.val)
            level -= 1
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
            if level  == 0:
                if flag == 0:
                    ans.append(res[::])
                    flag = 1
                else:
                    ans.append(res[::][::-1])
                    flag = 0
                level = len(queue)
                res  = []
        return ans
        if root == None:
            return []
        ans = []
        queue = [root]
        level = 1
        flag = 0
        res = []
        while queue:
            item = queue.pop(0)
            res.append(item.val)
            level -= 1
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
            if level == 0:
                if flag == 0:
                    ans.append(res[::])
                else:
                    ans.append(res[::][::-1])
                res = []
                flag ^= 1
                level = len(queue)
        return ans"""

        if root == None:
            return []
        ans = []
        res = []
        level = 1
        queue = [root]
        while queue:
            node = queue.pop(0)
            level -= 1
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if level == 0:
                if len(ans) % 2 == 0:
                    ans.append(res[::])
                else:
                    ans.append(res[::-1])
                res = []
                level = len(queue)
        return ans
