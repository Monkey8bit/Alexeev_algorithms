from collections import deque
from collections import defaultdict
from itertools import zip_longest


def calc(a, b):
    result = ""
    rev_dict = {str(value): key for key, value in num_dict.items()}
    print(rev_dict)
    n1, n2 = list(a)[::-1], list(b)[::-1]
    print(n1, n2)
    rest = 0
    for i, n in zip_longest(n1, n2):
        temp_result = int(num_dict[i]) + int(num_dict[n]) + rest
        rest = 0
        print(rest, temp_result)
        if temp_result > 15:
            rest = 1
            temp_result -= 16
            print(rest, temp_result)
        result += rev_dict[str(temp_result)]
        print()
    return result[::-1]


num_str = "0123456789abcdef"
num_dict = defaultdict(int)
for k, v in enumerate(num_str):
    num_dict[v] = k

first_n = deque(input("Enter first number: "))
second_n = deque(input("Enter second number: "))

print(calc(first_n, second_n))
