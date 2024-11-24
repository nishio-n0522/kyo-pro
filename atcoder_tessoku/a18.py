# import sys

# N, S = map(int, input().split())
# A = list(map(int, input().split()))

# A.sort()

# DP = [[] for _ in range(N+1)]
# DP[0].append(0)

# for i in range(N):
#     for j in range(len(DP[i])):
#         new_value = DP[i][j] + A[i]
#         if new_value == S:
#             print("Yes")
#             sys.exit()
#         elif new_value > S:
#             break
#         DP[i+1].append(new_value)
#         DP[i+1].append(DP[i][j])
#     DP[i+1].sort()

# print("No")

# ==== ビットDPによる解法 ====

N,S = map(int,input().split())
A = [int(i) for i in input().split()]

x = 1<<S
print(x)
for a in A:
    x |= x>>a
    print(x)
    
print('Yes') if x&1 else print('No')