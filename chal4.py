#Rabbits and Recurrence Relations 6/22/2024
#n is the number of months and k is the number of pairs each rabbit pair gives birth to

n = 32; k = 3; months = 2; num_adults = 1; num_babies = 0; num_newbabies = 0

if n == 1 or n == 2:
    print("1")

else:

    while months < n:

        months += 1
        
        num_newbabies = num_adults * k

        num_adults += num_babies

        num_babies = num_newbabies

        num_newbabies = 0


pairs = num_babies + num_adults

print(f"{pairs}")