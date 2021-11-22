from random import uniform


def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]
        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        c = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[c] = left[i]
                i += 1
            else:
                array[c] = right[j]
                j += 1
            c += 1

        while i < len(left):
            array[c] = left[i]
            i += 1
            c += 1

        while j < len(right):
            array[c] = right[j]
            j += 1
            c += 1


lst = [round(uniform(0, 49.99), 2) for i in range(100)]
print(f"Random list: {lst}")
merge_sort(lst)
print(f"Sorted list: {lst}")
print(lst == sorted(lst))
