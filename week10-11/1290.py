# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        if head == None:
            return 0
        ans = 0
        while head and head.next:
            ans += head.val
            ans *= 2
            head = head.next
        ans += head.val
        return ans
        
