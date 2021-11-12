import cProfile
from timeit import timeit
from random import randint
from collections import Counter


def rnd_lst_gen(n):
    return [randint(1, 100) for _ in range(n)]


def find_most_common_counter(array):
    c = Counter(array)
    return c.most_common()[0]


def find_most_common_dict(array):
    count = dict()
    freq = 0
    max_n = 0
    for i in array:
        if count.get(i):
            count[i] += 1
        else:
            count[i] = 1
        if count[i] > freq:
            freq, max_n = count[i], i
    return f"Max number: {max_n}\nNumber of occurrences: {freq}"


def find_most_common_double(array):
    count = dict()
    freq = 0
    max_n = 0
    for i in array:
        temp_n = ""
        for n in str(i):
            temp_n += n
        temp_n = int(temp_n)
        if count.get(temp_n):
            count[temp_n] += 1
        else:
            count[temp_n] = 1
        if count[temp_n] > freq:
            freq, max_n = count[temp_n], temp_n
    return f"Max number: {max_n}\nNumber of occurrences: {freq}"


i = 100
rnd_lst = rnd_lst_gen(i)

print(timeit('find_most_common_counter(rnd_lst)', number=1000, globals=globals()))  # 0.016834500000000002
print(timeit('find_most_common_dict(rnd_lst)', number=1000, globals=globals()))  # 0.0198237
print(timeit('find_most_common_double(rnd_lst)', number=1000, globals=globals()))  # 0.0703145
print()

i = 1000
rnd_lst = rnd_lst_gen(i)

print(timeit('find_most_common_counter(rnd_lst)', number=1000, globals=globals()))  # 0.08239260000000001
print(timeit('find_most_common_dict(rnd_lst)', number=1000, globals=globals()))  # 0.2205857
print(timeit('find_most_common_double(rnd_lst)', number=1000, globals=globals()))  # 0.8371676000000001
print()

i = 10000
rnd_lst = rnd_lst_gen(i)

print(timeit('find_most_common_counter(rnd_lst)', number=1000, globals=globals()))  # 0.4703027999999998
print(timeit('find_most_common_dict(rnd_lst)', number=1000, globals=globals()))  # 2.4569052000000005
print(timeit('find_most_common_double(rnd_lst)', number=1000, globals=globals()))  # 8.5223114

i = 100000
rnd_lst = rnd_lst_gen(i)

print(timeit('find_most_common_counter(rnd_lst)', number=1000, globals=globals()))  # 5.859032400000002
print(timeit('find_most_common_dict(rnd_lst)', number=1000, globals=globals()))  # 26.638473299999998
print(timeit('find_most_common_double(rnd_lst)', number=1000, globals=globals()))  # 79.3983393

cProfile.run('find_most_common_counter(rnd_lst)')
cProfile.run('find_most_common_dict(rnd_lst)')
cProfile.run('find_most_common_double(rnd_lst)')

i = 1000000
rnd_lst = rnd_lst_gen(i)

cProfile.run('find_most_common_counter(rnd_lst)')
cProfile.run('find_most_common_dict(rnd_lst)')
cProfile.run('find_most_common_double(rnd_lst)')
