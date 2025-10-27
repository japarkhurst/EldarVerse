for i,name in enumerate(input.split('\n')):
    if i == 0:
        continue
    count = len(set(name.lower()))
    discount = .05*count
    percent = int(round((1-discount)*100))
    print(f'Case #{i}: {percent}')
