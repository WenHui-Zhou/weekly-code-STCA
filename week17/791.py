class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        if S == '' or T == '':
            return T
        order = {}
        for idx,c in enumerate(S):
            order[c] = idx
        seq = []
        n = len(S)
        for c in T:
            if c not in S:
                seq.append([c,n])
            else:
                seq.append([c,order[c]])
        seq = sorted(seq,key = lambda x:x[1])
    #    print(seq)
        ans = ''
        for it in seq:
            ans += it[0]
        return ans
