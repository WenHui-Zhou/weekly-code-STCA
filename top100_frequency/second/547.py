class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if M == [] or M[0] == []:
            return 0
        edge = []
        for i in range(len(M)):
            for j in range(len(M[0])):
                if i != j and M[i][j] == 1:
                    edge.append([i,j])
        def find_root(parent,x):
            x_root = x
            while parent[x_root] != -1:
                x_root = parent[x_root]
            return x_root
        def union_node(parent,x,y):
            x = find_root(parent,x)
            y = find_root(parent,y)
            if x == y:
    #            print('circle')
                pass
            else:
                parent[x] = y
        parent = [-1]*len(M)
        for e in edge:
            union_node(parent,e[0],e[1])
        ans = 0
        for val in parent:
            if val == -1:
                ans += 1
        return ans
