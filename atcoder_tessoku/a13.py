# def search_index(start_index, end_index, search_num, A, N):
#     while True:
#         index = (start_index + end_index) // 2
#         if A[index] <= search_num < A[index+1]:
#             return index
#         elif search_num < A[index]:
#             end_index = index - 1
#         elif A[N-1] < search_num:
#             return N-1
#         else:
#             start_index = index + 1

# N, K = map(int, input().split())
# A = list(map(int, input().split()))

# sum_value = 0
# for i in range(N - 1):
#     start_index = i
#     end_index = min(start_index + K, N-2)
#     sum_value += search_index(start_index, end_index, A[i] + K, A, N) - i

# print(sum_value)

# ===== しゃくとり法 =====

N, K = map(int, input().split())
A = list(map(int, input().split()))

R = [None] * N

for i in range(N):
    R[i] = 0 if i == 0 else R[i-1]

    while R[i] < N-1 and A[R[i]+1] - A[i] <= K:
        R[i] += 1

ans = 0
for i in range(N-1):
    ans += R[i] - i

print(ans)
