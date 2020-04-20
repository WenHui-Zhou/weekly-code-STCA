class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == '':
            return True
        flag = 0
        num = 0
        for idx,c in enumerate(word):
            if c.isupper():
                num += 1
                if idx == 0:
                    continue
                else:
                    if flag == 1:
                        return False
            else:
                flag = 1
        if flag == 1 and num >1:
            return False
        return True
