def reverse(num):
    rev_n = 0
    i = num
    while i > 0:
        rev_n = rev_n * 10 + i % 10
        i //= 10
    return rev_n


def rec_rev(num):
    i = num
    rev_num = ""
    while i > 0:
        rev_num += str(i % 10)
        i //= 10
        rec_rev(i)
    return int(rev_num) if rev_num != "" else 0


number = int(input("Input number: "))
res = reverse(number)
print(res)
print(rec_rev(100500))
