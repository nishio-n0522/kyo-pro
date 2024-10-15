def get_input():  
    return map(int, input().split())

N, X = get_input()
int_list = list(get_input())

if X in int_list:
    print("Yes")
else:
    print("No")