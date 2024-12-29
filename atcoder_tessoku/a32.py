def main():
    N, A, B = map(int, input().split())

    min_num = min(A, B)
    max_num = max(A, B)

    dp = [None] * (N + 1)

    for i in range(N+1):
        if i < min_num:
            dp[i] = 0
            continue
        if dp[i - min_num] == 0 or dp[i-max_num] == 0:
            dp[i] = 1
        else:
            dp[i] = 0

    if dp[N] == 1:
        print("First")
    else:
        print("Second")

if __name__=='__main__':
    main()