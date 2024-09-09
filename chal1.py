#Counts the number of each nucleotide

a_count = 0
c_count = 0
t_count = 0
g_count = 0

import os
workingDirectory = os.path.dirname(__file__)

with open(os.path.join(workingDirectory, "rosalind_dna.txt"), 'r') as dataset:
    
    line = dataset.readline()

for x in range(len(line)):
    if line[x] == 'A':
        a_count += 1
    if line[x] == 'C':
        c_count += 1
    if line[x]== 'T':
        t_count += 1
    if line[x] == 'G':
        g_count += 1

print(f"{a_count} {c_count} {g_count} {t_count}")