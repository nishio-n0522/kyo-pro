def main():
    N = int(input())

    tumikis = []
    for _ in range(N):
        tumikis.append(list(map(int, input().split())))

    tumikis.sort(key=lambda x: x[1] + x[2], reverse=True)

    max_height = 0
    for i in range(2 ** N):
        height = 0
        last_size = [10 ** 9, 10 ** 9]
        for j, flag in enumerate(bin(i)[2:].zfill(N)):
            if not int(flag):
                continue
            
            if (tumikis[j][1] - last_size[0] <= 0 and tumikis[j][2] - last_size[1] <= 0) or \
                (tumikis[j][1] - last_size[1] <= 0 and tumikis[j][2] - last_size[0] <= 0):
                height += tumikis[j][0]
                last_size = [tumikis[j][1], tumikis[j][2]]

        max_height = max(height, max_height)

    print(max_height)


if __name__=='__main__':
    main()