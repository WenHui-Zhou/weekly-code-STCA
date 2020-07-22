# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        
        dummy = ListNode('None')
        temp = dummy
        while l1 and l2:
            if l1.val < l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
            temp.next = node
            temp = temp.next
        if l1 != None:
            temp.next = l1
        else:
            temp.next = l2
        return dummy.next
        
        dummy = ListNode(-1)
        tmp = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next 
            tmp = tmp.next
        if  l1:
            tmp.next = l1
        if l2:
            tmp.next = l2
        return dummy.next

        dummy = ListNode(-1)
        tmp = dummy
        while l1 and l2:
            if l1.val > l2.val:
                tmp.next = l2
                l2 = l2.next
            else:
                tmp.next = l1
                l1 = l1.next
            tmp = tmp.next
        if l1:
            tmp.next = l1
        else:
            tmp.next = l2
        return dummy.next"""
        dummy = ListNode(-1)
        pre = dummy
        while l1 and l2:
            if l1.val > l2.val:
                node = ListNode(l2.val)
                l2 = l2.next
            else:
                node = ListNode(l1.val)
                l1 = l1.next
            pre.next = node
            pre = pre.next
        if l1:
            pre.next = l1
        else:
            pre.next = l2
        return dummy.next
