import math

def check_prime_number(x: int):
    if x == 2 or x == 3:
        return True
    
    if x % 2 == 0 or x % 3 == 0:
        return False
    
    max_num = math.sqrt(x)

    num_small = 5
    num_large = 7
    while num_small <= max_num:
        if x % num_small == 0 or x % num_large == 0:
            return False
        num_small += 6
        num_large += 6
    return True

def main():
    Q = int(input())

    for _ in range(Q):
        X = int(input())
        
        if check_prime_number(X):
            print("Yes")
        else:
            print("No")

if __name__=='__main__':
    main()
