from random import randint
# from statistics import median


def find_median(array):
    max_num = max(array)
    size = max_num + 1
    count_lst = [0] * size
    middle = len(array) // 2

    for i in array:
        count_lst[i] += 1

    for j in range(1, size):
        count_lst[j] += count_lst[j - 1]

    res = [0] * len(array)
    n = len(array) - 1
    while n >= 0:
        temp_num = array[n]
        count_lst[temp_num] -= 1
        temp_pos = count_lst[temp_num]
        res[temp_pos] = temp_num
        n -= 1

    median = res[middle]
    print(f"Median number is: {median}")


odd_lst = [randint(1, 10) for i in range(11)]
print(odd_lst, sorted(odd_lst))
find_median(odd_lst)
