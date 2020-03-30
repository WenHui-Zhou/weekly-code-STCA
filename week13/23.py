# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        
        if lists == []:
            return None
        dummy = ListNode(-1)
        tmp = dummy
        compare = []
        for node in lists:
            compare.append(node)
        while True:
            min_val = sys.maxsize
            pp = -1
            for idx,node in enumerate(compare):
                if node == None:
                    continue
                if node.val < min_val:
                    min_val = node.val
                    pp = idx
            if min_val == sys.maxsize:
                return dummy.next
            else:
                tmp.next = compare[pp]
                compare[pp] = compare[pp].next
                tmp = tmp.next
        """
        if lists == []:
            return None
        tmp = []
        for l in lists:
            if l == None:
                continue
            else:
                tmp.append(l)
        lists = tmp
        # heap
        def heapify(nums,n,i):
            c1 = 2*i + 1
            c2 = 2*i + 2
            root_index = i
            if c1 <= n and nums[c1].val < nums[root_index].val:
                root_index = c1
            if c2<=n and nums[c2].val < nums[root_index].val:
                root_index = c2
            if root_index != i:
                nums[root_index],nums[i] = nums[i],nums[root_index]
                heapify(nums,n,root_index)

        def create_heap(nums):
            n = len(lists) - 1
            last = (n-1) // 2
            for i in range(last+1)[::-1]:
                heapify(nums,n,i)
        create_heap(lists)
        dummy = ListNode(-1)
        cur = dummy
        while lists:
            cur.next = lists[0]
            cur = cur.next
            if lists[0].next == None:
                lists[0] = lists[-1]
                lists.pop(-1)
            else:
                lists[0] = lists[0].next
            heapify(lists,len(lists)-1,0)
        return dummy.next
