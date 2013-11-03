file = '/Users/nadia/Downloads/rosalind_hamm.txt'

def hamming_dist(file):
    f = open(file).read()
    
    import re 
    import operator
    
    pattern = re.compile('^[A|C|G|T]*$\n?', re.MULTILINE)
    seqs = re.findall(pattern, f)
    
    seq1 = seqs[0].rstrip()
    seq2 = seqs[1].rstrip()
    
    print map(operator.eq, seq1, seq2).count(False)

    
hamming_dist(file)
    

