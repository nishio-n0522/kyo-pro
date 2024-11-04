H, W = map(int, input().split())

cumulative_2d_sum = [[0] * (W+1) for _ in range(H+1)] 

for i in range(H):
    input_row = list(map(int, input().split()))
    row_sum = 0
    for j in range(W):
        row_sum += input_row[j]
        cumulative_2d_sum[i+1][j+1] = cumulative_2d_sum[i][j+1] + row_sum

Q = int(input())

for _ in range(Q):
    A,B,C,D = map(int,input().split())
    ans = cumulative_2d_sum[C][D] - cumulative_2d_sum[A-1][D] - cumulative_2d_sum[C][B-1] + cumulative_2d_sum[A-1][B-1]
    print(ans)