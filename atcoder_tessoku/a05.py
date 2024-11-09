# N,K = map(int, input().split())

# answer = 0
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         k = K - i - j
#         if 1 <= k <= N:
#             answer += 1

# print(answer)

N, K = map(int, input().split())

count = 0
for red in range(1, N + 1):
    min_white = max(1, K - red - N)  # 最大青いボール数での白いボールの最小数
    if min_white > N:
        continue
    
    max_white = min(N, K - red - 1)  # 最小青いボール数での白いボールの最大数
    if max_white < min_white:
        continue
        
    count += max_white - min_white + 1  # 範囲をカウントする

print(count)