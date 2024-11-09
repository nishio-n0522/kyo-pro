# test = open("../atcoder_tessoku-test_case/a9/test01.txt", mode="r", encoding="utf-8")
# H, W, N = map(int, test.readline().split())

# H, W, N = map(int, input().split())

# comulative_2d = [[0]*(W+2) for _ in range(H+2)]

# for _ in range(N):
#     # A, B, C, D = map(int, test.readline().split())
#     A, B, C, D = map(int, input().split())
#     comulative_2d[A][B] += 1
#     comulative_2d[C+1][B] -= 1
#     comulative_2d[A][D+1] -= 1
#     comulative_2d[C+1][D+1] += 1

# # test.close()

# for i in range(H):
#     for j in range(W):
#         comulative_2d[i+1][j+1] = comulative_2d[i+1][j] + comulative_2d[i+1][j+1]

# for j in range(W):
#     for i in range(H):
#         comulative_2d[i+1][j+1] = comulative_2d[i][j+1] + comulative_2d[i+1][j+1]

# for i in range(H):
#     print(str(comulative_2d[i+1][1:-1])[1:-1].replace(",", " "))


# ========= with itertools =========

import itertools

H, W, N = map(int, input().split())

comulative_2d = [[0]*(W+2) for _ in range(H+2)]

for _ in range(N):
    A, B, C, D = map(int, input().split())
    comulative_2d[A][B] += 1
    comulative_2d[C+1][B] -= 1
    comulative_2d[A][D+1] -= 1
    comulative_2d[C+1][D+1] += 1

for i in range(H):
    comulative_2d[i+1] = list(itertools.accumulate(comulative_2d[i+1]))

for j in range(W):
    for i in range(H):
        comulative_2d[i+1][j+1] = comulative_2d[i][j+1] + comulative_2d[i+1][j+1]

for i in range(H):
    print(str(comulative_2d[i+1][1:-1])[1:-1].replace(",", " "))