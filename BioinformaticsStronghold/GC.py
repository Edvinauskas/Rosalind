def read_fasta_format(file_name):
    data = {}
    with open(file_name) as f:
        label_id = ''
        for line in f:
            if line[0] == '>':
                label_id = line[1:].strip()
                data[label_id] = ''
            else:
                data[label_id] += line.strip()
    return data

def calculate_highest_gc_content(fasta_dict):
    highest_gc_content = {'fasta_id':'','dna_gc_content':0}
    for fasta_id, dna in fasta_dict.items():
        g_molecule_count = dna.count('G')
        c_molecule_count = dna.count('C')
        gc_content = ((g_molecule_count + c_molecule_count) / len(dna)) * 100
        if gc_content > highest_gc_content['dna_gc_content']:
            highest_gc_content['fasta_id'] = fasta_id
            highest_gc_content['dna_gc_content'] = gc_content
    return highest_gc_content


file_name = 'GC_input.txt'
fasta_data = read_fasta_format(file_name)
highest_gc_content = calculate_highest_gc_content(fasta_data)
print(highest_gc_content['fasta_id'], '\n', highest_gc_content['dna_gc_content'])

