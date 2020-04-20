class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bank = set(bank)
        if end not in bank:
            return -1
        dictionary = {"A":"CGT", "C":"AGT", "G":"ACT", "T":"ACG"}
        front = {start}
        bottom = {end}
        step = 0
        while front:
            step += 1
            next_front = set()
            for word in front:
                for i in range(len(word)):
                    for c in dictionary.get(word[i]):
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in bottom:
                            return step
                        if new_word in bank:
                            next_front.add(new_word)
                            bank.remove(new_word)
            front = next_front
            if len(bottom) < len(front):
                front,bottom = bottom,front

        return -1
