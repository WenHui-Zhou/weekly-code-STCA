# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        nums = []
        tmp = head
        while tmp:
            nums.append(tmp.val)
            tmp = tmp.next
        # 冒泡
        def mp_sort(nums):
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i] > nums[j]:
                        nums[i],nums[j] = nums[j],nums[i]
        # 选择排序
        def select_sort(nums):
            for i in range(len(nums)):
                min_val = nums[i]
                pos = i
                for j in range(i+1,len(nums)):
                    if nums[j] < min_val:
                        pos = j
                        min_val = nums[j]
                if pos != i:
                    nums[i],nums[pos] = nums[pos],nums[i]

        # 归并排序
        def merge(a,b):
            temp = []
            lena = len(a)
            lenb = len(b)
            i,j = 0,0
            while i < lena and j < lenb:
                if a[i] < b[j]:
                    temp.append(a[i])
                    i += 1
                else:
                    temp.append(b[j])
                    j += 1
            while i<lena:
                temp.append(a[i])
                i += 1
            while j < lenb:
                temp.append(b[j])
                j += 1
            return temp

        def merge_sort(nums):
            if len(nums) < 2:
                return nums
            mid = len(nums) // 2
            a = nums[:mid]
            b = nums[mid:]
            return merge(merge_sort(a),merge_sort(b))
        # 快速排序
        def quick_sort(nums,left,right):
            if left >= right:
                return
            low = left
            hight = right
            pivot = nums[left]
            while left < right:
                while nums[right] > pivot and left < right:
                    right -= 1
                while nums[left] <= pivot and left < right:
                    left += 1
                nums[left],nums[right] = nums[right],nums[left]
            nums[low] = nums[right]
            nums[right] = pivot
            quick_sort(nums,low,right-1)
            quick_sort(nums,right+1,hight)
    #    mp_sort(nums)
    #    select_sort(nums)
    #    nums = merge_sort(nums)
        quick_sort(nums,0,len(nums)-1)
        new_head = ListNode(-1)
        aa = new_head
        for i in nums:
            tmp = ListNode(i)
            new_head.next = tmp
            new_head = new_head.next
        return aa.next
