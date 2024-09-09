#Finding a Most Likely Common Ancestor

name = []; check_line = []; dna_lines =[]
line = ""; consensus_str = ""
A_count = ""; C_count = ""; G_count = ""; T_count = ""; nuc_count = []
x = 0; check = 1; index = 0; index2 = 0; maximum = 0

import os 

workingDirectory = os.path.dirname(__file__)
with open(os.path.join(workingDirectory, "rosalind_fasta.txt"), 'r') as dataset:
    
    check_line = dataset.readline()

    while check == 1:
    
        if len(check_line) != 0: 
            
            if check_line.find(">") >  -1:
                x += 1
            
            check_line = dataset.readline()
            
            if len(check_line) == 0:
                check = 0

            else:
                while check_line.find(">") ==  -1:
                    if len(check_line) == 0:
                        check = 0
                        break
                    line += check_line
                    check_line = dataset.readline()
                
                line = line.replace("\n", "")
                dna_lines.append(line)
                line = ""

        else: 
            check = 0

while index < len(dna_lines[0]):  #index toggles wich column is selected
    y = 0
    column = ""
    while y < x:
        for nucleotide in dna_lines[y][index]: #y toggles which string is selected.
            column += nucleotide
            y += 1
            
    A_count += str(column.count('A')) + " "
    C_count+= str(column.count('C')) + " "
    G_count += str(column.count('G')) + " "
    T_count+= str(column.count('T')) + " "

    index += 1

#consensus string
while index2 < len(A_count):

    nuc_count = [A_count[index2], C_count[index2], G_count[index2], T_count[index2]]
    maximum = nuc_count.index(max(nuc_count))
    index2 += 2 #to skip over spaces

    if maximum == 0:
        consensus_str += "A"
    if maximum == 1:
        consensus_str += "C"
    if maximum == 2:
        consensus_str += "G"
    if maximum == 3:
        consensus_str += "T"
 

print(consensus_str)
print("A:", A_count)
print("C:", C_count)
print("G:", G_count)
print("T:", T_count)