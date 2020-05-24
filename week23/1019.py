# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if head  == None:
            return []
        res = []
        stack = []
        index = 0
        while head:
            res.append(0)
            if stack == []:
                stack.append([head.val,index])
            else:
                while stack and head.val > stack[-1][0]:
                    point = stack.pop(-1)
                    res[point[1]] = head.val
                stack.append([head.val,index])
            head = head.next
            index += 1
        return res
            
