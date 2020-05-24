# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
      
        if head == None:
            return head
        dummy = ListNode('None')
        dummy.next = head
        length = 0
        cur = dummy
        while cur!= None:
            cur = cur.next
            length += 1
        if length /  2 == 0:
            mid = length // 2
        else:
            mid = length // 2 + 1
        l1 = head
        l2 = dummy
        for i in range(mid):
            l2 = l2.next
        temp = l2.next
        l2.next = None
        l2 = temp
        pre = l2
        cur = l2.next
        while cur != None:
            last = cur.next
            cur.next = pre
            pre = cur
            cur = last
        dummy = ListNode("None")
        temp = dummy
        while l1!=None and l2!=None:
            temp.next = l1
            temp = temp.next
            temp.next = l2
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        return dummy.next  """
        arr = []
        tmp = head
        while tmp:
            arr.append(tmp)
            tmp = tmp.next
            arr[-1].next = None
        left = 0
        right = len(arr)-1
        dummy = ListNode(-1)
        p = dummy
        while left <= right:
            p.next = arr[left]
            p = p.next
            left += 1
            if left > right:
                return dummy.next
            p.next = arr[right]
            right -= 1
            p = p.next
        return dummy.next
