def _judge_each_stack(n: int, X: int, Y: int) -> 1 | 2:
    dp = []
    min_num = min(X, Y)
    max_num = max(X, Y)

    for i in range(n+1):
        if i < min_num:
            dp.append(0)
        else:
            if dp[i-min_num] == 0 or dp[i-max_num] == 0:
                dp.append(1)
            else:
                dp.append(0)
    return dp

def _main():
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    
    max_a = max(A)
    dp = _judge_each_stack(max_a, X, Y)

    count = 0
    for a in A:
        count += dp[a]

    if count % 2 == 0:
        print("Second")
    else:
        print("First")


def _calc_grundy(n: int, x: int, y: int):
    grundy = []

    for i in range(n+1):
        Transit = [False, False, False]
        if i >= x:
            Transit[grundy[i-x]] = True
        if i >= y:
            Transit[grundy[i-y]] = True

        if Transit[0] == False:
            grundy.append(0)
        elif Transit[1] == False:
            grundy.append(1)
        else:
            grundy.append(2)

    return grundy

def min_int(num_list: list[int]):
    sorted_num_list = sorted(num_list)
    count = 0
    while True:
        if not count in sorted_num_list:
            return count
        count += 1

def calc_grundy(n: int, x: int, y: int):
    grundy = []
    for i in range(n + 1):
        if i < x:
            grundy.append(0)
        elif x <= i < y:
            grundy.append(min_int([grundy[i-x]]))
        else:
            grundy.append(min_int([grundy[i-x], grundy[i-y]]))

    return grundy

def main():
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    
    max_a = max(A)
    grundy_list = calc_grundy(max_a, X, Y)

    result = grundy_list[A[0]]
    for a in A[1:]:
        result ^= grundy_list[a]

    if result == 0:
        print("Second")
    else:
        print("First")

if __name__=='__main__':
    main()