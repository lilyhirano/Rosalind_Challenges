#Finds highest GC content 6/22/2024

import os

protein = ""; name = []; gc_content = []; dna = ""; check1 = 1; x = 0

workingDirectory = os.path.dirname(__file__)
with open(os.path.join(workingDirectory, "rosalind_fasta.txt"), 'r') as dataset:
        
        if x == 0: #get the first name
            name.append(dataset.readline())
            x += 1

        while (check1 == 1):
            check_line = dataset.readline()

            if len(check_line) == 0: #if at the end of the file, calculate the final gc content
               
               dna = dna.replace("\n", "") #gets rid of newline

               g_count = dna.count("G")
               c_count = dna.count("C")
               gc = g_count + c_count
               gc_content.append((gc / len(dna) * 100))

               break
  

            if check_line.find(">") == -1: #if there is not a > in the line, it is DNA
                dna += check_line   #add onto the dna line
            else:
                name.append(check_line) #if there is a >, it is the next name

                dna = dna.replace("\n", "") #gets rid of newline

                g_count = dna.count("G")
                c_count = dna.count("C")
                gc = g_count + c_count

                basepairs = len(dna)
                gc_content.append((gc / len(dna) * 100))

                dna = ""

maximum = max(gc_content) #maximum gc content
index = gc_content.index(max(gc_content)) #index of max gc content

name_max = name[index].replace(">", "") #formatting

print(f"{name_max}{maximum}")

