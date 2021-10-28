l_1, l_2 = map(ord, input("Input two symbols from alphabet, separated by space: ").split())

print(f"Place of '{chr(l_1)}' in alphabet: {l_1 - ord('a') + 1}\n"
      f"Place of '{chr(l_2)}' in alphabet: {l_2 - ord('a') + 1}")

l_1 = l_1 - ord('a') + 1
l_2 = l_2 - ord('a') + 1

print(f"Number of characters between {l_1} and {l_2}: {abs(l_1 - l_2) - 1}")
