# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
       
        if head == None or head.next == None:
            return False
        first = head 
        second = head.next
        while second.next and second.next.next:
            first = first.next
            second = second.next.next
            if first == second:
                return True
        return False
        
        if head == None:
            return False
        first = head
        second = head.next
        while second!=None and second.next != None:
            first = first.next
            second = second.next.next
            if first == second:
                return True
        return False
        """

        if head == None:
            return False
        first = head
        second = head.next
        while second and second.next:
            first = first.next
            second = second.next.next
            if first == second:
                return True
        return False




