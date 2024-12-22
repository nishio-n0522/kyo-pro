import random

def binary_search(L, search_num) -> int:
    if len(L) == 0:
        return 0
    
    l_index = 0
    r_index = len(L) - 1
    
    while True:
        if search_num <= L[l_index]:
            return l_index
        
        if L[r_index] <= search_num:
            return r_index + 1
        
        m_index = int((r_index + l_index) / 2)
        
        if L[m_index] == search_num:
            return m_index + 1
        elif L[m_index] < search_num:
            l_index = m_index + 1
        else:
            r_index = m_index - 1

L = [3 * i + 10 for i in range(5)]

for _ in range(10):
    num = random.randint(0, 20)
    index = binary_search(L, num)
    L.insert(index, num)
    print(num, L)

