class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        
        if endWord not in wordList  or wordList==None:
            return 0
        
        word_combine = {}
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                cc = word[:i]+'_'+word[i+1:]
                if cc not in word_combine:
                    word_combine[cc] = [word]
                else:
                    word_combine[cc].append(word)

        queue = [(beginWord,1)]
        visits = {beginWord:True}
   #     print(word_combine)
        while queue:
            cur_word,level = queue.pop(0)
            for i in range(L):
                intermine = cur_word[:i] + '_' + cur_word[i+1:]
         #       print(intermine)
                if intermine not in word_combine:
                    continue
                for word in word_combine[intermine]:
                    if word == endWord:
                        return level + 1
                    if word not in visits:
                        visits[word] = True
                        queue.append((word,level+1))
                word_combine[intermine] = []
        return 0
"""

        if endWord not in wordList or wordList == []:
            return 0
        from collections import defaultdict
        word_combine = defaultdict(list)
        L = len(endWord)
        for word in wordList:
            for i in range(L):
                tmp = word[:i] + '_' + word[i+1:]
                word_combine[tmp].append(word)
        queue = [(beginWord,1)]
        visits = {beginWord:True}
        while queue:
            cur_word,level = queue.pop(0)
            for i in range(L):
                tmp = cur_word[:i] + '_' + cur_word[i+1:]
                if tmp not in word_combine:
                    continue
                for word in word_combine[tmp]:
                    if word == endWord:
                        return level + 1
                    if word not in visits:
                        visits[word] = True
                        queue.append((word,level+1))
                word_combine.pop(tmp)
        return 0


