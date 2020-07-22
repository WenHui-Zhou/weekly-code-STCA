# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        
        dummy = ListNode(-1)
        dummy.next = head
        last = dummy 
        fast = dummy 
        for i in range(n+1):
            fast = fast.next
        while fast != None:
            last = last.next
            fast = fast.next
        last.next = last.next.next
        return dummy.next
        
        if head == None:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        first = dummy
        second =dummy
        for _ in range(n+1):
            first = first.next
        while first!=None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next"""
        if head == None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        first = dummy
        for i in range(n+1):
            first = first.next
        second = dummy
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
        
