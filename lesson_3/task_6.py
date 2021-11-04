from random import randint
from task_3 import min_max


lst = {randint(1, 1000) for i in range(1, 100)}  # i used set for remove duplicates
lst = list(lst)
min_, max_ = min_max(lst)
START = lst.index(min_) + 1
STOP = lst.index(max_)

result = 0
for num in lst[START:STOP]:
    result += num

print(f"Sum of elements between min and max numbers in list: {result}")
