N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

DP = [0] * N

DP[1] = A[0]
for i in range(2, N):
    cost_a = DP[i-1] + A[i-1]
    cost_b = DP[i-2] + B[i-2]
    if cost_a < cost_b:
        DP[i] = cost_a
    else:
        DP[i] = cost_b

ans = []
place = N-1
while True:
    ans.append(place+1)
    if place == 0:
        break
    
    if DP[place-1] + A[place-1] == DP[place]:
        place = place - 1
    else:
        place = place - 2
ans.reverse()


print(len(ans))
print(str(ans)[1:-1].replace(",", " "))