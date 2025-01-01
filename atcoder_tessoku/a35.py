def main():
    N = int(input())
    A = list(map(int, input().split()))

    dp = [[] for _ in range(N+1)]
    dp[N] = A
    
    for i in range(N-1, 0, -1):
        for j in range(i):
            if i % 2 == 1:
                dp[i].append(max(dp[i+1][j:j+2]))
            else:
                dp[i].append(min(dp[i+1][j:j+2]))

    print(dp[1][0])

if __name__=='__main__':
    main()