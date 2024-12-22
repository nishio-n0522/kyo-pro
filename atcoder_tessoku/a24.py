import bisect

def main():
    N = int(input())

    A = list(map(int, input().split()))

    LEN = 0
    L = []

    for a in A:
        pos = bisect.bisect_left(L, a)
        if pos >= LEN:
            L.append(a)
            LEN += 1
        else:
            L[pos] = a


    print(LEN)

if __name__=='__main__':
    main()