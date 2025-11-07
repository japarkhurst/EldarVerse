input = '''1
3 3
wool of bat (5)
eye of newt (1)
owlet's wing (3)
= wool of bat (2), eye of newt (1), owlet's wing (3)
= hobbit's nail (10)
= wool of bat (1), eye of newt (2), owlet's wing (2)'''

case = 0
for i,row in enumerate(input.split('\n')):
    if i == 0:
        continue
    elif '(' not in row:
        case += 1
        ingredients= {}
        good_cnt = 0
    elif row.startswith('='):
        recipe = row
    else:
        ing,cnt = row.split(' (')
        ingredients[ing] = int(cnt.strip(')'))

        continue
    