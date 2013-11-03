#!/usr/bin/env python

#open file and turn it into a string
file = '/Users/nadia/Downloads/rosalind_revp (12).txt'
f = open(file).read().replace('\n', '')
#find the FASTA
import re
fasta = re.findall('^>Rosalind_[0-9]*', f)
#remove FASTA from dna 
dna = f[len(fasta[0]):]

def find_indexes(sub, s):#helper function to find all indexes of substr in str
    pos = 0
    indices = []
    while True:
        i = s.find(sub,pos)
        if i==-1:
            break
        indices.append(i+1)
        pos = i+1
    return indices
    

def is_reverse_pal(dna): #check if a piece of dna is a reverse palindrome
    #find complement and reverse it
    from string import maketrans
    intab = 'ATCG'
    outtab = 'TAGC'
    trantab = maketrans(intab, outtab)
    reversed_complement = dna.translate(trantab)[::-1]
    #check if they match
    if dna == reversed_complement:
        return True
    else:
        return False
    
def tokenize_dna(dna):
    tokens = []
    #iterate dna_string multiple times using various sequence length (4..12)
    for seq_len in range(4, 13):
        #walk-through dna_string using given seq_len
        for start_pos in range(len(dna)-seq_len):
            tokens.append(dna[start_pos:start_pos+seq_len])
#     if 'ATGCAT' in tokens:
#         print dna.find('ATGCAT') + 1
    return tokens
    
def find_rev_pals(dna):
    #finds reverse complements in dna string
    tokens = tokenize_dna(dna)
    reverse_pals = []
    for token in tokens:
        if is_reverse_pal(token):
            reverse_pals.append(token)
    return reverse_pals

def main(dna):
    pal_to_inds = {}
    reverse_pals = find_rev_pals(dna)
    for pal in reverse_pals:
        ind = find_indexes(pal, dna)
        pal_to_inds[pal] = ind 
    for pal in pal_to_inds:
        for ind in pal_to_inds[pal]:
            print ind, len(pal)
        
main(dna)