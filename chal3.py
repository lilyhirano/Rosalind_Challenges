#Reverse complement of a DNA string

import os
complement = ""


workingDirectory = os.path.dirname(__file__)

with open (os.path.join(workingDirectory, "rosalind_dna.txt"), "r") as dataset:
    line = dataset.readline()

convert_dna = {"A" : "T", "T" : "A", "G" : "C", "C" : "G"}

for x in range(len(line)):
    complement += convert_dna[line[x]]

i = len(line) - 1
while i >= 0:
    print(complement[i], end = "")
    i -= 1
