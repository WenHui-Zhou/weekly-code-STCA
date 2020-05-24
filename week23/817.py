# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        lens = 0
        tmp = head
        while tmp != None:
            lens += 1
            tmp = tmp.next
        arr = [-1]*lens
        for index in G:
            if index >= lens:
                continue
            else:
                arr[index] = 1
        ans = 0
        res = 0
        tmp = head
        while tmp:
            if arr[tmp.val] == 1:
                res += 1
            else:
                if res != 0:
                    ans += 1
                res = 0
            tmp = tmp.next
        if res != 0:
            ans += 1
        return ans

            

