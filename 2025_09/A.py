input = '''16
Ana
Konstantine
Andro
Murtazi
Ia
Zz
Giorgi
Gesfhweoifwhe
Aaaaaaaaaaaaa
Abcdefghijklmn
Pqwoerqwyfjsjck
Xeligamishvi
Vasomamadzagli
Kilimandzharo
Aaaaaaaaaaaaaab
Baaaaaaaaaaaaab'''

for i,name in enumerate(input.split('\n')):
    if i == 0:
        continue
    count = len(set(name.lower()))
    discount = .05*count
    percent = (1-discount)*100
    print(f'Case #{i}: {percent}')
