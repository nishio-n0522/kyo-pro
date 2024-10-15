def input_formatter(input_line:str):
    return list(map(int, input_line.split(" ")))

M, N = input_formatter(input())

grid = [input_formatter(input()) for _ in range(M)]
dp = [[0] * N for _ in range(M)]

dp[0] = grid[0]

for i in range(1,M):
    for j in range(N):
        prev_max = dp[i-1][j]
        if j > 0:
            prev_max = max(prev_max, dp[i-1][j-1])
        if j < N-1:
            prev_max = max(prev_max, dp[i-1][j+1])
        dp[i][j] = grid[i][j] + prev_max

print(max(dp[-1]))