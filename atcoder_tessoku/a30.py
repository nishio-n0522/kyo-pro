def main():
    waru = 1000000007

    n, r = map(int, input().split())

    bunshi = 1
    bunbo = 1

    for i in range(n, n-r, -1):
        bunshi = bunshi * i % waru
        bunbo = bunbo * (i-n+r) % waru

    i = 0
    M = waru - 2
    p = bunbo
    while True:
        if M // (2 ** i) % 2 == 1:
            bunshi = bunshi * p % waru
        if M <= 2 ** i:
            break
        p = p ** 2 % waru
        i += 1

    print(bunshi)

if __name__=='__main__':
    main()