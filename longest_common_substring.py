file = '/Users/nadia/Downloads/rosalind_cons (3).txt'

def ancestor(file):
    import re
    import numpy

    f = open(file).read().replace('\n', '')
    raw_lines = re.findall('>Rosalind_[0-9]*[A|C|G|T]*', f)
    chains = []
    for line in raw_lines:
        line = re.sub('>Rosalind_[0-9]*', '', line)
        chains.append(list(line))
        
    x = numpy.array(chains)
    
    profile_a = []
    profile_c = []
    profile_g = []
    profile_t = []
    profile = []
    for i in x.T:
        profile_a.append(list(i).count('A'))
        profile_c.append(list(i).count('C'))
        profile_g.append(list(i).count('G'))
        profile_t.append(list(i).count('T'))
    profile.append(profile_a)
    profile.append(profile_c)
    profile.append(profile_g)
    profile.append(profile_t)
      
    z = numpy.array(profile)
      
    ancestor_str = ''
      
    for i in enumerate(list(z.max(axis = 0))):
        if profile[0][i[0]] == list(z.max(axis = 0))[i[0]]:
            ancestor_str += 'A'
        elif profile[1][i[0]] == list(z.max(axis = 0))[i[0]]:
            ancestor_str += 'C'
        elif profile[2][i[0]] == list(z.max(axis = 0))[i[0]]:
            ancestor_str += 'G'
        elif profile[3][i[0]] == list(z.max(axis = 0))[i[0]]:
            ancestor_str += 'T'
              
    print ancestor_str
    print 'A: ' + ' '.join(map(str, profile_a))
    print 'C: ' + ' '.join(map(str, profile_c))
    print 'G: ' + ' '.join(map(str, profile_g))
    print 'T: ' + ' '.join(map(str, profile_t)) 
    
         
ancestor(file)