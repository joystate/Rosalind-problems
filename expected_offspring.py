file = '/Users/nadia/Downloads/rosalind_iev (6).txt'
 
def num_offspring(file):
    f = open(file).read().replace('\n', '')
    given_data = f.split()
    data = []
    for i in given_data:
        data.append(int(i))
    probabilities = [2.0, 2.0, 2.0, 1.5, 1.0, 0]
    print sum([x * y for x, y in zip(probabilities, data)])
        
num_offspring(file)

