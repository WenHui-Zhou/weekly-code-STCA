# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = head
        n = 0
        while tmp != None:
            n += 1
            tmp = tmp.next
        n //= 2
        tmp = head
        for i in range(n):
            tmp = tmp.next

        return tmp
