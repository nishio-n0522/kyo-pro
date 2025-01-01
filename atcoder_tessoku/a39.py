MAX_TIME = 999999
import operator


def main():
    N = int(input())

    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort(key=lambda x: x[1])

    ans = 0
    last_time = 0
    for i in range(N):
        if last_time <= LR[i][0]:
            ans += 1
            last_time = LR[i][1]

    print(ans)

if __name__=='__main__':
    main()