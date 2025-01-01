def main():
    D, N = map(int, input().split())

    max_work_list = [24 for _ in range(D)]

    for _ in range(N):
        L, R, H = map(int, input().split())
        for j in range(L-1, R):
            max_work_list[j] = min(max_work_list[j], H)
            
    print(sum(max_work_list))


if __name__=='__main__':
    main()