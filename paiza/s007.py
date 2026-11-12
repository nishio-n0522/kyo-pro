# import re

# pattern = re.compile("r\(|\)|\d+|[a-z]+")

# def nest(k, start_index, str_list):
#     temp_ans = {}

#     for i, s in enumerate(re.finditer(pattern, str_list[start_index:])):
#         if s.group().isdigit():
#             k = s.group()
#         elif s.group().isalpha():
#             for moji in s.group():
#                 temp_ans[moji] += k
#             k = 1
#         elif s.group(0) == "(":
#             nest(k, )
#         else:
#             return {key: value * k for key, value in temp_ans.items()} 


# def main():
#     str_list = input()
#     ans = {}
#     exist_moji = set()
#     process_queue = []
#     print(re.findall(pattern, "12345edrfghj(567gh6j7kj7k)"))

#     for i, s in enumerate(re.finditer(pattern, str_list)):
#         print(s.end())
#         if s.group().isdigit():
#             k = int(s.group())
#         elif s.group().isalpha():
#             for moji in s.group():
#                 if moji not in exist_moji:
#                     ans[moji] = k
#                 else:
#                     ans[moji] += k
#                 k = 1
#         elif s.group(0) == "(":
#             nest(k)
#             print("kakko start", s)
#         else:
#             print("kakko end", s)
    
#     for key, value in ans.items():
#         print(key, value)

# if __name__=='__main__':
#     main()

# ======== chat gpt ========

import re

pattern = re.compile(r"\(|\)|\d+|[a-z]")

def merge_dict(base_dict, add_dict):
    for k, v in add_dict.items():
        base_dict[k] = base_dict.get(k, 0) + v

def parse_expr(tokens, start_index=0, base_multiplier=1):
    char_counts = {}
    i = start_index
    current_multiplier = 1

    while i < len(tokens):
        token = tokens[i]

        if token.isdigit():
            current_multiplier = int(token)
            i += 1
        elif token.isalpha():
            char_counts[token] = char_counts.get(token, 0) + (current_multiplier * base_multiplier)
            current_multiplier = 1
            i += 1
        elif token == '(':
            sub_dict, new_i = parse_expr(tokens, i + 1, base_multiplier * current_multiplier)
            merge_dict(char_counts, sub_dict)
            i = new_i
            current_multiplier = 1
        elif token == ')':
            i += 1
            return char_counts, i
        
        else:
            i += 1
            break

    return char_counts, i

def main():
    str_list = input().strip()

    tokens = re.findall(pattern, str_list)

    ans_dict, _ = parse_expr(tokens, 0, 1)

    for ch in "abcdefghijklmnopqrstuvwxyz":
        print(ch, ans_dict.get(ch, 0))

if __name__ == '__main__':
    main()
