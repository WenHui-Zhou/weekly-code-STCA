class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        arr = defaultdict(int)
        for address in cpdomains:
            time,add = address.split(' ')
            arr[add] += int(time)
            while add:
                if '.' not in add:
                    break
                else:
                    add = add[add.index('.')+1:]
                    arr[add] += int(time)
        res = []
        for key,val in arr.items():
            tmp = str(val) + ' ' + key
            res.append(tmp)
        return res
