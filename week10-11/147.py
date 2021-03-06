# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
       
        if head == None:
            return None
        dummy = ListNode(-sys.maxsize)
        dummy.next = head
        end = head.next
        cur = head.next
        pre_cur = head
        # charu
        while end != None:
            end = cur.next
            pre_cur.next = cur.next
            tmp = dummy
            while tmp.next != end:
                if tmp.next.val >= cur.val:
                    tt = tmp.next
                    tmp.next = cur
                    cur.next = tt
                    break
                tmp = tmp.next
            if tmp.next == end:
                tmp.next = cur
                cur.next = end
            while pre_cur.next!=end:
                pre_cur = pre_cur.next
            cur = end

        return dummy.next
         """

        if head == None:
            return head
        dummy = ListNode(-sys.maxsize)
        dummy.next = head
        cur = head
        while cur.next:
    #        print(cur.val)
            tmp = cur.next
            cur.next = tmp.next
            pre = dummy
            while pre != cur:
                if pre.next.val >= tmp.val:
                    tt = pre.next
                    pre.next = tmp
                    tmp.next = tt
                    break
                else:
                    pre = pre.next
            if pre == cur:
                cur.next = tmp
                cur = cur.next
        return dummy.next

