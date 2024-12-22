def main():
    H, W = map(int, input().split())
    board = []
    for _ in range(H):
        board.append(list(input()))

    dp = [[0 for _ in range(W)] for _ in range(H)]
    dp[0][0] = 1

    for i in range(H):
        for j in range(W):
            num_choice = 0
            if i == 0 or board[i-1][j] == "#":
                pass
            else:
                dp[i][j] += dp[i-1][j]
            
            if j == 0 or board[i][j-1] == "#":
                pass
            else:
                dp[i][j] += dp[i][j-1]

    print(dp[-1][-1])    


if __name__=='__main__':
    main()