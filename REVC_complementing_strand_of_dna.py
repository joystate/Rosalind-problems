file = '/Users/nadia/Downloads/rosalind_revc.txt'

def sec_and_tert_structures(file):
    f = open(file).read().replace('\n', '')
    
    from string import maketrans
    intab = 'ATCG'
    outtab = 'TAGC'
    trantab = maketrans(intab, outtab)
    
    print f.translate(trantab)[::-1]
    

sec_and_tert_structures(file)