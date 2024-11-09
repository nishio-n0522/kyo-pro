N = int(input())

l = [0] * N
r = [0] * N

A = list(map(int, input().split()))

l[0] = A[0]
for i in range(1, N):
    l[i] = max(l[i-1], A[i])

r[N-1] = A[N-1]
for i in range(N-2, -1, -1):
    r[i] = max(r[i+1], A[i])

D = int(input())

for _ in range(D):
    L, R = map(int, input().split())
    print(max(l[L-2], r[R]))