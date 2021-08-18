# ====== main code ====================================== #
with open('goats.txt') as f1, open('answer.txt', 'w') as f2:
    cont = f1.read().split('\n')
    colors, goats = cont[1:cont.index('GOATS')], cont[cont.index('GOATS')+1:]
    print(*sorted(filter(lambda x: goats.count(x) / len(goats) > 0.07, colors)), sep='\n', file=f2)
# ====== end of code ==================================== #
