class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if tree == []:
            return 0
        left = 0
        right = 1
        ans = 0
        aset = set()
        aset.add(tree[left])
        while right < len(tree):
            if tree[right] not in aset and len(aset) == 2:
                ans = max(ans,right - left)
                while left < right:
                    if len(set(tree[left:right])) == 2:
                        left += 1
                    else:
                        aset = set(tree[left:right+1])
                        break
            elif tree[right] not in aset and len(aset) < 2:
                aset.add(tree[right])
        
            right += 1
        if tree[right-1] in aset:
            ans = max(ans,right - left)
        return ans
            


