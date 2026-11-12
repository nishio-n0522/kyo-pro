def main():
    M, N = map(int, input().split())

    area_map = [[0] * M for _ in range(N)]
    result_map = [[10 ** 9] * M for _ in range(N)]
    start_index = None
    goal_index = None

    for y in range(N):
        row_input = input().split()
        for x in range(M):
            area_map[y][x] = row_input[x]
            if row_input[x] == "s":
                start_index = [x, y]
            if row_input[x] == "g":
                goal_index = [x, y]

    stack = [start_index]
    visited = []
    result_map[start_index[1]][start_index[0]] = 0

    i = 0
    while stack:
        cx, cy = stack.pop(0)
        for nx, ny in [[cx+1,cy], [cx,cy+1], [cx-1,cy], [cx, cy-1]]:
            if 0 <= nx < M and 0 <= ny < N and area_map[ny][nx] in ["0", "g"] and [nx, ny] not in visited:
                result_map[ny][nx] = min(result_map[ny][nx], result_map[cy][cx]+1)
                visited.append([nx,ny])
                stack.append([nx,ny])

                if area_map[ny][nx] == "g":
                    flag = True
                    for mx, my in [[nx+1, ny], [nx, ny+1], [nx-1, ny],[nx, ny-1]]:
                        if 0 <= mx < M and 0 <= my < N and area_map[my][mx] == "0" and result_map[my][mx] == 10 ** 9:
                            flag = False

                    if flag:
                        break

    if result_map[goal_index[1]][goal_index[0]] == 10**9:
        print("Fail")
    else:
        print(result_map[goal_index[1]][goal_index[0]])

if __name__ == '__main__':
    main()