file = '/Users/nadia/Downloads/rosalind_prot (1).txt'

codon_table = {"UUU": "F",
"CUU": "L",
"AUU": "I",
"GUU": "V",
"UUC": "F",
"CUC": "L",
"AUC": "I",
"GUC": "V",
"UUA": "L",
"CUA": "L",
"AUA": "I",
"GUA": "V",
"UUG": "L",
"CUG": "L",
"AUG": "M",
"GUG": "V",
"UCU": "S",
"CCU": "P",
"ACU": "T",
"GCU": "A",
"UCC": "S",
"CCC": "P",
"ACC": "T",
"GCC": "A",
"UCA": "S",
"CCA": "P",
"ACA": "T",
"GCA": "A",
"UCG": "S",
"CCG": "P",
"ACG": "T",
"GCG": "A",
"UAU": "Y",
"CAU": "H",
"AAU": "N",
"GAU": "D",
"UAC": "Y",
"CAC": "H",
"AAC": "N",
"GAC": "D",
"UAA": "Stop",
"CAA": "Q",
"AAA": "K",
"GAA": "E",
"UAG": "Stop",
"CAG": "Q",
"AAG": "K",
"GAG": "E",
"UGU": "C",
"CGU": "R",
"AGU": "S",
"GGU": "G",
"UGC": "C",
"CGC": "R",
"AGC": "S",
"GGC": "G",
"UGA": "Stop",
"CGA": "R",
"AGA": "R",
"GGA": "G",
"UGG": "W",
"CGG": "R",
"AGG": "R",
"GGG": "G "}


def rna_to_protein(file):
    f = open(file).read().replace('\n', '')
    protein_chain = ''
    for i in xrange(0, len(f), 3):
        if codon_table[f[i:i+3]] != 'Stop':
            protein_chain += codon_table[f[i:i+3]]
    print protein_chain
        
    
rna_to_protein(file)
    
