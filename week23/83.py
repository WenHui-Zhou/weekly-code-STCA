# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        first = head
        while first != None and first.next!=None:
            if first.val == first.next.val:
                first.next = first.next.next
            else:
                first = first.next
        return head
        """
        if head == None:
            return head
        first = head
        second = head.next
        while second:
            while first.val == second.val:
                if second.next:
                    second = second.next
                else:
                    first.next = None
                    return head
            first.next = second
            first = second
            second = first.next
        return head
