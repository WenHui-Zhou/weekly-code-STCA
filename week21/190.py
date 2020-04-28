class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        '''
        ans,mask = 0,1
        for i in range(32):
            if n & mask:
                ans |= 1 <<(31 - i)
            mask <<= 1
        return ans'''

        ans,mask = 0,1
        for i in range(32):
            if n & mask:
                ans |= 1 << (31 - i)
            mask <<= 1
        return ans
