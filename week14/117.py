"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
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
        """
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
                level = len(queue)
                for idx,nod in enumerate(queue):
                    if idx + 1 < len(queue):
                        nod.next = queue[idx + 1]
        return root
