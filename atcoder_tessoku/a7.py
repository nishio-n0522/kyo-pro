D = int(input())
N = int(input())

dp = [0] * (D+2)
sum_dp = [0] * (D+2)

for _ in range(N):
    l, r = map(int, input().split())
    dp[l] += 1
    dp[r+1] -= 1

for i in range(D):
    sum_dp[i+1] = sum_dp[i] + dp[i+1]
    print(sum_dp[i+1])
