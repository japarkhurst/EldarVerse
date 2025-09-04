input = '''2
2 0
3 2'''

cases = []
for i,row in enumerate(input.split('\n')):
    if i == 0:
        continue
    N,K = row.split(' ')
    N,K = int(N),int(K)
    cases.append((N,K))


for i,(N,K) in enumerate(cases,1):
    games = N * (N-1)
    print(f'Games: {games}')
    
