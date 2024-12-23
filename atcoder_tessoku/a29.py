import math

def sub_calc(x: int, waru: int):
    result = x
    for _ in range(9):
        result *= x
        if result > waru:
            result = result % waru
    return result

def main():
    waru = 10**9 + 7

    a, b = map(int, input().split())

    result = a ** (b % 10)

    for i in range(int(math.log10(b))):
        if result > waru:
            result = result % waru

        a = sub_calc(a, waru)

        for _ in range(b // (10 ** (i+1)) % 10):
            if result > waru:
                result = result % waru
            result *= a

    print(result % waru)


if __name__=='__main__':
    main()
