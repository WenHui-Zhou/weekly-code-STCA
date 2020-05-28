class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        if nums == []:
            return []
        def quick_sort(nums,left,right):
            if left > right:
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
            quick_sort(nums,low,right - 1)
            quick_sort(nums,right + 1,hight)
        quick_sort(nums,0,len(nums) - 1)
        return  nums

        if nums == []:
            return []
        
        def quick_sort(nums,left,right,k):
            if left > right:
                return 
            low = left
            high = right
            pivot = nums[low]
            while left < right:
                while nums[right] > pivot and left < right:
                    right -= 1
                while nums[left] <= pivot and left < right:
                    left += 1
                nums[left],nums[right] = nums[right],nums[left]
            nums[low] = nums[right]
            nums[right] = pivot
            if right == k-1:
                return 
            elif k-1 < right:
                quick_sort(nums,low,right - 1,k)
            else:
                quick_sort(nums,right + 1,high,k)
        quick_sort(nums,0,len(nums) - 1,6)
        return nums
        def heapify(nums,n,root):
            c1 = root*2 + 1
            c2 = root*2 + 2
            max_index = root
            if c1<=n and nums[c1] > nums[max_index]:
                max_index = c1
            if c2<=n and nums[c2] > nums[max_index]:
                max_index = c2
            if max_index != root:
                nums[max_index],nums[root] = nums[root],nums[max_index]
                heapify(nums,n,max_index)
        def create_heap(nums):
            n = len(nums) - 1
            last_root = (n - 1) // 2
            for i in range(last_root + 1)[::-1]:
                heapify(nums,n,i)
        def Asort(nums):
            create_heap(nums)
            for i in range(len(nums))[::-1]:
                nums[0],nums[i] = nums[i],nums[0]
                heapify(nums,i-1,0)
        Asort(nums)
        return nums"""
        def heapify(nums,n,root):
            c1 = root*2 + 1
            c2 = root*2 + 2
            max_index = root
            if c1 <= n and nums[c1] > nums[max_index]:
                max_index = c1
            if c2 <= n and nums[c2] > nums[max_index]:
                max_index = c2
            if max_index != root:
                nums[max_index],nums[root] = nums[root],nums[max_index]
                heapify(nums,n,max_index)
        def create_heap(nums):
            n = len(nums) - 1
            last_index = (n-1) // 2
            for i in range(last_index+1)[::-1]:
                heapify(nums,n,i)
        def Asort(nums):
            create_heap(nums)
            for i in range(len(nums))[::-1]:
                nums[0],nums[i] = nums[i],nums[0]
                heapify(nums,i-1,0)
        Asort(nums)
        return nums




