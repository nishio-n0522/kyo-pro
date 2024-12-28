def convert_to_2(n: int):
    num_2 = ""
    i = 0
    while True:
        print(n // (2 ** i) % 2)
        i += 1
        if 2 ** i >= n:
            break
        # if n // (2 ** i) % 2 == 1:      # 10進数を2進数に変換する考えをうまく取り込んでいる  
            
    

print(convert_to_2(9))