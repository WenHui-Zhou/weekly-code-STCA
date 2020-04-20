class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        right = len(s) - 1
        s = [c for c in s]
        res = ['a','e','i','o','u']
        while left < right:
    #        print(left,right,s)
            while left < right:
                if str(s[left]).lower() in res:
                    break
                else:
                    left += 1
            while left < right:
                if str(s[right]).lower() in res:
                    break
                else:
                    right -= 1
            if left < right:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1
        return ''.join(s)

