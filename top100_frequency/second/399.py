class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        from collections import defaultdict, deque
        graph = defaultdict(dict)
        vars = set()
        for item, val in zip(equations, values):
            x, y = item[0], item[1]
            vars.update(item)
            graph[x][y] = val
            graph[y][x] = 1 / val

        def bfs(s, e):
            queue = deque([[s, 1.0]])
            visited = set([s])
            while queue:
                tmp, val = queue.pop()
                if tmp == e:
                    return val
                for nxt in graph[tmp]:
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.appendleft([nxt, val * graph[tmp][nxt]])
            return -1.0

        return [bfs(*q) if q[0] in vars and q[1] in vars else -1.0 for q in queries]
