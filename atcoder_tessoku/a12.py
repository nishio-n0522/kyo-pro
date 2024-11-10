def calc_print(t, A):
    return sum([t//a for a in A])

N, K = map(int, input().split())
A = list(map(int, input().split()))

# with open("./atcoder_tessoku-test_case/a12/10_random_small_02.txt", mode="r", encoding="utf-8") as file:
#     N,K = map(int, file.readline().split())
#     A = list(map(int, file.readline().split()))

min_value = min(A)
start_index = 0
end_index = K * min_value
index =  (start_index + end_index) // 2

while True:
    index =  (start_index + end_index) // 2
    num = calc_print(index, A)
    next_num = calc_print(index+1, A)
    if num < K <= next_num:
        break
    elif num < K:
        start_index = index + 1
    else:
        end_index = index - 1

print(index+1)
