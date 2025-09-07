input = '''4
pythonia
python
pythoner
geolymp
=====
pythonia<<<<<<<<geolymp'''

words = set()
for i,word in enumerate(input.split('\n')):
    if i == 0:
        continue
    elif word == '=====':
        break
    else:
        words.add(word)
sequence = input.split('\n')[-1]

search = []
for s in sequence:
    if search == '<':
        search.pop()
    else:
        search.append(s)
    if len(search) >= 3:
        searchText = ''.join(search)
        cnt = len([w for w in words if w.startswith(searchText)])
        if cnt:
            print(cnt)
