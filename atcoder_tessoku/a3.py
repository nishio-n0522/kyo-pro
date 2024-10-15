N, K = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

result = "No"

for p in P:
    search_num = K - p
    for q in Q:
        if q == search_num:
            result = "Yes"
            break

print(result)