from timeit import timeit
import itertools


def prime_from_web(n):
    res = []
    c = itertools.count()
    for num in c:
        if all(num % i != 0 for i in range(2, num)):
            res.append(num)
            if len(res) >= n:
                return res[-1]


def prime(n):
    res = []
    c = itertools.count(2)
    for num in c:
        if all(num % i != 0 for i in range(2, num)):
            res.append(num)
            if len(res) >= n:
                return res[-1]


def sieve_func(n):
    if n == 1:
        return 2
    sieve = [i for i in range(n * n)]
    sieve[1] = 0
    res = []
    for i in range(2, len(sieve)):
        if sieve[i] != 0:
            res.append(i)
            j = i + i
            while j < len(sieve):
                sieve[j] = 0
                j += i

    return res[n - 1]


# test
print(sieve_func(20))
print(prime(20))

prime_n = 100
# print(timeit("prime(prime_n)", number=1000, globals=globals()))  # 1.2329802
# print(timeit("sieve_func(prime_n)", number=1000, globals=globals()))  # 3.6721727

prime_n = 1000
print(timeit("prime_from_web(prime_n)", number=1000, globals=globals()))  # 224.7664485
# print(timeit("sieve_func(prime_n)", number=1000, globals=globals()))  # 652.9537038
