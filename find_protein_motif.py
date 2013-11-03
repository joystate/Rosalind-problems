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
    
def open_page(protein):
    import urllib2
    import re
    data = urllib2.urlopen('http://www.uniprot.org/uniprot/%s.fasta'%protein).read()
    fasta = re.findall('^>(.*)\n', data)
    chain = data[len(fasta[0]):]
    return chain.replace('\n', '')

def find_pattern():
    chain = open_page(protein)
    import re
    glyc = re.findall(r'(?=(N[^P][S|T][^P]))', chain)
    inds = []
    for gl in glyc:
        inds.append(str(chain.find(gl)))
    return ' '.join(inds)
                
file = '/Users/nadia/Downloads/rosalind_mprt (3).txt'
f = open(file).readlines()
proteins = []
for protein in f:
    protein = protein.rstrip()
    proteins.append(protein)
for protein in proteins:
    open_page(protein)
    if find_pattern() != '':
        print protein
        print find_pattern()   




    