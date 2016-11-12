dna='AAAACCCGGT'
dna_complement = ''
 # 'A' and 'T' are complements of each other, as are 'C' and 'G'.
for nucleotide in dna[::-1]:
	if nucleotide == 'A':
		dna_complement += 'T'
	elif nucleotide == 'T':
		dna_complement += 'A'
	elif nucleotide == 'C':
		dna_complement += 'G'
	elif nucleotide == 'G':
		dna_complement += 'C'
print(dna_complement)