# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        
        op1 = []
        op2 = []
        while l1 != None:
            op1.append(l1.val)
            l1 = l1.next
        while l2 != None:
            op2.append(l2.val)
            l2 = l2.next
        step = 0
        head = ListNode('None')
        temp = head
        res = []
        for i in range(max(len(op1),len(op2))):
            val = 0
            if i < len(op1):
                val += op1[i]
            if i < len(op2):   
                val += op2[i]
            val += step
            step = 0
            if val >= 10:
                step = 1
                val -= 10
            res.append(val)
        
        if step != 0:
            res.append(1)
        for val in res:
            node = ListNode(val)
            temp.next = node
            temp = temp.next
        return head.next
        
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        dummy = ListNode(-1)
        tmp = dummy
        step = 0
        while l1 and l2:
            print(l1.val,l2.val)
            if l1.val + l2.val + step >= 10:
                val = l1.val + l2.val + step - 10
                step = 1
            else:
                val = l1.val + l2.val + step
                step = 0
            node = ListNode(val)
            tmp.next = node
            tmp = tmp.next
            l1 = l1.next
            l2 = l2.next
        l1 = l1 if l1 else l2
        while l1:
            if l1.val + step >= 10:
                step = 1
                val = 0
            else:
                val = step + l1.val
                step = 0
            node = ListNode(val)
            tmp.next = node
            l1 = l1.next
            tmp = tmp.next
        if step == 1:
            tmp.next = ListNode(1)
        return dummy.next
        """
        if l1 == None or l2 == None:
            return None
        val1 = ""
        val2 = ""
        while l1:
            val1 += str(l1.val)
            l1 = l1.next
        while l2:
            val2 += str(l2.val)
            l2 = l2.next
        res = int(val1[::-1]) + int(val2[::-1])
        dummy = ListNode(-1)
        t = dummy
        while res:
            node = ListNode(res%10)
            res = res // 10
            t.next = node
            t = t.next
        return dummy.next if dummy.next else ListNode(0)
