class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        arr_d = {}
        val_i = {}
        for idx,d in enumerate(arr2):
            arr_d[d] = idx
            val_i[idx] = d
        inside = []
        other = []
        for val in arr1:
            if val in arr_d:
                inside.append(arr_d[val])
            else:
                other.append(val)
        inside.sort()
        for idx,val in enumerate(inside):
            inside[idx] = val_i[val]
        other.sort()
        return inside + other

