# 输入两个整数 n 和 m，从数列1，2，3，.......，n 中随意取几个数,
# 使其和等于 m ,要求将其中所有的可能组合列出来。

# 用动态规划的思想来做，对节点，从右到左遍历

n = 10
m = 8

def getList(n,m,lists,ans):
    if m == 0:
        ans.append(lists[::])
        return
    if m < 0 or n <=0:
        return 
    getList(n-1,m,lists,ans)

    lists.append(n)
    getList(n-1,m-n,lists,ans)
    lists.pop()
ans = []
getList(n,m,[],ans)
print(ans)

