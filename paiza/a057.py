def main():
    N = int(input())

    matrix = []
    check_lists = []
    for _ in range(N):
        row = [int(i) for i in input()]
        matrix.append(row)
        check_lists.append(row)

    # tate 
    for x in range(N):
        check_lists.append([])
        for y in range(N):
            check_lists[-1].append(matrix[y][x])

    # migi_naname
    for x in range(N):
        check_lists.append([])
        for i in range(N):
            if not (0 <= x+i < N and 0 <= i < N):
                break
            check_lists[-1].append(matrix[i][x+i])

    for y in range(N):
        check_lists.append([])
        for i in range(N):
            if not (0 <= y+i < N and 0 <= i < N):
                break
            check_lists[-1].append(matrix[y+i][i])

    # hidari_naname
    for x in range(N):
        check_lists.append([])
        for i in range(N):
            if not (0 <= x-i < N and 0 <= i < N):
                break
            check_lists[-1].append(matrix[i][x-i])

    for y in range(N):
        check_lists.append([])
        for i in range(N):
            if not (0 <= y+i < N and 0 <= N-1-i < N):
                break
            check_lists[-1].append(matrix[y+i][N-1-i])


    # max_length_check
    ans = 0
    for check_list in check_lists:
        continuity_num = 1
        current_num = check_list[0]
        found_set = set([current_num])

        for next_num in check_list[1:]:
            if current_num -1 == next_num or current_num + 1 == next_num and next_num not in found_set:
                continuity_num += 1
            else:
                continuity_num = 1
                found_set = set()

            current_num = next_num
            found_set.add(current_num)

            if continuity_num > ans:
                ans = continuity_num

    print(ans)

if __name__=='__main__':
    main()