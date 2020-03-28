# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        
        if head == None:
            return head
        dummy = ListNode('None')
        dummy.next = head
        cur = dummy
        while cur.next !=None and cur.next.next != None:
            if cur.next.val != cur.next.next.val:
                cur = cur.next
            else:
                pose = cur.next.next
                while pose!= None and pose.val == cur.next.val:
                    pose = pose.next
                cur.next = pose
        return dummy.next"""
        if head == None:
            return None
        dummy = ListNode(-1)
        cur = dummy
        dummy.next = head
        while cur.next!=None and cur.next.next!=None:
            if cur.next.val != cur.next.next.val:
                cur = cur.next
            else:
                pose = cur.next.next
                while pose != None and pose.val == cur.next.val:
                    pose = pose.next
                cur.next = pose
        return dummy.next
