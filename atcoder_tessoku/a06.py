# dp_table = []

# N, Q = map(int, input().split())

# A_list = map(int, input().split())

# a_sum = 0
# for each_A in A_list:
#     a_sum += each_A
#     dp_table.append(a_sum)

# for _ in range(Q):
#     l, r = map(int, input().split())
#     prev_sum = dp_table[l-2] if l-2 >= 0 else 0
#     print(dp_table[r-1] - prev_sum)

# ==== dpテーブルサイズを規定、if文を削除 ====

N, Q = map(int, input().split())
dp_table = [0] * (N+1)

A_list = list(map(int, input().split()))

for i in range(N):
    dp_table[i+1] = dp_table[i] + A_list[i]

for _ in range(Q):
    l, r = map(int, input().split())
    print(dp_table[r] - dp_table[l-1])
