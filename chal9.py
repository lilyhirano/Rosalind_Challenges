#Finding a Motif in DNA 8/23/2024


s_str = "ATTAGAGCTCGATGGTCAGGACACCGATGGTGCCGATGGTCGATGGTCGATGGTCCGATGGTAATAATATCGATGGTCGATGGTCGATGGTCGATGGTCGATGGTGCCCTGTTCGATGGTACCACGATGGTTACCGATGGTGCGATGGTCGATGGTAGTTCGATGGTACTCGATGGTCCGATGGTGACCCCTGCCGCGATGGTACGATGGTGCCAATTGTGCGCGATGGTACGATGGTTCGATGGTCCGATGGTCATCGATGGTCGATGGTGAACCGATGGTCGATGGTACGCGCCGCGATGGTCCACGATGGTAGTGGCCACGATGGTCATCGATGGTCGATGGTGCCGCGATGGTGGTTGCGATGGTCAACCGATGGTAAAAGTCCGATGGTTATCGATGGTGCGATGGTCGATGGTTCGATGGTGTCTCGATGGTTCTGCGGCCGATGGTAGCCGATGGTCGATGGTAGCGATGGTCGATGGTTGCGTCCATCTTCGATGGTGCCGATGGTTCGATGGTTCGATGGTACCGCGATGGTCGATGGTGGCGATGGTGGCGATGGTCGATGGTCGATGGTCGATGGTGCGATGGTACCGATGGTGACTCGCGATGGTACGATGGTCCGATGGTCATGTCCGATGGTCGATGGTATACACGATGGTCGATGGTTCGATGGTTAGTCGATGGTAAGAACGATGGTCGATGGTCAACCAACGATGGTTCTTACTGCGATGGTGTCGATGGTCCCTTGGCGATGGTTCACACGATGGTCGATGGTGTATCTTCGATGGTGGTACGATGGTCGATGGTCATAGCGATGGTCCGATGGTGCCGATGGTACCCGATGGTCGATGGTAAGCGATGGTGACACGATGGTTCCACCGATGGTCGATGGTTCGATGGTCGATGGTCGATCGATGGTCGATGGTACGATGGTCGATGGTGCGGACAGAGACGATTGGCGATGGTTTCGATGGTCGATGGTCGATGGT"
t_str = "CGATGGTCG"
index = 0; x = 0; y = 0; found = []; found_str = ""

while x < len(s_str):
    x += 1
    if (s_str[index : len(t_str) + index].find(t_str) != -1):
        found.append(index + 1)
        #s_str = s_str.replace(s_str[0], "", 1)
        index += 1
    
    else:
        index += 1

while y < len(found):
    print(f"{found[y]}", end = " ")
    y += 1