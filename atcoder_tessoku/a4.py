# === my ans ===
# N = int(input())

# result = ""

# while N > 1:
#     if N % 2 == 0:
#         result = "0" + result
#     else:
#         result = "1" + result
#     N = N // 2

# if N == 1:
#     result = "1" + result

# if len(result) != 10:
#     result = "0" * (10 - len(result)) + result

# print(result)

# === answer ===
N = int(input())

# for x in range(9,-1,-1):
for x in [9,8,7,6,5,4,3,2,1,0]: # range()を使わないほうが実行時間が短い 12ms -> 9ms 
    wari = (2 ** x)
    print((N//wari)%2, end="")

print("")