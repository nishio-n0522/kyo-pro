# with open("./atcoder_tessoku-test_case/a18/04_subtask2_random01.txt", mode="r", encoding="utf-8") as file:
#     N, S = map(int, file.readline().split())
#     A = list(map(int, file.readline().split()))

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

# ==== なにこれ ====

N,S = map(int,input().split())
A = [int(i) for i in input().split()]

x = 1<<S
for a in A:
    x |= x>>a
    
print('Yes') if x&1 else print('No')