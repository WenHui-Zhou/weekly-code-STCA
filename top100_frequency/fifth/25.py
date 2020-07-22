# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        
        def reverse(begin,end):
            tmp = None
            cur = begin
            while cur != end:
                last = cur.next
                cur.next = tmp
                tmp = cur
                cur = last
            end = begin
            begin = tmp
            return begin,end

        if head == None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre_begin = dummy
        begin = head
        end = head
        while end != None:
            for _ in range(k-1):
                end = end.next
                if end == None:
                    return dummy.next
            tmp = end.next
            begin,end = reverse(begin,tmp)
            end.next = tmp
            pre_begin.next = begin
            pre_begin = end
            begin = tmp
            end = tmp
        return dummy.next
        if head == None or k <= 1:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head
        while cur:
            for i in range(k-1):
                if cur == None:
                    return dummy.next
                cur = cur.next
            if cur == None:
                return dummy.next
            last = cur.next
            #翻转
            l1 = pre.next
            l2 = l1.next
            while l2!=cur:
                l3 = l2.next
                l2.next = l1
                l1 = l2
                l2 = l3
            pre.next.next = cur.next
            tmp = pre.next
            cur.next = l1
            pre.next = cur
            # 翻转
            pre = tmp
            cur = last
        return dummy.next"""
        if head == None or k <= 1:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head
        while cur:
            for i in range(k-1):
                if cur == None:
                    return dummy.next
                cur = cur.next
            if cur == None:
                return dummy.next
            last = cur.next
            l1 = pre.next
            l2 = l1.next
            while l2!=cur:
                l3 = l2.next
                l2.next = l1
                l1 = l2
                l2 = l3
            pre.next.next = cur.next
            tmp = pre.next
            cur.next = l1
            pre.next = cur
            pre = tmp
            cur = last
        return dummy.next








