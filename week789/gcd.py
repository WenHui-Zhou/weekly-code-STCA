
N = 5
nums = [3,6,2,2,2]

def cal_gcd(a,b):
    while(a%b!=0):
        m=a%b
        a=b
        b=m
    return b

arr = [[0]* len(nums) for _ in range(len(nums))]

for i in range(N):
    arr[i][i] = nums[i]
for i in range(N):
    for j in range(i+1,N):
        arr[i][j] = cal_gcd(arr[i][j-1],nums[j])
    for j in range(i+1,N):
        arr[i][j] *= (j-i+1)
res = max(nums)
print(arr)
for num in arr:
    if res < max(num):
        res = max(num)
print(res)
