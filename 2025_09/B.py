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
    cnt = N * (N-1)
    print(f'Games: {cnt}')
    games = []
    for H in range(1,cnt+1):
        for A in range(1,cnt+1):
            if H != A:
                games.append((H,A))
    print(games)
