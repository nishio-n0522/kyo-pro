import math

def main():
    N = int(input())
    A = list(map(int, input().split()))

    a_counts = [0] * (101)
    for a in A:
        a_counts[a] += 1
    
    ans = 0
    for count in a_counts:
        if count < 3:
            continue
        ans += math.comb(count, 3)

    print(ans)


if __name__=='__main__':
    main()