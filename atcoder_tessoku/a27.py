import math

def _main():
    A, B = map(int, input().split())

    small_num = min(A, B)
    large_num = max(A, B)

    num_max = math.sqrt(small_num)

    large_list = []
    small_list = []

    for i in range(1, math.floor(num_max)+1):
        if small_num % i == 0:
            small_list.append(i)
            large_list.append(small_num//i)

    small_list.reverse()
    
    for i in large_list + small_list:
        if large_num % i == 0:
            print(i)
            break

# using Euclidean mutual division
def main():
    A, B = map(int, input().split())

    small_num = min(A, B)
    large_num = max(A, B)

    while small_num > 0:
        amari = large_num % small_num        
        large_num = small_num
        small_num = amari
    
    print(large_num)

if __name__=='__main__':
    main()