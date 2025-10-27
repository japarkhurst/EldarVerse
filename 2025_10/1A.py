input = '''4
7 158
10 777
12 012345
1 235'''

results = []
for i,row in enumerate(input.split('\n')):
    if i == 0:
        continue
    nights,sequence = row.split(' ')
    clans = list(sequence)
    clanCount = len(clans)
    countDict = {c:0 for c in clans}
    n = 0
    clanIndex = 0
    while n < int(nights):
        n+=1
        clan = clans[clanIndex]
        clanIndex+=1
        if clanIndex >= clanCount:
            clanIndex = 0
        countDict[clan]+=1
    #print(countDict)
    counts = countDict.values()
    results.append(f'Case #{i}: {max(counts)} {min(counts)}')
    
print("\n".join(results))
