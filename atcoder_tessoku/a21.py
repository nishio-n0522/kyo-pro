def main():
    N = int(input())
    P = [0] * (N + 2)
    A = [0] * (N + 2)

    for i in range(N):
        P[i+1], A[i+1] = map(int, input().split())
        
    dp = [[0]*(N+1) for _ in range(N+1)]

    for LEN in range(N-2, -1, -1):
        for l in range(1, N-LEN+1):
            r = l + LEN

            score_l = A[l-1] if l <= P[l-1] <= r else 0
            score_r = A[r+1] if l <= P[r+1] <= r else 0
            if l == 1:
                dp[l][r] = score_r + dp[l][r+1]
            elif r == N:
                dp[l][r] = score_l + dp[l-1][r]
            else:
                dp[l][r] = max(score_l + dp[l-1][r] , score_r + dp[l][r+1])

    ans = 0
    for i in range(N, 0, -1):
        ans = max(ans,dp[i][i])

    print(ans)

if __name__=="__main__":
    main()