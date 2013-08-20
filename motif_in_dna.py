file = '/Users/nadia/Downloads/rosalind_subs (1).txt'

def motif(file):
    f = open(file).read()
    
    import re
    
    pattern = re.compile('^[A|C|G|T]*$\n?', re.MULTILINE)
    seqs = re.findall(pattern, f)
    
    seq1 = seqs[0].rstrip()
    seq2 = seqs[1].rstrip()
    
    indexes = [a.start() for a in list(re.finditer('(?=%s)'%seq2, seq1))]
    output = ''
    for i in indexes:
        output += str(i+1) + ' '
    print output
    
    

motif(file)