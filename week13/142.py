# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        first = head
        second = head.next
        while second != first:
            if second == None or second.next == None:
                return None
            first = first.next
            second = second.next.next
        dummy = ListNode(-1)
        dummy.next = head
        first = dummy
        while first != second:
            first = first.next
            second = second.next
        return first
