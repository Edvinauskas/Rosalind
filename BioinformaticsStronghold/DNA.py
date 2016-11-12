dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
molecule_a = 0
molecule_c = 0
molecule_g = 0
molecule_t = 0
for molecule in dna:
    if molecule == "A":
        molecule_a += 1
    elif molecule == "C":
        molecule_c += 1
    elif molecule == "G":
        molecule_g += 1
    elif molecule == "T":
        molecule_t += 1

print(molecule_a, molecule_c, molecule_g, molecule_t, sep=" ")