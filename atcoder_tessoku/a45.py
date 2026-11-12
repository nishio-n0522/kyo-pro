def main():
    N, C = input().split()
    A = list(input())

    score = 0
    for a in A:
        if a == "B":
            score += 1
        elif a == "R":
            score += 2

    result = score % 3

    if score % 3 == 0:
        result = "W"
    elif score % 3 == 1:
        result = "B"
    else:
        result = "R"

    if result == C:
        print("Yes")
    else:
        print("No")

if __name__=='__main__':
    main()