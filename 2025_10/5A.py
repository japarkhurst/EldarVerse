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
    elif '(' not in row: # reset for each case
        case += 1
        ingredients= {}
        good_cnt = 0
    elif row.startswith('='): # test each recipe
        good = True
        for ing_str in row.strip('= ').split(', '):
            ing,cnt = ing_str.split(' (')
            cnt = int(cnt.strip(')'))
            if cnt > ingredients.get(ing,0):
                good = False
                break
        if good:
            good_cnt += 1
    else: # get ingredients
        ing,cnt = row.split(' (')
        ingredients[ing] = int(cnt.strip(')'))

        
    