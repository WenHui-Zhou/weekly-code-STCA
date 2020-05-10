import sys
# 输入
T = int(sys.stdin.readline().strip())
arr = []
while True:
    line = sys.stdin.readline().strip()
    l = list(map(int,line.split(' ')))
    arr.append(l[1:])

#arr = [
#    [1,1,1,1],
#    [1,1,1,1,2],
#    [1,1,1,1,2,2,4,4]
#]

def is_box(nums):
    if len(nums) < 4 or sum(nums) % 4 != 0:
        return False

    nums.sort(reverse=True)
    edges = [0] * 4

    def dfs(i,nums,edges,div):
        if i == len(nums):
            if len(set(edges)) == 1:
                return True
            return False
        for k in range(4):
            if edges[k] + nums[i] > div: continue
            edges[k] += nums[i]
            if dfs(i + 1,nums,edges,div): return True
            edges[k] -= nums[i]
        return False
    return dfs(0,nums,edges,sum(nums) // 4)

for nums in arr:
    if is_box(nums):
        print('YES')
    else:
        print('NO')
        
