import bisect

N = int(input())
A = list(map(int, input().split()))

T = list(set(A))
T.sort()

B = [None] * N
for i in range(N):
    B[i] = bisect.bisect_right(T, A[i])

print(str(B)[1:-1].replace(",", " "))