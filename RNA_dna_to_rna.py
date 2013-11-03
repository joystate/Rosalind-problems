file = '/Users/nadia/Downloads/rosalind_rna.txt'

def dna_to_rna(file):
    f = open(file).read().replace('\n', '')
    print f.replace('T', 'U')
    
dna_to_rna(file)