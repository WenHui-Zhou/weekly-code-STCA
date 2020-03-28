# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        
        num = []
        while head:
            num.append(head.val)
            head = head.next
        num1 = num[::-1]
        for i in range(len(num)):
            if num[i] != num1[i]:
                return False
        return True
        """
        if head == None:
            return True
        nums = []
        while head != None:
            nums.append(head.val)
            head = head.next
        return nums == nums[::-1]
