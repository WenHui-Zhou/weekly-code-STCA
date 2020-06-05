class Solution(object):
    def minMalwareSpread(self, graph, initial):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """
        parent = range(len(graph))
        sz = [1]*len(graph)
        def find_root(parent,x):
            x_root = x
            while parent[x_root] != x_root:
                x_root = parent[x_root]
            return x_root
        def union_node(parent,sz,x,y):
            x = find_root(parent,x)
            y = find_root(parent,y)
            parent[x] = y
            sz[y] += sz[x]
        for i,row in enumerate(graph):
            for j in range(i):
                if row[j]:
                    union_node(parent,sz,i,j)
        import collections
        count = collections.Counter(find_root(parent,u) for u in initial)
        ans = (-1, min(initial))
        for node in initial:
            root = find_root(parent,node)
            if count[root] == 1:  # unique color
                if sz[root] > ans[0]:
                    ans = sz[root], node
                elif sz[root] == ans[0] and node < ans[1]:
                    ans = sz[root], node

        return ans[1]
              


