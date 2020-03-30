# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        n = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            n += 1
        k  %= n
        if k== 0:
            return head
        k = n - k
        tmp = head
        for _ in range(k-1):
            tmp = tmp.next
        new_head = tmp.next
        tmp.next = None
        tmp = new_head
        while tmp and tmp.next:
            tmp = tmp.next
        tmp.next = head
        return new_head

