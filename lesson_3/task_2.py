from random import randint


lst = [randint(1, 100) for i in range(1, 100)]
even_idx_lst = [lst.index(i) for i in lst if i % 2 == 0]

print(f"Indexes for even numbers in list: {even_idx_lst}")
