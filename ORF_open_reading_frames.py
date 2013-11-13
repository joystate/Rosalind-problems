#!/usr/bin/env python

#open file and turn it into a string
file = '/Users/nadia/Downloads/rosalind_mprt.txt'
f = open(file).read().replace('\n', '')
#find the FASTA
import re
fasta = re.findall('^>Rosalind_[0-9]*', f)
#remove FASTA from dna 
dna = f[len(fasta[0]):]

def tokenize_dna(dna, num):#divide dna to codons
    codons = [dna[start:start+num] for start in range(0, len(dna), num)]
    return codons

def find_orfs():
    codons = tokenize_dna(dna, 3)
    for codon in codons:
        if codon in ['TAG', 'TGA','TAA']:
            print codon
        
    
find_orfs()    
