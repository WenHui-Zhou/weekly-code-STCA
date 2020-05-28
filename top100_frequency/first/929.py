class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = set()
        for email in emails:
            pre,last = email.split('@')
            if '+' in pre:
                pre = pre[0:pre.index('+')]
            if '.' in pre:
                pre = ''.join(pre.split('.'))
            res.add(pre + '@' + last)
        print(res)
        return len(res)


