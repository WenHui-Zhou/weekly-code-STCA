# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None:
            return None
        l1 = ListNode(-1)
        l2 = ListNode(-1)
        tmp = l1
        tmp2 = l2
        while head:
            if head.val < x:
                l1.next = ListNode(head.val)
                l1 = l1.next
            else:
                l2.next = ListNode(head.val)
                l2 = l2.next
            head = head.next
        l1.next = tmp2.next
        return tmp.next
