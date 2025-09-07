input = '''2
3 4 1
6 8 3'''

import math
for case,row in enumerate(input.split('\n')):
    if case == 0:
        continue
    a,b,i = row.split(' ')
    a,b,i = int(a), int(b), int(i)
    for _ in range(i):
        low,high = min(a,b), max(a,b)
        angle = math.atan(low/high)
        a = math.sin(angle) * high
        b = math.sqrt((high*high)-(a*a))
    area = (a*b)/2
    print(f'Case #{case}: {area}')
        
