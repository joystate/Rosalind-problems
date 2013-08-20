file = '/Users/nadia/Downloads/rosalind_dna.txt'

def count_nucleotides(file):
    f = open(file).read().replace('\n', '')
    import collections
    count = collections.Counter()
    for nucleotide in list(f):
        count[nucleotide] += 1
    print count['A'], count['C'], count['G'], count['T']
    
count_nucleotides(file)

        




        
