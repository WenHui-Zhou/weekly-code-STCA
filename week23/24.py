# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        
        if head == None or head.next == None:
            return head
        first = head
        second = head.next
        head = second
        last = second.next
        first.next = last
        second.next = first
        while last and last.next:
            first.next = last.next
            first = last
            second = last.next
            last = second.next
            second.next = first
            first.next = last
        return head
       
        if head == None:
            return head
        first = head 
        second = head.next
        new_head = second if second!=None else first
        while second != None:
            first.next = second.next
            tmp = first
            second.next = first
            first = first.next
            if first == None:
                break
            else:
                second = first.next
            if second!=None:
                tmp.next = second
        return new_head
         """

        dummy = ListNode(-1)
        dummy.next = head
        if head == None or head.next == None:
            return head
        pre = dummy
        first = head
        second = head.next
        last = second.next
        while True:
            pre.next = second
            second.next = first
            first.next = last
            pre = first
            if last == None:
                return dummy.next
            first = last
            second = last.next
            if second == None:
                return dummy.next
            last = second.next
        

