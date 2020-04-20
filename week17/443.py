class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        cur = 0
        count = 1
        for idx in range(1,len(chars)):
            c = chars[idx]
            if chars[idx-1] == chars[idx]:
                count += 1
            else:
                chars[cur] = chars[idx-1]
                cur += 1
                if count != 1:
                    for i in range(len(str(count))):
                        chars[cur] = str(count)[i]
                        cur += 1
                count = 1
        chars[cur] = chars[-1]
        cur += 1
        if count!=1:
            for i in range(len(str(count))):
                chars[cur] = str(count)[i]
                cur += 1
        #cur += 1
        return cur
