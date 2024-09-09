#DNA to RNA
import os 

rna_line = ""

workingDirectory = os.path.dirname(__file__)

with open(os.path.join(workingDirectory, "rosalind_dna.txt"), 'r') as dataset:
    
    line = dataset.readline()

convert_nuc = {"A" : "A", "G" : "G", "C" : "C", "T" : "U"}


for x in range(len(line)):
    rna_line += convert_nuc[line[x]]

print(f"{rna_line}")