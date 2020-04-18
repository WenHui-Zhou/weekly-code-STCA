# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    index = 0
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        
        if preorder == []:
            return None
        def dfs(preorder,inorder):
        #    print(self.index)
            if self.index == len(preorder) or inorder == [] or preorder[self.index] not in inorder:
                return None
            root = TreeNode(preorder[self.index])
            left = inorder[:inorder.index(preorder[self.index])]
            right = inorder[inorder.index(preorder[self.index])+1:]
            self.index += 1
            root.left = dfs(preorder,left)
            root.right = dfs(preorder,right)
            return root
        return dfs(preorder,inorder)"""
        def dfs(preorder,inorder):
        #    print(preorder)
        #    print(inorder)
            if inorder == []:
                return None
            pos = inorder.index(preorder[0])
            root = TreeNode(preorder[0])
            preorder.pop(0)
            root.left = dfs(preorder,inorder[:pos])
            root.right = dfs(preorder,inorder[pos+1:])
            return root
        return dfs(preorder,inorder)            
