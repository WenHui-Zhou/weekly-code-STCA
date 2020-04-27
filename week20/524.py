class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort()
        d.sort(key=lambda x:-len(x))
        for word in d:
            cur = 0
            for ch in s:
                if ch == word[cur]:
                    cur += 1
                if cur == len(word):
                    return word
        return ''

