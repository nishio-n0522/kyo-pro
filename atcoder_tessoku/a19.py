N, W = map(int, input().split())

dp = [0] * (W+1)
dp[0] = 0

for i in range(N):
    w, v = map(int, input().split())
    add_dp = ([0]*w + dp)[:W+1]
    for j in range(W, w-1, -1):
        if dp[j] < add_dp[j] + v:
            dp[j] = add_dp[j] + v

print(dp[-1])