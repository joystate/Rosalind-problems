file = '/Users/nadia/Downloads/rosalind_grph (1).txt'

def overlap(file):
    f = open(file).read().replace('\n', '')
    
    import re
    import itertools
    
    raw_lines = re.findall('>Rosalind_\d+[A|C|G|T]*', f)
    fasta_to_chain = {}
    for line in raw_lines:
        fasta = re.sub('[A|C|G|T]*', '', line)[1:]
        chain = re.sub('>Rosalind_\d+', '', line)
        fasta_to_chain[chain] = fasta
    
    chains = []
    for i in fasta_to_chain:
        chains.append(i)
        
    for pair in itertools.product(chains, repeat = 2):
        if pair[0] != pair[1]:
            suffix = ''
            i = -3
            j = 0
            while j < 3:
                if pair[0][i] == pair[1][j]:
                    suffix += pair[1][j]
                    i += 1
                    j += 1
                else:
                    i += 1
                    j += 1
            if len(suffix) == 3:
                print fasta_to_chain[pair[0]], fasta_to_chain[pair[1]]
                                
overlap(file)
                               
