from random import randint


def desc_bubble_upgrade(array):
    print(array)
    counter = 0
    for i in range(len(array) - 1, 0, -1):
        swap_case = False
        for j in range(i, -1, -1):
            counter += 1
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                swap_case = True
        if not swap_case:
            break
    print(array)
    print(array == sorted(array, reverse=True))
    print(f"Amount of comparisons for {desc_bubble_upgrade.__name__}: {counter}")


def bubble_sort(array):
    n = 1
    counter = 0
    while n < len(array):
        for i in range(len(array) - 1):
            counter += 1
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1

    print(f"Amount of comparisons for {bubble_sort.__name__}: {counter}")
    print(sorted(array) == array)


lst = [randint(-100, 99) for i in range(100)]
desc_bubble_upgrade(lst)
bubble_sort(lst)
