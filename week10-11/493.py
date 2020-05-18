class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def merge(nums,left,mid,right):
            res = []
            start = left
            end = mid + 1
            while start <=mid and end <= right:
                if nums[start] > nums[end]:
                    res.append(nums[end])
                    end += 1
                else:
                    res.append(nums[start])
                    start += 1
            while start <= mid:
                res.append(nums[start])
                start += 1
            while end <= right:
                res.append(nums[end])
                end += 1
            for idx,i in enumerate(range(left,right + 1)):
                nums[i] = res[idx]

        def merge_and_sort(nums,left,right):
            if left >= right:
                return 0
            mid = (left + right) // 2
            count = merge_and_sort(nums,left,mid) + merge_and_sort(nums,mid + 1,right)
            j = mid + 1
            for i in range(left,mid+1):
                while j <= right and nums[i] > nums[j]*2:
                    j += 1
                count += j - (mid + 1)
        #    return count
            merge(nums,left,mid,right)
            return count
        return merge_and_sort(nums,0,len(nums) - 1)
