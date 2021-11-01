def seq_sum(number):
    n = 1
    m = 1
    i = number
    while i > 1:
        m = m / -2
        n += m
        i -= 1
    return n


seq_count = int(input("Input number of elements in sequence: "))
res = seq_sum(seq_count)
print(res)
