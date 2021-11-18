from random import randint  # 64 bytes (function)
from sys import getsizeof  # 72 bytes (function)


lst = tuple([randint(-100, 100) for i in range(100)])  # 840 bytes (tuple)

max_neg = -100  # 28 bytes (int)
for num in lst:  # num - 28 bytes (int)
    if num >= 0:
        continue
    else:
        if num > max_neg:
            max_neg = num

print(f"Maximum negative number: {max_neg}.\nIndex of {max_neg}: {lst.index(max_neg)}")
print("-" * 100)
dir_lst = {k: v for k, v in locals().items() if not k.startswith("__")}
print(f"Size of al variables: {sum(map(getsizeof, dir_lst.values()))}")
for k, v in dir_lst.items():
    print(f"{k} : {getsizeof(v)}")

#  Python version: 3.9.5 x64
#  OS: Windows 10 Pro x64 build 18362.720
