

s1 = 'abcdefgeeeeeeeeee'
s2 = 'abcdefgaeeeeeeee'

def get_longest_str(s1,s2):
    if len(s1) < len(s2):
        s1,s2 = s2,s1
    # s1 > s2
    max_len = 0
    max_start = 0
    dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            if dp[i][j] > max_len:
                max_len = dp[i][j]
                max_start = j - max_len
    return s2[max_start:max_start + max_len]

print(get_longest_str(s1,s2))



