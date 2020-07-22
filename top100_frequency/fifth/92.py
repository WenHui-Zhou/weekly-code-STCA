# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        
        if n == m:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        left = m - 1
        right = n + 1
        lside = dummy
        rside = dummy
        for i in range(left):
            lside = lside.next
        for i in range(right):
            rside = rside.next
        pre = lside.next
        cur = pre.next
        last = cur.next
        while last != rside:
            cur.next = pre
            pre = cur
            cur = last
            last = last.next
        cur.next = pre
        lside.next.next = rside
        lside.next = cur
        return dummy.next
        """
        if head == None:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        start = head
        for i in range(1,m):
            start = start.next
            pre = pre.next
        begin = pre
        last = start
        for i in range(m,n+1):
            last = last.next
        while start != last:
            tmp = start.next
            if begin == pre:
                start.next = last
            else:
                start.next = pre
            pre = start
            start = tmp
        begin.next = pre
        return dummy.next
