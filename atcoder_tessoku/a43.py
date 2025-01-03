def main():
    N, L = map(int, input().split())

    max_time = 0
    for _ in range(N):
        A, B = input().split()
        pass_time = int(A) if B == "W" else L-int(A)
        if max_time < pass_time:
            max_time = pass_time
    
    print(max_time)

if __name__=='__main__':
    main()