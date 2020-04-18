# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        
        if nums == []:
            return None
       
        
        def dfs(nums,begin,end):
            if begin == end:
                return None
            mid = (begin + end) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(nums,begin,mid)
            root.right = dfs(nums,mid + 1,end)
            return root
        return dfs(nums,0,len(nums))
        """
        if nums == []:
            return None
        def dfs(nums,begin,end):
            if begin == end:
                return None
            mid = (begin + end)// 2
            root = TreeNode(nums[mid])
            root.left = dfs(nums,begin,mid)
            root.right = dfs(nums,mid+1,end)
            return root
        return dfs(nums,0,len(nums))
