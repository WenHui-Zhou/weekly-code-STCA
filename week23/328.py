# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        
        if head == None or head.next == None:
            return head
        jishu = head 
        oushu = head.next
        head2 = oushu
        while oushu:
            jishu.next = oushu.next
            if jishu.next == None:
                break
            jishu = jishu.next
            oushu.next = jishu.next
            oushu = oushu.next
        jishu.next = head2
        return head
        if head == None or head.next == None:
            return head
        ji = head
        ou = head.next
        cur = head.next.next
        head.next.next = None
        head.next = None
        temp = ji
        tempo = ou
        flag = 0
        while cur:
            if flag == 0:
                ji.next = cur
                ji = ji.next
            else:
                ou.next = cur
                ou = ou.next
            flag ^= 1
            last = cur.next
            cur.next = None 
            cur = last
        ji.next = tempo
        return temp"""
        if head == None:
            return None
        odd = ListNode(-1)
        even = ListNode(-1)
        po = odd
        pe = even
        p = head
        index = 0
        while p:
            if index % 2 == 0:
                pe.next = p
                pe = pe.next
            else:
                po.next = p
                po = po.next
            p = p.next
            index += 1
        pe.next = odd.next
        po.next = None
        return even.next
        
                











