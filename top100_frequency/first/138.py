"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        
        if head == None:
            return None
        pdict = {}
        tmp = head
        count = 1
        while tmp:
            pdict[tmp] = count
            tmp = tmp.next
            count += 1
        tmp = head
        dummy = Node(-1,None,None)
        ntmp = dummy
        while tmp:
            node = Node(tmp.val,None,None)
            ntmp.next = node
            ntmp = ntmp.next
            tmp = tmp.next
        tmp = head 
        cur = dummy.next
        while tmp:
            if tmp.random not in pdict:
                tmp = tmp.next
                cur = cur.next
                continue
            order = pdict[tmp.random]
            
            ntmp = dummy
            for i in range(order):
                ntmp = ntmp.next
            cur.random = ntmp
            cur = cur.next
            tmp = tmp.next
        return dummy.next
        
        pdict = {}
        dummy = Node(-1,None,None)
        if head == None:
            return None
        tmp = dummy
        index = 0
        cur = head
        NodeOrder = {}
        Listlen = 0
        while cur:
            NodeOrder[cur] = index
            index += 1
            cur = cur.next
            Listlen += 1
 #       Listlen += 1
        for index in range(Listlen):
            if head.random != None:
                pdict[index] = NodeOrder[head.random]
            tmp.next = Node(head.val,None,None)
            tmp = tmp.next
            head = head.next
        tmp = dummy.next
    #    print(pdict)
        for index in range(Listlen):
            cur = dummy.next
            if index in pdict:
                count = pdict[index]
                for _ in range(count):
                    cur = cur.next
                tmp.random = cur
            tmp = tmp.next
        return dummy.next
        """
        dummy = Node(-1)
        p = head
        cur = dummy
        if p == Node:
            return head
        pdict = {}
        index = 0
        while p!=None:
            node = Node(p.val)
            cur.next = node
            pdict[p] = index
            index += 1
            p = p.next
            cur = cur.next
        p = head
        order = []
        while p!=None:
            if p.random == None:
                order.append(-1)
            else:
                order.append(pdict[p.random])
            p = p.next
        cur = dummy
    #    print(order)
        for index in order:
            cur = cur.next
            if index == -1:
                continue
            tmp = dummy.next
            for t in range(index):
                tmp = tmp.next
            cur.random = tmp
        return dummy.next


            



