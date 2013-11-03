file = '/Users/nadia/Downloads/rosalind_gc.txt'

def ident_unknown_dna(file):
    f = open(file).read().replace('\n', '')
    
    import re
    import operator
    
    raw_lines = re.findall('>Rosalind_[0-9]*[A|C|G|T]*', f)
    fasta_to_cont = {}
    for line in raw_lines:
        fasta = line[1:len('>Rosalind_0000')]
        chain = line[len('>Rosalind_0000'):]
        gc = chain.count('G') + chain.count('C')
        gc_cont = float(gc)/float(len(chain)) * 100
        fasta_to_cont[fasta] = round(gc_cont, 6)
    print max(fasta_to_cont.iteritems(), key=operator.itemgetter(1))[0]
    print max(fasta_to_cont.iteritems(), key=operator.itemgetter(1))[1]
        
        
ident_unknown_dna(file)