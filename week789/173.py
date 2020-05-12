# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.res = []
        def dfs(root,res):
            if root == None:
                return res
            
            dfs(root.left,res)
            res.append(root.val)
            dfs(root.right,res)
        dfs(root,self.res)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return self.res.pop(0)


    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.res != []



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
