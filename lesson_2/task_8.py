def num_count(num, seq):
    # easy way
    # return seq.count(num)
    count = 0
    for n in seq:
        if n == num:
            count += 1
    return count


digit = input("Input digit to calculate count in number sequence: ").strip()
num_seq = input("Input numbers, separated by space: ")
res = num_count(digit, num_seq)

print(f"Count of {digit} in {num_seq}: {res}")
