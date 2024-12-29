def main():
    N = int(input())
    A = list(map(int, input().split()))    

    result = A[0]
    for a in A[1:]:
        result ^= a
    
    if result == 0:
        print("Second")
    else:
        print("First")

if __name__=='__main__':
    main()