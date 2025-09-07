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

import string
lowers = string.ascii_lowercase
from collections import defaultdict
friends = defaultdict(set)
case = 0
for i,row in enumerate(input.split('\n')):
    if i < 1:
        continue
    elif row[0] in lowers:
        continue
    elif row[0] == 'A':
        _,f1,f2 = row.split(' ')
        friends[f1].add(f2)
        friends[f2].add(f1)
    elif row[0] == 'R':
        _,f1,f2 = row.split(' ')
        friends[f1].discard(f2)
        friends[f2].discard(f1)
    elif row[0] == 'S':
        _,x = row.split(' ')
        xF = friends[x]
        options = set()
        maxMutualCount = -1
        for y,yF in friends.items():
            mutualCount = len([_ for _ in yF if _ != x and _ in xF])
            if mutualCount > maxMutualCount:
                options = {y}
            elif mutualCount == maxMutualCount:
                options.add(y)
        suggest = min(options)
        print(suggest)
    else:
        case += 1
        print(f'Case #{case}')
    
        
