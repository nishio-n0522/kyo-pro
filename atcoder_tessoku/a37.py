def main():
    N, M, B = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))

    sum_A = sum(A)
    sum_C = sum(C)

    print(sum_A * M + N * M * B + sum_C * N)

if __name__=='__main__':
    main()