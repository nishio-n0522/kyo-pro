def main():
    N, x = map(int, input().split())
    
    dp = [[None] * x for _ in range(N+1)]
    dp[0][0] = 0
    
    for i in range(N):
        w, r = map(int, input().split())
        for prev_w, prev_r in enumerate(dp[i]):
            
            if prev_r is None:
                continue

            if dp[i+1][prev_w] is None:
                dp[i+1][prev_w] = prev_r
            else:
                dp[i+1][prev_w] = max(prev_r, dp[i+1][prev_w])


            if 0 <= prev_w + w < x:
                if dp[i][prev_w+w] is None:
                    dp[i+1][prev_w+w] = prev_r + r
                else:
                    dp[i+1][prev_w+w] = max(dp[i][prev_w+w], prev_r + r)
    
    
    ans = 0
    for row in dp:
        print(row)
        for num in row:
            if num is not None:
                ans = max(ans, num)

    print(ans)
    
if __name__ == '__main__':
    main()