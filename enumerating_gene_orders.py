file = '/Users/nadia/Downloads/rosalind_perm (4).txt'

def permuts(file):
    f = open(file).read()
    
    import itertools
    
    perms = list(itertools.permutations(range(1, int(f) + 1)))
    print len(perms)
    for i in perms:
        print str(i)[1:-1].replace(',', ' ')
        
    
#     print len(list(itertools.permutations(range(int(f)))))
#     for i in itertools.permutations(range(int(f))):
#         print str(i)[1:-1].replace(',', ' ')
    
permuts(file)
