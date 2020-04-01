class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        
        import sys
        tmp = nums1[:m]
        tmp.append(sys.maxsize)
        cur1 = 0
        cur2 = 0
        cur = 0
        while cur < m + n:
            if cur2 < n and nums2[cur2] < tmp[cur1]:
                nums1[cur] = nums2[cur2]
                cur2 += 1
            else:
                nums1[cur] = tmp[cur1]
                cur1 += 1
            cur += 1
        return nums1
        
        cur = 0
        tmp = nums1[:m]
        import sys
        tmp.append(sys.maxsize)
        cur1 = 0
        cur2 = 0
        for i in range(m+n):
            if cur2 < n and tmp[cur1] > nums2[cur2]:
                nums1[cur] = nums2[cur2]
                cur2 += 1
            else:
                nums1[cur] = tmp[cur1]
                cur1 += 1
            cur+= 1
        return nums1
        """
        if nums1 == []:
            return []
        for i in range(n):
            nums1[m+i] = nums2[i]
        def quick_sort(nums,left,right):
            if left >= right:
                return
            low = left
            hight = right
            pivot = nums[left]
            while left < right:
                while pivot < nums[right] and left < right:
                    right -= 1
                while nums[left] <= pivot and left < right:
                    left += 1
                nums[left],nums[right] = nums[right],nums[left]
            nums[low] = nums[right]
            nums[right] = pivot
            quick_sort(nums,low,right - 1)
            quick_sort(nums,right+1,hight)
    
    #    quick_sort(nums1,0,len(nums1)-1)
        
        def heapify(nums,n,i):
            c1 = 2*i + 1
            c2 = 2*i + 2
            max_index = i
            if c1 <= n and nums[c1] > nums[max_index]:
                max_index = c1
            if c2 <= n and nums[c2] > nums[max_index]:
                max_index = c2
            if max_index != i:
                nums[max_index],nums[i] = nums[i],nums[max_index]
                heapify(nums,n,max_index)
        def create_heap(nums):
            n = len(nums) - 1
            last = (n - 1) // 2
            for index in range(last+1)[::-1]:
                heapify(nums,n,index)
        def sort_arr(nums):
            create_heap(nums)
            for i in range(len(nums))[::-1]:
                nums[0],nums[i] = nums[i],nums[0]
                heapify(nums,i-1,0)
        sort_arr(nums1)
        return nums1

