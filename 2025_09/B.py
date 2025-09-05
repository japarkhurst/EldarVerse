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

solutions = []
for case,(N,K) in enumerate(cases,1):
    gameCount = N * (N-1)
    print(f'Games: {gameCount}')
    games = []
    for H in range(1,N+1):
        for A in range(1,N+1):
            if H != A:
                games.append((H,A))
    #print(games)
    current = [[W]*gameCount]
    cumulative = []
    for i in range(len(games)):
        #print(i)
        #print(current)
        cumulative += current
        current = cumulative[::]
        #print(cumulative)
        new_results = []
        for j in range(len(current)):
            result = current[j][::]
            result[i] = L
            new_results.append(result)
            #print(f'{result=}')
        #print(len(new_results))
        current = new_results
        #print(current)
    cumulative += current
    #print(cumulative)
    #print(len(cumulative))
    
    sparseCount = 0
    for result in cumulative:
        resultDict = dict(zip(games,result))
        #print(resultDict)
        scores = []
        maxScore = 0
        minScore = 1000
        for team in range(1,N+1):
            homeWins = len([R for (H,A),R in resultDict.items() if R==W and H==team])
            awayWins = len([R for (H,A),R in resultDict.items() if R==L and A==team])
            score = homeWins + awayWins
            maxScore = max(score,maxScore)
            minScore = min(score,minScore)
            scores.append((team,score))
        rankings = sorted(scores,key=lambda x:x[1],reverse=True)
        #print(rankings)
        if maxScore-minScore > K:
            sparseCount+=1
    print(f'{sparseCount=}')
    solutions.append(f'Case #{case}: {sparseCount}')
    
print('\n\n')
print("\n".join(solutions))
