
def max_sum_path(grid):
    M = len(grid)
    N = len(grid[0])
    
    # DPテーブルを初期化
    dp = [[0] * N for _ in range(M)]
    
    # 1行目を初期化
    dp[0] = grid[0]
    
    # 2行目以降を計算
    for i in range(1, M):
        for j in range(N):
            # 上、左上、右上の中で最大値を選択
            max_prev = dp[i-1][j]
            if j > 0:
                max_prev = max(max_prev, dp[i-1][j-1])
            if j < N - 1:
                max_prev = max(max_prev, dp[i-1][j+1])
            
            dp[i][j] = grid[i][j] + max_prev

    
    # 最後の行の最大値を返す
    return max(dp[-1])

# テストケース
test_cases = [
    [
        [1, 1, 2, 1],
        [2, 1, 1, 2],
        [2, 7, 1, 2]
    ],
    [
        [5, 4, 3, 10],
        [1, 3, 0, 6],
        [9, 0, 3, 2],
        [3, 5, 1, 3]
    ]
]

for i, case in enumerate(test_cases, 1):
    result, kurikaeshi = max_sum_path(case)
    print(f"テストケース {i} の結果: {result}")
