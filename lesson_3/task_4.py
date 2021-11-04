from random import randint


lst = [randint(1, 1000) for i in range(1000)]
num_count = {}
num_count.setdefault("max_num", 0)
num_count.setdefault("max_count", 0)

for num in lst:
    if num_count.get(num):
        num_count[num] += 1
    else:
        num_count.setdefault(num, 1)
    if num_count[num] > num_count["max_count"]:
        num_count["max_count"] = num_count[num]
        num_count["max_num"] = num

print(f"Number with the most occurrences: {num_count['max_num']}\nAmount of occurrences: {num_count['max_count']}.")
