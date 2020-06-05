class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.split('-')
        S = ''.join(S)
        index = len(S) % K
        if index == 0:
            index = K
        res = S[:index].upper()
        S = S[index:]
        step = 0
        tmp = ''
        for i in range(len(S)):
            if step == K:
                res += '-' + tmp.upper()
                tmp = S[i]
                step = 1
            else:
                tmp += S[i]
                step += 1
        return res if tmp == '' else res + '-' + tmp.upper()
                

