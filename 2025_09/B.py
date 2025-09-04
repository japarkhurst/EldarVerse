input = '''2
2 0
3 2'''
W,L = 'W','L'
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
    for H in range(1,N+1):
        for A in range(1,N+1):
            if H != A:
                games.append((H,A))
    print(games)
gameCount = cnt
current = [[W]*gameCount]
cumulative = []
for i in range(N):
    print(i)
    print(current)
    cumulative += current
    current = cumulative[::]
    print(cumulative)
    new_results = []
    for j in range(len(current)):
        result = current[j][::]
        result[i] = L
        new_results.append(result)
        print(f'{result=}')
    current = new_results
    print(current)
    
