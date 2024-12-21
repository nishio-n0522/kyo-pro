def main():
    N = int(input())

    A = list(map(int, input().split()))

    dp = [0] * (N+1)
    L = [None] * (N+1)
    
    dp[1] = 1
    L[1] = A[0]

    for i in range(1, N):
        

        L[i] = A[i]

    print(max(dp))

if __name__=='__main__':
    main()