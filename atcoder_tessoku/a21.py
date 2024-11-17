# 入力
N = int(input())
P = [ None ] * (N + 1)
A = [ None ] * (N + 1)

for i in range(N):
    P[i+1], A[i+1] = map(int, input().split())
    
dp = [[0]*(N+1) for _ in range(N+1)]

for LEN in range(N-2, -1, -1):
    for i in range(1, N-LEN+1):
        print(LEN, i)