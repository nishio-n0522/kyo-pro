S = input()
T = input()

len_s = len(S)
len_t = len(T)

dp = [[0]*(len_s+1) for _ in range(len_t+1)]

max_len = 0
for i in range(len_t):
    for j in range(len_s):
        if T[i] == S[j]:
            dp[i+1][j+1] = dp[i][j]+1
            if dp[i][j]+1 > max_len:
                max_len = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

print(max_len)