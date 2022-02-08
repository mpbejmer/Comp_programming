# Problem 28

nbr = 1
tot_sum = 0

gap = 2

side = 1001
nbr_max = side*side

tot_sum += nbr
while (nbr < nbr_max):

    for i in range(0, 4):
        nbr += gap
        tot_sum += nbr

    gap += 2

print(tot_sum)
