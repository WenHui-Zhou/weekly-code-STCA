import sys

memo  = {}

def dfs(K,N):
    if K == 1:
        return N
    if N == 0:
        return 0
    res = sys.maxsize
    for i in range(1,N+1):
        res = min(res,max( 
            dfs(K,N-i),
            dfs(K-1,i-1)
        )+1)
    memo[(K,N)] = res
    return res
print(dfs(2,10))

def dfs_speed(K,N):
    if K == 1:
        return N
    if N == 0:
        return 0
    res = sys.maxsize
    low = 1
    high = N
    while low <= high:
        mid = (low + high) // 2
        broken = dfs_speed(K-1,mid-1)
        not_broken = dfs(K,N-mid)
        if broken > not_broken:
            high = mid - 1
            res = min(res,broken+1)
        else:
            low = mid + 1
            res = min(res,not_broken+1)
    memo[(K,N)] = res
    return res
print(dfs_speed(2,10))
        

