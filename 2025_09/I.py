input = '''1
4 6
gojira
rachvela
lekva
samurai
ADD gojira rachvela
ADD gojira lekva
ADD lekva samurai
SUGGEST samurai
ADD samurai gojira
SUGGEST samurai'''

from collections import defaultdict
friends = defaultdict(set())
for i,row in enumerate(input.split('\n')):
    if i < 1:
        continue
    elif row[0] == 'A':
        _,f1,f2 = row.split(' ')
        friends[f1].add(f2)
        friends[f2].add(f1)
        
