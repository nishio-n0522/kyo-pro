def main():
    N, R = map(int, input().split())

    island_cells = []
    for i in range(N):
        island_cells.append(list(map(int, input().split())))

    ans = 0
    while island_cells:
        island_cells.sort()

        stack_cells = [island_cells.pop(0)]
        while True:
            base_cell = stack_cells.pop()
            for island_cell in island_cells:
                if (island_cell[0] - base_cell[0]) ** 2 + (island_cell[1] - base_cell[1]) ** 2 <= 4 * (R ** 2):
                    island_cells.remove(island_cell)
                    stack_cells.append(island_cell)
                else:
                    continue

            if len(stack_cells) == 0:
                ans += 1
                break

    print(ans)

if __name__=='__main__':
    main()