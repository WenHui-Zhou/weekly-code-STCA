# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        
        h1 = []
        while headA!= None:
            h1.append(headA)
            headA = headA.next
        h2 = []
        while headB != None:
            h2.append(headB)
            headB = headB.next
        h1 = h1[::-1]
        h2 = h2[::-1]
        node = None
        for i in range(min(len(h1),len(h2))):
            if h1[i] == h2[i]:
                node = h1[i]
            else:
                break
        return node
        """
        lenA = 0
        lenB = 0
        tmp = headA
        while tmp!=None:
            tmp = tmp.next
            lenA += 1
        tmp = headB
        while tmp != None:
            tmp = tmp.next
            lenB += 1
        while lenA > lenB:
            lenA -= 1
            headA = headA.next
        while lenB > lenA:
            lenB -= 1
            headB = headB.next
        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None


