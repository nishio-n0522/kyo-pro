def main():
    N = int(input())
    S = list(input())

    last_color = S[0]
    cnt = 1

    ans = "No"
    for s in S[1:]:
        if s != last_color:
            cnt = 1
        else:
            cnt += 1

        if cnt >= 3:
            ans = "Yes"
            break

        last_color = s

    print(ans)

if __name__=='__main__':
    main()