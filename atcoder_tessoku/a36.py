def main():
    N, K = map(int, input().split())

    if K < 2 * (N-1):
        print("No")
    elif K == 2 * (N-1):
        print("Yes")
    else:
        check_num = K - 2 * (N-1)
        if check_num % 2 == 0:
            print("Yes")
        else:
            print("No")

if __name__=='__main__':
    main()