# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def get_ans(start,end):
            ans = []
            if start > end:
                ans.append(None)
                return ans
            if start == end:
                ans.append(TreeNode(start))
                return ans
            for i in range(start,end + 1):
                left = get_ans(start,i - 1)
                right = get_ans(i+1,end)
                for left_t in left:
                    for right_t in right:
                        root = TreeNode(i)
                        root.left = left_t
                        root.right = right_t
                        ans.append(root)
            return ans
        if n == 0:
            return []
        
    #    print(get_ans(1,n,ans))
        return get_ans(1,n)
