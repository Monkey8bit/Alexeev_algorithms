def sum_check(seq):
    max_sum = 0
    temp_sum = 0
    max_number = ""
    cur_number = ""
    for number in seq:
        if number == " ":
            if temp_sum > max_sum:
                max_sum = temp_sum
                max_number = cur_number
            temp_sum = 0
            cur_number = ""
        else:
            temp_sum += int(number)
            cur_number += number
    return f"Number with max sum of digits: {max_number}.\nSum of digits: {max_sum}."


num_seq = input("Input numbers, separated by space: ")
res = sum_check(num_seq)

print(res)