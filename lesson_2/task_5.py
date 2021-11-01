start = 32
end = 127

i = start
sym_seq = ""
sym_line = ""

while i <= end:
    s = chr(i)
    if sym_line.count("|") > 9:
        sym_seq += sym_line + "\n"
        sym_line = ""
    sym_line = sym_line + str(i) + " " + "-" + " " + s + "| "
    i += 1
else:
    sym_seq += sym_line


print(sym_seq)
