N, X = map(int, input().split())

A = list(map(int, input().split()))

start_index = 0
end_index = N-1
while True:
    index = int((end_index+start_index)/2)
    if A[index] == X:
        break
    elif A[index] < X:
        start_index = index + 1
    else:
        end_index = index - 1

print(index+1)