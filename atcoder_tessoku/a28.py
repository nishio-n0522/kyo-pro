def main():
    N = int(input())

    result = 0
    for i in range(N):
        T, A = input().split()
        A = int(A)

        if result < 0:
            result += 10000

        if T == "+":
            result += A
        elif T == "-":
            result -= A
        elif T == "*":
            result *= A

        result = result % 10000
        print(result)

if __name__=='__main__':
    main()