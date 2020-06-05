# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
          
        def dfs(root,res):
            if root == None:
                res += 'None,'
            else:
                res += str(root.val) + ','
                res = dfs(root.left,res)
                res = dfs(root.right,res)

            return res
        res = ''
        res = dfs(root,res)
        return res[:-1]""" 
        def dfs(root,res):
            if root == None:
                res += 'None,'
            else:
                res += str(root.val) + ','
                res = dfs(root.left,res)
                res = dfs(root.right,res)
            return res
        res = ''
        res = dfs(root,res)
        print(res)
        return res[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        
        def dfs(data_list):
            if data_list == []:
                return 
            if data_list[0] == "None":
                data_list.pop(0)
                return
            node = TreeNode(data_list[0])
            data_list.pop(0)
            node.left = dfs(data_list)
            node.right = dfs(data_list)
            return node
        data_list = data.split(',')
        return dfs(data_list)"""
        def dfs(data_list):
            if data_list == []:
                return
            if data_list[0] == 'None':
                data_list.pop(0)
                return
            node = TreeNode(data_list[0])
            data_list.pop(0)
            node.left = dfs(data_list)
            node.right = dfs(data_list)
            return node
        data_list = data.split(',')
        return dfs(data_list)

        


        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root)
