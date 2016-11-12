dna_1='GAGCCTACTAACGGGAT'
dna_2='CATCGTAATGACGGCCT'

hamming_distance = 0

for molecule in range(len(dna_1)):
    if dna_1[molecule] != dna_2[molecule]:
        hamming_distance += 1

print(hamming_distance)