#Mendel's First Law
#Given: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
#Return: The probability that two randomly selected mating organisms will produce an individual possessing 
#        a dominant allele.

k = 20; m = 26; n = 26; probability = 0
total = k + m + n

#HH
probability += (k / total) *  ((k - 1) / (total - 1)) #HH
probability += (k / total) * (m / (total - 1)) #Hh
probability += (k / total) * (n / (total - 1)) #hh

#Hh
probability += (m / total) * (k / (total - 1)) #HH
probability += (m / total) * ((m - 1) / (total - 1)) * (0.75) #Hh
probability += (m / total) * (n / (total - 1)) * (0.5)

#hh
probability += (n / total) * (k / (total - 1)) #HH
probability += (n / total) * (m / (total - 1)) * (0.5) #Hh


print(f"{probability}")
