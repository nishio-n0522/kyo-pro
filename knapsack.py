# a18

N,S = map(int,input().split())
A = [int(i) for i in input().split()]

x = 1<<S
print(x)
for a in A:
    x |= x>>a
    print(x)
    
print('Yes') if x&1 else print('No')