from random import randint


def min_max(array):
    max_ = 0
    min_ = len(array)

    for num in array:
        if num > max_:
            max_ = num
        if num < min_:
            min_ = num
    return min_, max_


if __name__ == "__main__":
    lst = [randint(1, 10000) for i in range(1, 1000)]
    min_n, max_n = min_max(lst)
    min_idx, max_idx = lst.index(min_n), lst.index(max_n)
    lst[min_idx], lst[max_idx] = lst[max_idx], lst[min_idx]
