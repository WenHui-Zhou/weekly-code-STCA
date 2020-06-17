class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        
        if len(tasks) <= 1:
            return len(tasks)
        
        task_map = {}
        for val in tasks:
            if val not in task_map:
                task_map[val] = 1
            else:
                task_map[val] += 1
        sort_map = sorted(task_map.items(),key=lambda x:-x[1])
        max_len = sort_map[0][1]
        min_len = (max_len-1)*(n+1)
        for val in sort_map:
            if val[1] == max_len:
                min_len += 1
            else:
                break
        return max(len(tasks),min_len)"""
        
        if len(tasks) <= 1:
            return len(tasks)
        from collections import Counter
        count = Counter(tasks)
        common = count.most_common()
        max_len = common[0][1]
        min_len = (max_len - 1)*(n+1)
        for item in common:
            if item[1] == max_len:
                min_len += 1
            else:
                break
        return max(len(tasks),min_len)
