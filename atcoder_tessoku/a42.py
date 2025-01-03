def main():
    N, K = map(int, input().split())
    TK = [[0 for _ in range(101)] for _ in range(101)] 
    
    for _ in range(N):
        A, B = map(int, input().split())
        TK[A][B] += 1

    TK_RUISEKI = [[0] * 101 for _ in range(101)]
    for i in range(100):
        row_sum = 0
        for j in range(100):
            row_sum += TK[i+1][j+1]
            TK_RUISEKI[i+1][j+1] = TK_RUISEKI[i][j+1] + row_sum

    ans = 0
    for i in range(1, 100-K+1):
        for j in range(1, 100-K+1):
            max_player = TK_RUISEKI[i+K][j+K] - TK_RUISEKI[i-1][j+K] - TK_RUISEKI[i+K][j-1] + TK_RUISEKI[i-1][j-1]
            if max_player > ans:
                ans = max_player

    print(ans)

if __name__=='__main__':
    main()