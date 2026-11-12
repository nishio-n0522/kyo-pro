def dfs(area_map, start, H, W) -> bool:
    visited = [start]
    stack = [start]
    while stack:
        nx, ny = stack.pop(0)
        for cx, cy in [[nx, ny+1], [nx+1, ny], [nx, ny-1], [nx-1, ny]]:
            if 0 <= cx <= W-1 and 0 <= cy <= H-1 and area_map[cy][cx] == "#" and [cx, cy] not in visited:
                visited.append([cx, cy])
                stack.append([cx,cy])

    return len(visited)


def main():
    H, W = map(int, input().split())

    num_lake_area = 0
    area_map = [[None] * W for _ in range(H)]
    lake_cells = []
    for y in range(H):
        row = list(input())
        for x in range(W):
            area_map[y][x] = row[x]
            if row[x] == "#":
                lake_cells.append([x, y])
                num_lake_area += 1
    
    ans = 0
    for y in range(H):
        for x in range(W):
            if area_map[y][x] == ".":
                ans += 1
                continue

            area_map[y][x] = "."
            start = lake_cells[0] if [x, y] != lake_cells[0] else lake_cells[1]
            num = dfs(area_map, start, H, W)
            if num == num_lake_area - 1:
                ans += 1
            area_map[y][x] = "#"

    print(ans)

if __name__=='__main__':
    main()