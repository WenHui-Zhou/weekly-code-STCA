"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        
        if root == None:
            return None
        count = 1
        level = 0
        res = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            count -= 1
            res.append(node)
            if node.left:
                queue.append(node.left)
                level += 1
            if node.right:
                queue.append(node.right)
                level += 1
            if count == 0:
                count = level
                level = 0
                for i in range(len(res)-1):
                    res[i].next = res[i+1]
                res = []
        return root
        if root == None:
            return None
        queue = [root]
        level = 1
        
        while queue:
            node = queue.pop(0)
            level -= 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if level == 0:
                node.next = None
                level = len(queue)
            else:
                node.next = queue[0]
        return root"""
        if not root:
            return root
        queue = [root]
        level = 1
        while queue:
            node = queue.pop(0)
            level -= 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if level == 0:
                level = len(queue)
                for i in range(len(queue)-1):
                    queue[i].next = queue[i+1]
        return root
