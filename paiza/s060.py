def check_all_stars(pattern: str, start_index: int):
    for s in pattern[start_index:]:
        if s != "*":
            return False
    return True

def main():
    p1 = input()
    p2 = input()

    memo = {}

    def match_dfs(i: int, j: int) -> bool:
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == len(p1) and j == len(p2):
            memo[(i, j)] = True
            return True
        elif i < len(p1) and j == len(p2):
            memo[(i, j)] = check_all_stars(p1, i)
            return memo[(i, j)]
        elif i == len(p1) and j < len(p2):
            memo[(i, j)] = check_all_stars(p2, j)
            return memo[(i, j)]

        if p1[i] == "*" and p2[j] == "*":
            if match_dfs(i+1, j) or match_dfs(i, j+1) or match_dfs(i+1, j+1):
                memo[(i, j)] = True
                return True
        elif p1[i] == "*":
            if match_dfs(i+1, j) or match_dfs(i, j+1):
                memo[(i, j)] = True
                return True
        elif p2[j] == "*":
            if match_dfs(i, j+1) or match_dfs(i+1, j):
                memo[(i, j)] = True
                return True
        else:
            if p1[i] == p2[j] and match_dfs(i+1, j+1):
                memo[(i, j)] = True
                return True

        memo[(i, j)] = False
        return False

    if match_dfs(0, 0):
        print("Yes")
    else:
        print("No")

if __name__=='__main__':
    main()