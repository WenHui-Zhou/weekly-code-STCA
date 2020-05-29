# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        
        if head == None or head.next == None:
            return head
        pre = None 
        cur = head
        last = head.next
        while last!=None:
            cur.next = pre
            pre = cur
            cur = last 
            last = last.next
        cur.next = pre
        return cur
        
        if head == None or head.next == None:
            return head
        pre = None
        cur = head
        last = cur.next
        while last:
            cur.next = pre
            pre = cur
            cur = last 
            last = cur.next
        cur.next = pre
        return cur"""
        if head == None or head.next == None:
            return head
        pre = head.next
        cur = head
        cur.next = None
        while pre:
            tmp = pre.next
            pre.next = cur
            cur = pre
            pre = tmp
        return cur
