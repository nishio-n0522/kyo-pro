def main():
    N, Q = map(int, input().split())
    A = [i for i in range(N+1)]

    inverse = 1
    for _ in range(Q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            A[inverse * query[1]] = query[2]
        elif query[0] == 2:
            inverse *= -1
        else:
            print(A[inverse * query[1]])

if __name__=='__main__':
    main()