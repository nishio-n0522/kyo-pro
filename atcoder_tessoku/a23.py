# 2進数を10進数に変換する関数
def convert_2to10(num: list[int]):
    result = 0
    
    # num.reverse()
    for i, bit in enumerate(reversed(num)):
        result += bit * 2 ** i
    return result

def main():
    N, M = map(int, input().split())

    max_num = convert_2to10([1] * N)
    dp = [[10 ** 9 for _ in range(max_num+1)]] * (M+1)
    dp[0][0] = 0

    for i in range(1, M+1):
        c = list(map(int, input().split()))
        available_items = convert_2to10(c)
        for j in range(0, max_num+1):
            S = j | available_items
            dp[i][S] = min(dp[i-1][S], dp[i][j] + 1)

    if dp[-1][-1] > 100:
        print(-1)
    else:
        print(dp[-1][-1])
    

if __name__=='__main__':
    main()