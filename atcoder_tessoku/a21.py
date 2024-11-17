# 入力
N = int(input())
P = [ None ] * (N + 1)
A = [ None ] * (N + 1)
for i in range(1, N+1):
	P[i], A[i] = map(int, input().split())

# 動的計画法（LEN は r-l の値)
dp = [ [ None ] * (N + 1) for i in range(N + 1) ]
dp[1][N] = 0
for LEN in reversed(range(0, N-1)):
	for l in range(1, N-LEN+1):
		print(LEN, l)