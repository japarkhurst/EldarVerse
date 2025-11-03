input = '''1
#|,  .-.  .-.  ,|#
####`--------`####
#(_     ^^     _)#
##/            \##
$##.-"  "  "'-.#$#
##################
#|/     /\     \|#
#| )(_o/  \o_)( |#
###| \IIIIII/ |###
##>09044444444<###
###\          /###
##################
##\__|IIIIII|__/##
====='''

results = []
case = 1
for i,row in enumerate(input.split('\n')):
    if i == 0:
        continue
    lIndex = row.index('>')
    rIndex = row.index('<')
    if lIndex and rIndex:
        token = row[lIndex+1:rIndex]
    
        results.append(f'Case #{case}: {token}')
        case+=1

print("\n".join(results))
